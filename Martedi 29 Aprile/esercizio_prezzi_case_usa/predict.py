import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
# Importazioni aggiuntive per il calcolo VIF
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant

class HousePricePredictor:
    def __init__(self, base_dir: str, input_file: str):
        self.base_dir = base_dir
        self.input_file = input_file
        self.df = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.model = None
        self.y_pred = None
        self.scaler = StandardScaler()
        self.features = None  # Per tenere traccia delle feature selezionate
        
    def load_cleaned_data(self):
        """Carica i dati già puliti dal file CSV"""
        input_path = os.path.join(self.base_dir, self.input_file)
        
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Il file di dati puliti non esiste: {input_path}")
            
        # Carica direttamente il file pulito
        self.df = pd.read_csv(input_path)
        print(f"Dati puliti caricati: {self.df.shape} righe e colonne")
    
    def optimize_features_vif(self):
        """Elimina ricorsivamente le colonne con VIF più alto se ciò migliora l'R²"""
        print("\n" + "=" * 50)
        print("OTTIMIZZAZIONE FEATURES CON VIF")
        print("=" * 50)
        
        # Separazione del dataset
        X = self.df.drop('price', axis=1)
        y = self.df['price']
        self.features = list(X.columns)
        
        # Train-test split iniziale
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Modello e R² iniziale
        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        best_r2 = r2_score(y_test, y_pred)
        
        print(f"R² iniziale: {best_r2:.6f} con {len(self.features)} features")
        
        improvement = True
        removed_features = []
        
        while improvement and len(self.features) > 1:
            improvement = False
            
            # Calcola VIF per tutte le features rimanenti
            X_vif = X[self.features].copy()
            vif_data = pd.DataFrame()
            vif_data["Feature"] = self.features
            vif_data["VIF"] = [variance_inflation_factor(X_vif.values, i) for i in range(len(self.features))]
            
            # Ordina per VIF decrescente
            vif_data = vif_data.sort_values("VIF", ascending=False)
            
            print(f"\nVIF delle feature:")
            print(vif_data)
            
            # Prova a rimuovere la feature con VIF più alto
            feature_to_remove = vif_data["Feature"].iloc[0]
            temp_features = [f for f in self.features if f != feature_to_remove]
            
            # Valuta il modello senza questa feature
            X_train_reduced = X_train[temp_features]
            X_test_reduced = X_test[temp_features]
            
            model = LinearRegression()
            model.fit(X_train_reduced, y_train)
            y_pred = model.predict(X_test_reduced)
            new_r2 = r2_score(y_test, y_pred)
            
            print(f"Tentativo rimozione '{feature_to_remove}' (VIF: {vif_data['VIF'].iloc[0]:.2f})")
            print(f"Nuovo R²: {new_r2:.6f}, Differenza: {new_r2 - best_r2:.6f}")
            
            # Se l'R² è migliorato, rimuovi definitivamente la feature
            if new_r2 > best_r2:
                self.features = temp_features
                best_r2 = new_r2
                improvement = True
                removed_features.append(feature_to_remove)
                print(f"✓ Feature '{feature_to_remove}' rimossa (miglioramento R²)")
            else:
                print(f"✗ Feature '{feature_to_remove}' mantenuta (nessun miglioramento)")
        
        print("\n" + "-" * 50)
        print(f"Ottimizzazione completata!")
        print(f"R² finale: {best_r2:.6f}")
        print(f"Feature rimosse: {removed_features}")
        print(f"Feature mantenute: {self.features}")
        
        # Aggiorna il dataset con le feature selezionate
        self.df = pd.concat([self.df[self.features], y], axis=1)
        
        return best_r2
        
    def prepare_data(self):
        """Prepara i dati per il modello"""
        
        # Converti la colonna date in datetime
        if 'date' in self.df.columns:
            self.df['date'] = pd.to_datetime(self.df['date'])
            
            # Estrai caratteristiche utili dalla data
            self.df['year'] = self.df['date'].dt.year
            self.df['month'] = self.df['date'].dt.month
            
            # Rimuovi la colonna date originale
            self.df.drop('date', axis=1, inplace=True)
        
        # Verifica altre colonne non numeriche da rimuovere
        object_columns = self.df.select_dtypes(include=['object']).columns
        if not object_columns.empty:
            print(f"Rimozione colonne non numeriche: {list(object_columns)}")
            self.df.drop(columns=object_columns, inplace=True)
        
        # Ottimizza le feature usando il VIF
        self.optimize_features_vif()
                
        # Dividi in features e target
        X = self.df.drop('price', axis=1)
        y = self.df['price']
        
        # Train-test split
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Standardizza le feature
        self.X_train = self.scaler.fit_transform(self.X_train)
        self.X_test = self.scaler.transform(self.X_test)
        
        print(f"Dati preparati: X_train shape {self.X_train.shape}")
    
    def train_model(self):
        """Addestra un modello di regressione lineare"""
        self.model = LinearRegression()
        self.model.fit(self.X_train, self.y_train)
        
        # Coefficienti del modello
        if self.features is None:
            feature_names = self.df.drop('price', axis=1).columns
        else:
            feature_names = self.features
            
        coefficients = pd.DataFrame(
            self.model.coef_, 
            index=feature_names, 
            columns=['Coefficient']
        )
        print("\nCoefficienti del modello:")
        print(coefficients.sort_values('Coefficient', ascending=False))
        
    def evaluate_model(self):
        """Valuta le prestazioni del modello"""
        self.y_pred = self.model.predict(self.X_test)
        
        # Calcola le metriche
        r2 = r2_score(self.y_test, self.y_pred)
        rmse = np.sqrt(mean_squared_error(self.y_test, self.y_pred))
        mae = mean_absolute_error(self.y_test, self.y_pred)
        
        print("\nValutazione del modello:")
        print(f"R² Score: {r2:.4f}")
        print(f"RMSE: ${rmse:.2f}")
        print(f"MAE: ${mae:.2f}")
        
        return r2, rmse, mae
    
    def visualize_results(self):
        """Visualizza i risultati della previsione"""
        plt.figure(figsize=(10, 6))
        plt.scatter(self.y_test, self.y_pred, alpha=0.5)
        
        # Linea ideale (y=x)
        min_val = min(self.y_test.min(), self.y_pred.min())
        max_val = max(self.y_test.max(), self.y_pred.max())
        plt.plot([min_val, max_val], [min_val, max_val], 'r--')
        
        plt.title('Regressione Lineare: Valori Reali vs Previsti')
        plt.xlabel('Prezzo Reale ($)')
        plt.ylabel('Prezzo Previsto ($)')
        plt.tight_layout()
        # Mostra la figura
        plt.show()
    
    def run(self):
        """Esegue l'intero workflow predittivo"""
        self.load_cleaned_data()
        self.prepare_data()
        self.train_model()
        self.evaluate_model()
        self.visualize_results()
        self.optimize_features_vif()


if __name__ == "__main__":
    BASE_DIR = 'Martedi 29 Aprile/esercizio_prezzi_case_usa'
    predictor = HousePricePredictor(
        base_dir=BASE_DIR,
        input_file='kc_house_data_cleaned.csv'
    )
    predictor.run()