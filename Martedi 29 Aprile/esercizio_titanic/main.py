import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, r2_score
import os

# Caricamento del dataset Titanic
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'titanic.csv')
titanic = pd.read_csv(file_path)
df = titanic.copy()

# Funzione per stampare separatori di sezione
def separatore(title):
    print(f"\n{'='*10} {title} {'='*10}\n") 
    
def grafico_boxplot_modello(final_df):
    separatore("Boxplot delle Feature del Modello Ottimizzato")
    numeric_columns = final_df.select_dtypes(include=['float64', 'int64']).columns
    
    if numeric_columns.empty:
        print("Non ci sono colonne numeriche nel dataset del modello.")
        return
    
    plt.figure(figsize=(12, 8))
    sns.boxplot(data=final_df[numeric_columns], orient='h', palette='Set3')
    plt.title("Boxplot delle Feature del Modello Ottimizzato", fontsize=16)
    plt.xlabel("Valori", fontsize=12)
    plt.ylabel("Feature", fontsize=12)
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.show()
    
def rimuovi_multicollinearita(df, soglia=0.9):
    separatore("Rimozione Colonne Multicollineari")
    corr_matrix = df.corr().abs()
    upper_triangle = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
    to_drop = [column for column in upper_triangle.columns if any(upper_triangle[column] > soglia)]
    print(f"Colonne rimosse per multicollinearità (soglia > {soglia}): {to_drop}")
    df = df.drop(columns=to_drop)
    return df

