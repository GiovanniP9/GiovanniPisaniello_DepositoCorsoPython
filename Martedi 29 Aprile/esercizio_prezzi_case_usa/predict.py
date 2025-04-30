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
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.linear_model import Ridge, Lasso


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
        self.X_scaled = None  # Per memorizzare le X standardizzate
        
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
        
        # Standardizza i dati prima dell'analisi VIF
        # Utilizziamo lo scaler della classe
        X_scaled = pd.DataFrame(
            self.scaler.fit_transform(X), 
            columns=X.columns
        )
        
        # Salviamo le X standardizzate per usarle dopo
        self.X_scaled = X_scaled
        
        print("Dati standardizzati per l'analisi VIF")
        
        # Train-test split iniziale con dati standardizzati
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.2, random_state=42
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
            X_vif = X_scaled[self.features].copy()
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
        
        # Manteniamo le feature selezionate, ma continuiamo a lavorare con i dati standardizzati
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
        
        # Ottimizza le feature usando il VIF
        self.optimize_features_vif()
                
        # A questo punto abbiamo i dati standardizzati in self.X_scaled e le feature selezionate in self.features
        X = self.X_scaled[self.features]  # Utilizziamo le X già standardizzate 
        y = self.df['price']
        
        # Train-test split con i dati standardizzati
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        print(f"Dati preparati: X_train shape {self.X_train.shape}")
        print(f"Dati standardizzati correttamente")
        
        # DEBUG: Verifica standardizzazione
        debug_train_mean = self.X_train.mean()
        debug_train_std = self.X_train.std()

        print("\nControllo standardizzazione X_train (media ~0, std ~1):")
        print(pd.DataFrame({
                "media": debug_train_mean.round(4),
                "std": debug_train_std.round(4)
            }))

    
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

        # Normalizzazione RMSE e MAE
        y_range = self.y_test.max() - self.y_test.min()
        rmse_normalized = rmse / y_range
        mae_normalized = mae / y_range

        print("\nValutazione del modello:")
        print(f"R² Score: {r2:.4f}")
        print(f"RMSE Normalizzato: {rmse_normalized:.4f}")
        print(f"MAE Normalizzato: {mae_normalized:.4f}")

        return r2, rmse_normalized, mae_normalized
    
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
        
    def elimina_variabili_vif_pvalue(X_train, y_train, vif_threshold=10.0, pvalue_threshold=0.05):
        """
        Rimuove variabili da X_train basandosi su VIF e p-value.
    
        - Elimina solo variabili con VIF > soglia e p-value > soglia.
        - Ricalcola VIF e p-value dopo ogni eliminazione.
        """
    
        # Copia dei dati per lavorare in sicurezza
        X_current = X_train.copy()
    
        # Aggiungi costante per statsmodels
        X_const = sm.add_constant(X_current)
    
        while True:
            # Modello OLS per calcolare p-value
            model = sm.OLS(y_train, X_const).fit()
            pvalues = model.pvalues.drop('const')  # escludi l'intercetta
        
            # Calcolo VIF
            vif = pd.DataFrame()
            vif["Feature"] = X_current.columns
            vif["VIF"] = [variance_inflation_factor(X_current.values, i) for i in range(X_current.shape[1])]
        
            # Unisco p-value e VIF
            stats = vif.copy()
            stats["p-value"] = pvalues.values
        
            # Trova candidati da eliminare: VIF alto + p-value alto
            candidates = stats[(stats["VIF"] > vif_threshold) & (stats["p-value"] > pvalue_threshold)]
        
            if candidates.empty:
                print("\nNessuna variabile da eliminare. Selezione completata.")
                break
        
            # Elimina la variabile con il VIF più alto tra i candidati
            worst_feature = candidates.sort_values(by="VIF", ascending=False)["Feature"].iloc[0]
            print(f"Rimuovo '{worst_feature}' con VIF = {candidates.loc[candidates['Feature'] == worst_feature, 'VIF'].values[0]:.2f} "
                  f"e p-value = {candidates.loc[candidates['Feature'] == worst_feature, 'p-value'].values[0]:.4f}")
            
            #Aggiorna i dati
            X_current = X_current.drop(columns=[worst_feature])
            X_const = sm.add_constant(X_current)
    
        return X_current 
    def train_ridge(self, alpha=1.0):
        """Addestra un modello Ridge"""
        model = Ridge(alpha=alpha)
        model.fit(self.X_train, self.y_train)
        y_pred = model.predict(self.X_test)

        # Calcola le metriche
        r2 = r2_score(self.y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(self.y_test, y_pred))
        mae = mean_absolute_error(self.y_test, y_pred)

        # Normalizzazione RMSE e MAE
        y_range = self.y_test.max() - self.y_test.min()
        rmse_normalized = rmse / y_range
        mae_normalized = mae / y_range

        print("\n[Ridge Regression]")
        print(f"R² Score: {r2:.4f}")
        print(f"RMSE Normalizzato: {rmse_normalized:.4f}")
        print(f"MAE Normalizzato: {mae_normalized:.4f}")

        return model

    def train_lasso(self, alpha=0.1):
        """Addestra un modello Lasso"""
        model = Lasso(alpha=alpha, max_iter=10000)
        model.fit(self.X_train, self.y_train)
        y_pred = model.predict(self.X_test)

        # Calcola le metriche
        r2 = r2_score(self.y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(self.y_test, y_pred))
        mae = mean_absolute_error(self.y_test, y_pred)

        # Normalizzazione RMSE e MAE
        y_range = self.y_test.max() - self.y_test.min()
        rmse_normalized = rmse / y_range
        mae_normalized = mae / y_range

        print("\n[Lasso Regression]")
        print(f"R² Score: {r2:.4f}")
        print(f"RMSE Normalizzato: {rmse_normalized:.4f}")
        print(f"MAE Normalizzato: {mae_normalized:.4f}")

        return model

    def _print_metrics(self, y_pred):
        """Stampa le metriche di valutazione"""
        r2 = r2_score(self.y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(self.y_test, y_pred))
        mae = mean_absolute_error(self.y_test, y_pred)
    
        print(f"R² Score: {r2:.4f}")
        print(f"RMSE: ${rmse:.2f}")
        print(f"MAE: ${mae:.2f}")

    
    def run(self, visualize=True):
        """
        Esegue l'intero workflow predittivo
        
        Args:
            visualize (bool): Se True, visualizza i grafici dei risultati
            
        Returns:
            dict: Risultati del modello e metriche di valutazione
        """
        import time
        
        # Dizionario per memorizzare timing e risultati
        results = {
            "timing": {},
            "metrics": {},
            "features": []
        }
        
        try:
            # Fase 1: Caricamento dati
            start_time = time.time()
            self.load_cleaned_data()
            results["timing"]["load_data"] = time.time() - start_time
            print(f"✓ Caricamento dati completato in {results['timing']['load_data']:.2f} secondi")
            
            # Fase 2: Preparazione dati
            start_time = time.time()
            self.prepare_data()
            results["timing"]["prepare_data"] = time.time() - start_time
            results["features"] = self.features if self.features else []
            print(f"✓ Preparazione dati completata in {results['timing']['prepare_data']:.2f} secondi")
            
            # Fase 3: Training del modello
            start_time = time.time()
            self.train_model()
            results["timing"]["train_model"] = time.time() - start_time
            print(f"✓ Training del modello completato in {results['timing']['train_model']:.2f} secondi")
            
            # Fase 4: Valutazione del modello
            start_time = time.time()
            r2, rmse, mae = self.evaluate_model()
            results["timing"]["evaluate_model"] = time.time() - start_time
            results["metrics"] = {
                "r2": r2,
                "rmse": rmse,
                "mae": mae
            }
            print(f"✓ Valutazione del modello completata in {results['timing']['evaluate_model']:.2f} secondi")
            
            # Fase 5: Visualizzazione dei risultati (opzionale)
            if visualize:
                start_time = time.time()
                self.visualize_results()
                results["timing"]["visualize"] = time.time() - start_time
                print(f"✓ Visualizzazione completata in {results['timing']['visualize']:.2f} secondi")
            
            # Calcola il tempo totale
            results["timing"]["total"] = sum(results["timing"].values())
            print(f"\nPipeline completata in {results['timing']['total']:.2f} secondi")
            
            # Riepilogo finale
            print("\n" + "=" * 50)
            print("RIEPILOGO")
            print("=" * 50)
            print(f"Feature utilizzate ({len(results['features'])}): {', '.join(results['features']) if results['features'] else 'Tutte'}")
            print(f"Performance: R² = {r2:.4f}, RMSE = ${rmse:.2f}, MAE = ${mae:.2f}")
            print(HousePricePredictor.elimina_variabili_vif_pvalue(self.X_train, self.y_train))
            
            # Fase 6: Ridge e Lasso (opzionale)
            print("\n" + "=" * 50)
            print("CONFRONTO MODELLI: Ridge e Lasso")
            print("=" * 50)

            self.train_ridge(alpha=1.0)
            self.train_lasso(alpha=0.1)
            
            HousePricePredictor._print_metrics(self.y_pred)

            
            return results
            
        except Exception as e:
            print(f"\nErrore durante l'esecuzione: {str(e)}")
            import traceback
            traceback.print_exc()
            return None


if __name__ == "__main__":
    BASE_DIR = 'Martedi 29 Aprile/esercizio_prezzi_case_usa'
    predictor = HousePricePredictor(
        base_dir=BASE_DIR,
        input_file='kc_house_data_cleaned.csv'
    )
    predictor.run()