import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix
import os

# Caricamento del dataset Titanic
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'titanic.csv')
titanic = pd.read_csv(file_path)
df = titanic.copy()

# Funzione per stampare separatori di sezione
def separatore(title):
    print(f"\n{'='*10} {title} {'='*10}\n") 

# Analisi della struttura del dataset
separatore("Struttura del dataset")
# Stampa delle colonne, tipi di dati e dimensioni del dataset
print("Colonne del dataset:", df.columns.tolist())
print("Tipi di dati delle colonne:\n", df.dtypes)
print("Dimensioni del dataset:", df.shape)

# Pulizia del dataset
separatore("Pulizia del dati")
# Calcolo delle percentuali di valori mancanti e gestione dei NaN
percentuali_mancanti = df.isnull().mean() * 100
print("Percentuali di dati mancanti:\n", percentuali_mancanti[percentuali_mancanti > 0])

df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop(columns=['Cabin', 'Ticket', 'Name', 'PassengerId'], inplace=True) # Rimuovo le colonne Cabin, Ticket, Name e PassengerId
df.dropna(inplace=True) # Rimuovo le righe con valori NaN

# Salvataggio del dataset pulito
clean_path = os.path.join(current_dir, 'titanic_clean.csv')
df.to_csv(clean_path, index=False)
print(f"Dataset pulito salvato in: {clean_path}")

# Analisi delle singole colonne
separatore("Analisi delle singole colonne")
# Analisi statistica e distribuzione delle colonne principali
print("Distribuzione età:\n", df['Age'].describe())
print("\nDistribuzione prezzo biglietto:\n", df['Fare'].describe())
print("\nValori Unici - sesso:\n", df['Sex'].unique())
print("\nDistribuzione sesso:\n", df['Sex'].value_counts()*100)
print("Valori Unici - porto di imbarco:\n", df['Embarked'].unique())
print("Valori Unici - classe:\n", df['Pclass'].unique())