# Funzione principale del menu
def menu():
    global df  # Rende df accessibile all'interno della funzione
    while True:
        # Mostra il menu all'utente
        print("\nMenu:")
        print("1. Analisi della struttura del dataset")  # Opzione per analizzare la struttura del dataset
        print("2. Pulizia del dataset")  # Opzione per pulire il dataset
        print("3. Analisi delle singole colonne")  # Opzione per analizzare le colonne
        print("4. Visualizzazione grafici")  # Opzione per visualizzare grafici
        print("5. Analisi delle relazioni tra colonne e target")  # Opzione per analizzare relazioni
        print("6. Creazione di nuove feature")  # Opzione per creare nuove feature
        print("7. Preparazione del dataset per il modello")  # Opzione per preparare il dataset
        print("8. Creazione e valutazione del modello predittivo")  # Opzione per creare un modello
        print("9. Ottimizzazione del modello predittivo")  # Opzione per ottimizzare il modello
        print("10. Regressione lineare con accuratezza e R quadro")  # Aggiunta al menu
        print("11. Visualizzazione Boxplot delle Feature")  # Aggiunta al menu
        print("0. Esci")  # Opzione per uscire
        
        # Input dell'utente
        scelta = input("Scegli un'opzione: ")
        
        if scelta == "1":
            # Analisi della struttura del dataset
            separatore("Struttura del dataset")
            print("Colonne del dataset:", df.columns.tolist())
            print("Tipi di dati delle colonne:\n", df.dtypes)
            print("Dimensioni del dataset:", df.shape)
        elif scelta == "2":
            # Pulizia del dataset
            separatore("Pulizia del dati")
            percentuali_mancanti = df.isnull().mean() * 100
            print("Percentuali di dati mancanti:\n", percentuali_mancanti[percentuali_mancanti > 0])

            df['Age'].fillna(df['Age'].median(), inplace=True)
            df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
            df.drop(columns=['Cabin', 'Ticket', 'Name', 'PassengerId'], inplace=True)
            df.dropna(inplace=True)

            clean_path = os.path.join(current_dir, 'titanic_clean.csv')
            df.to_csv(clean_path, index=False)
            print(f"Dataset pulito salvato in: {clean_path}")
        elif scelta == "3":
            # Analisi delle singole colonne
            separatore("Analisi delle singole colonne")
            print("Distribuzione età:\n", df['Age'].describe())
            print("\nDistribuzione prezzo biglietto:\n", df['Fare'].describe())
            print("\nValori Unici - sesso:\n", df['Sex'].unique())
            print("\nDistribuzione sesso:\n", df['Sex'].value_counts()*100)
            print("Valori Unici - porto di imbarco:\n", df['Embarked'].unique())
            print("Valori Unici - classe:\n", df['Pclass'].unique())
        elif scelta == "4":
            # Visualizzazione grafici
            separatore("Grafici")
            plt.figure(figsize=(10, 6))
            sns.histplot(df['Age'], kde=True, color='blue', bins=30, label='Distribuzione Età')
            plt.title('Distribuzione Età', fontsize=16)
            plt.xlabel('Età', fontsize=12)
            plt.ylabel('Frequenza', fontsize=12)
            plt.legend(loc='upper right')
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.show()

            plt.figure(figsize=(10, 6))
            sns.histplot(df['Fare'], kde=True, color='green', bins=30, label='Distribuzione Prezzo Biglietto')
            plt.title('Distribuzione Prezzo Biglietto', fontsize=16)
            plt.xlabel('Prezzo Biglietto', fontsize=12)
            plt.ylabel('Frequenza', fontsize=12)
            plt.legend(loc='upper right')
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.show()

            plt.figure(figsize=(8, 6))
            sns.countplot(x='Sex', data=df, palette='pastel')
            plt.title('Distribuzione Sesso', fontsize=16)
            plt.xlabel('Sesso', fontsize=12)
            plt.ylabel('Conteggio', fontsize=12)
            plt.legend(['Maschio e Femmina'], loc='upper right')
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.show()

            plt.figure(figsize=(8, 6))
            sns.countplot(x='Embarked', data=df, palette='muted')
            plt.title('Distribuzione Porto di Imbarco', fontsize=16)
            plt.xlabel('Porto di Imbarco', fontsize=12)
            plt.ylabel('Conteggio', fontsize=12)
            plt.legend(['C = Cherbourg, Q = Queenstown, S = Southampton'], loc='upper right')
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.show()
        elif scelta == "5":
            # Analisi delle relazioni tra colonne e target
            separatore("Relazioni tra colonna e target")
            print("Distribuzione sopravvissuti per sesso:\n", df.groupby('Sex')['Survived'].mean())
            print("\nDistribuzione sopravvissuti per classe:\n", df.groupby('Pclass')['Survived'].mean())
            print("\nDistribuzione sopravvissuti per porto di imbarco:\n", df.groupby('Embarked')['Survived'].mean())
            print("\nCorrelazione tra Fare e Survived:\n", df[['Fare', 'Survived']].corr())
            df['IsChild'] = df['Age'] < 13
            print("\nDistribuzione sopravvissuti per bambini:\n", df.groupby('IsChild')['Survived'].mean())
            print("\nDistribuzione sopravvissuti per età:\n", df.groupby('Age')['Survived'].mean())
        elif scelta == "6":
            # Creazione di nuove feature
            separatore("6. Creazione Nuove Feature")
            df['AgeGroup'] = pd.cut(df['Age'], bins=range(0, int(df['Age'].max()) + 5, 5), right=False)

            plt.figure(figsize=(12, 6))
            sns.barplot(x='AgeGroup', y='Survived', data=df, ci=None, palette='coolwarm')
            plt.title('Distribuzione Sopravvissuti per Gruppi di Età', fontsize=16)
            plt.xlabel('Gruppo di Età', fontsize=12)
            plt.ylabel('Percentuale Sopravvissuti', fontsize=12)
            plt.xticks(rotation=45)
            plt.legend(['Percentuale Sopravvissuti'], loc='upper right')
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.show()

            df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
            print("\nSopravvivenza per FamilySize:\n", df.groupby('FamilySize')['Survived'].mean())

            df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
            print("Sopravvivenza se da solo:\n", df.groupby('IsAlone')['Survived'].mean())
        elif scelta == "7":
            # Preparazione del dataset per il modello
            separatore("7. Preparazione per Modello")
            df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)
            scaler = StandardScaler()
            df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])

            columns_to_keep = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'FamilySize', 'IsAlone'] + \
                              [col for col in df.columns if col.startswith('Sex_') or col.startswith('Embarked_')]
            final_df = df[columns_to_keep]
            final_df = rimuovi_multicollinearita(final_df)

            print("\nColonne usate:\n", final_df.columns.tolist())
        elif scelta == "8":
            # Creazione e valutazione del modello predittivo
            separatore("9. Modello Predittivo")
            X = final_df
            y = df['Survived']
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            decision_tree = DecisionTreeClassifier(random_state=42)
            decision_tree.fit(X_train, y_train)

            pred = decision_tree.predict(X_test)

            plt.figure(figsize=(20, 10))
            sns.heatmap(confusion_matrix(y_test, pred), annot=True, fmt='d', cmap='Blues', xticklabels=['Not Survived', 'Survived'], yticklabels=['Not Survived', 'Survived'])
            plt.xlabel('Predicted')
            plt.title("Decision Tree Confusion Matrix")
            plt.ylabel('True')
            plt.legend(['Not Survived', 'Survived'], loc='upper right')
            plt.show()

            print(confusion_matrix(y_test, pred))
            print(classification_report(y_test, pred))
        elif scelta == "9":
            # Ottimizzazione del modello predittivo
            separatore("9.1 Modello Predittivo Ottimizzato")
            param_grid = {
                'criterion': ['gini', 'entropy'],
                'max_depth': [None, 5, 10, 15, 20],
                'min_samples_split': [2, 5, 10],
                'min_samples_leaf': [1, 2, 4]
            }

            grid_search = GridSearchCV(DecisionTreeClassifier(random_state=42), param_grid, cv=5, scoring='accuracy')
            grid_search.fit(X_train, y_train)

            best_params = grid_search.best_params_
            print("Migliori parametri trovati:", best_params)

            optimized_tree = DecisionTreeClassifier(**best_params, random_state=42)
            optimized_tree.fit(X_train, y_train)

            optimized_pred = optimized_tree.predict(X_test)

            plt.figure(figsize=(20, 10))
            sns.heatmap(confusion_matrix(y_test, optimized_pred), annot=True, fmt='d', cmap='Greens', xticklabels=['Not Survived', 'Survived'], yticklabels=['Not Survived', 'Survived'])
            plt.xlabel('Predicted')
            plt.title("Optimized Decision Tree Confusion Matrix")
            plt.ylabel('True')
            plt.legend(['Not Survived', 'Survived'], loc='upper right')
            plt.show()

            print(confusion_matrix(y_test, optimized_pred))
            print(classification_report(y_test, optimized_pred))
        elif scelta == "10":
            # Regressione lineare
            separatore("10. Regressione Lineare")
            try:
                X = final_df
                y = df['Survived']
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

                # Modello di regressione lineare
                regression_model = LogisticRegression()  # Puoi usare anche LinearRegression per regressione continua
                regression_model.fit(X_train, y_train)

                y_pred = regression_model.predict(X_test)

                # Calcolo delle metriche
                accuracy = accuracy_score(y_test, y_pred)
                print(f"Accuratezza del modello di regressione: {accuracy:.2f}")

                # R² è significativo solo per regressione continua
                y_pred_proba = regression_model.predict_proba(X_test)[:, 1]  # Probabilità per la classe positiva
                r2 = r2_score(y_test, y_pred_proba)
                print(f"R quadro del modello di regressione: {r2:.2f}")
            except NameError:
                print("Il dataset o il modello non sono stati preparati. Seleziona prima l'opzione 7 o 9.")
        elif scelta == "11":
            grafico_boxplot_modello(final_df)
        elif scelta == "0":
            # Uscita dal programma
            print("Uscita dal programma.")
            break
        else:
            # Gestione input non valido
            print("Scelta non valida. Riprova.")

# Punto di ingresso del programma
if __name__ == "__main__":
    menu()