# Creazione di grafici per visualizzare le distribuzioni
separatore("Grafici")
# Grafico distribuzione età
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], kde=True, color='blue', bins=30, label='Distribuzione Età')
plt.title('Distribuzione Età', fontsize=16)
plt.xlabel('Età', fontsize=12)
plt.ylabel('Frequenza', fontsize=12)
plt.legend(loc='upper right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Grafico distribuzione prezzo biglietto
plt.figure(figsize=(10, 6))
sns.histplot(df['Fare'], kde=True, color='green', bins=30, label='Distribuzione Prezzo Biglietto')
plt.title('Distribuzione Prezzo Biglietto', fontsize=16)
plt.xlabel('Prezzo Biglietto', fontsize=12)
plt.ylabel('Frequenza', fontsize=12)
plt.legend(loc='upper right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Grafico distribuzione sesso
plt.figure(figsize=(8, 6))
sns.countplot(x='Sex', data=df, palette='pastel')
plt.title('Distribuzione Sesso', fontsize=16)
plt.xlabel('Sesso', fontsize=12)
plt.ylabel('Conteggio', fontsize=12)
plt.legend(['Maschio e Femmina'], loc='upper right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Grafico distribuzione porto di imbarco
plt.figure(figsize=(8, 6))
sns.countplot(x='Embarked', data=df, palette='muted')
plt.title('Distribuzione Porto di Imbarco', fontsize=16)
plt.xlabel('Porto di Imbarco', fontsize=12)
plt.ylabel('Conteggio', fontsize=12)
plt.legend(['C = Cherbourg, Q = Queenstown, S = Southampton'], loc='upper right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Analisi delle relazioni tra colonne e target
separatore("Relazioni tra colonna e target")
# Analisi delle sopravvivenze in base a sesso, classe, porto di imbarco, ecc.
print("Distribuzione sopravvissuti per sesso:\n", df.groupby('Sex')['Survived'].mean())
print("\nDistribuzione sopravvissuti per classe:\n", df.groupby('Pclass')['Survived'].mean())
print("\nDistribuzione sopravvissuti per porto di imbarco:\n", df.groupby('Embarked')['Survived'].mean())
print("\nCorrelazione tra Fare e Survived:\n", df[['Fare', 'Survived']].corr())
df['IsChild'] = df['Age'] < 13
print("\nDistribuzione sopravvissuti per bambini:\n", df.groupby('IsChild')['Survived'].mean())
print("\nDistribuzione sopravvissuti per età:\n", df.groupby('Age')['Survived'].mean())

# Creazione di nuove feature
separatore("6. Creazione Nuove Feature")
# Creazione di colonne come 'IsChild', 'AgeGroup', 'FamilySize', 'IsAlone'
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

plt.figure(figsize=(8, 6))
sns.barplot(x='Pclass', y='Survived', data=df, ci=None, palette='viridis')
plt.title('Distribuzione Sopravvissuti per Classe', fontsize=16)
plt.xlabel('Classe', fontsize=12)
plt.ylabel('Percentuale Sopravvissuti', fontsize=12)
plt.legend(['1 = Prima Classe, 2 = Seconda Classe, 3 = Terza Classe'], loc='upper right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

plt.figure(figsize=(8, 6))
sns.barplot(x='Sex', y='Survived', data=df, ci=None, palette='pastel')
plt.title('Distribuzione Sopravvissuti per Sesso', fontsize=16)
plt.xlabel('Sesso', fontsize=12)
plt.ylabel('Percentuale Sopravvissuti', fontsize=12)
plt.legend(['Maschio e Femmina'], loc='upper right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

plt.figure(figsize=(8, 6))
sns.barplot(x='Embarked', y='Survived', data=df, ci=None, palette='muted')
plt.title('Distribuzione Sopravvissuti per Porto di Imbarco', fontsize=16)
plt.xlabel('Porto di Imbarco', fontsize=12)
plt.ylabel('Percentuale Sopravvissuti', fontsize=12)
plt.legend(['C = Cherbourg, Q = Queenstown, S = Southampton'], loc='upper right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

plt.figure(figsize=(8, 6))
sns.barplot(x='IsChild', y='Survived', data=df, ci=None, palette='coolwarm')
plt.title('Distribuzione Sopravvissuti per Bambini', fontsize=16)
plt.xlabel('Bambino (True/False)', fontsize=12)
plt.ylabel('Percentuale Sopravvissuti', fontsize=12)
plt.legend(['True = Bambino, False = Adulto'], loc='upper right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
print("\nSopravvivenza per FamilySize:\n", df.groupby('FamilySize')['Survived'].mean())

plt.figure(figsize=(10, 6))
sns.barplot(x='FamilySize', y='Survived', data=df, palette='viridis')
plt.title('Sopravvivenza per Dimensione Famiglia', fontsize=16)
plt.xlabel('Dimensione Famiglia', fontsize=12)
plt.ylabel('Percentuale Sopravvissuti', fontsize=12)
plt.legend(['Percentuale Sopravvissuti'], loc='upper right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
print("Sopravvivenza se da solo:\n", df.groupby('IsAlone')['Survived'].mean())
print(df.head())

plt.figure(figsize=(8, 6))
sns.barplot(x='IsAlone', y='Survived', data=df, palette='coolwarm')
plt.title('Sopravvivenza per Chi è da Solo', fontsize=16)
plt.xlabel('Da Solo (1 = Sì, 0 = No)', fontsize=12)
plt.ylabel('Percentuale Sopravvissuti', fontsize=12)
plt.legend(['1 = Da Solo, 0 = Non da Solo'], loc='upper right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Preparazione del dataset per il modello
separatore("7. Preparazione per Modello")
# Codifica delle variabili categoriche e normalizzazione delle colonne numeriche
df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)
scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])

columns_to_keep = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'FamilySize', 'IsAlone'] + \
                  [col for col in df.columns if col.startswith('Sex_') or col.startswith('Embarked_')]
final_df = df[columns_to_keep]

print("\nColonne usate:\n", final_df.columns.tolist())

# Creazione e valutazione del modello predittivo
separatore("9. Modello Predittivo")
# Addestramento di un Decision Tree e valutazione delle performance
X = final_df
y = df['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

decision_tree = DecisionTreeClassifier(random_state=42)
decision_tree.fit(X_train, y_train)

# Predizioni
pred = decision_tree.predict(X_test)

# Visualizzazione della matrice di confusione e valutazione del modello
plt.figure(figsize=(20, 10))
sns.heatmap(confusion_matrix(y_test, pred), annot=True, fmt='d', cmap='Blues', xticklabels=['Not Survived', 'Survived'], yticklabels=['Not Survived', 'Survived'])
plt.xlabel('Predicted')
plt.title("Decision Tree Confusion Matrix")
plt.ylabel('True')
plt.legend(['Not Survived', 'Survived'], loc='upper right')
plt.show()

print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))

# Ottimizzazione dei parametri del Decision Tree
separatore("9.1 Modello Predittivo Ottimizzato")
param_grid = {
    'criterion': ['gini', 'entropy'],
    'max_depth': [None, 5, 10, 15, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

grid_search = GridSearchCV(DecisionTreeClassifier(random_state=42), param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Migliori parametri trovati
best_params = grid_search.best_params_
print("Migliori parametri trovati:", best_params)

# Addestramento del modello con i migliori parametri
optimized_tree = DecisionTreeClassifier(**best_params, random_state=42)
optimized_tree.fit(X_train, y_train)

# Predizioni con il modello ottimizzato
optimized_pred = optimized_tree.predict(X_test)

# Visualizzazione della matrice di confusione e valutazione del modello ottimizzato
plt.figure(figsize=(20, 10))
sns.heatmap(confusion_matrix(y_test, optimized_pred), annot=True, fmt='d', cmap='Greens', xticklabels=['Not Survived', 'Survived'], yticklabels=['Not Survived', 'Survived'])
plt.xlabel('Predicted')
plt.title("Optimized Decision Tree Confusion Matrix")
plt.ylabel('True')
plt.legend(['Not Survived', 'Survived'], loc='upper right')
plt.show()

print(confusion_matrix(y_test, optimized_pred))
print(classification_report(y_test, optimized_pred))