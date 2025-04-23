import pandas as pd
import numpy as np
import os  # Per la gestione dei percorsi

# Classe per l'analisi dei clienti di una compagnia di telecomunicazioni
class AnalisiClienti:
    def __init__(self, file_path):
        # Salva il percorso del file originale
        self.file_path = file_path
        # Carica i dati da un file CSV
        self.df = pd.read_csv(file_path)
    
    def esplora_dati(self):
        # Mostra informazioni generali sul dataset
        print("Info Generali:")
        print(self.df.info())
        # Mostra statistiche descrittive delle colonne numeriche
        print("\nStatistiche Descrittive:")
        print(self.df.describe())
        # Mostra la distribuzione dei clienti che hanno abbandonato (Churn)
        print("\nDistribuzione Churn:")
        print(self.df['Churn'].value_counts())
        # Verifica la presenza di valori nulli
        print("\nValori Mancanti:")
        print(self.df.isnull().sum())
        
    def pulisci_dati(self):
        print("Pulizia dei dati...")
        inizio_righe = len(self.df)
        # Rimuove righe con valori nulli
        self.df.dropna(inplace=True)
        # Rimuove righe duplicate
        self.df.drop_duplicates(inplace=True)
        # Mantiene solo righe con età maggiore di 0
        self.df = self.df[self.df['Età'] > 18]
        # Mantiene solo righe con tariffa mensile maggiore di 0
        self.df = self.df[self.df['Tariffa_Mensile'] > 10]
        # Mantiene solo righe con dati consumati maggiori di 0
        self.df = self.df[self.df['Dati_Consumati'] > 0]
        fine_righe = len(self.df)
        print(f"Righe iniziali: {inizio_righe}, Righe finali: {fine_righe}")
        print("Dati puliti.")
    
    def analisi_esplorativa(self):
        print("Analisi esplorativa...")
        # Creazione di una nuova colonna per il costo per GB
        self.df['Costo_Gb'] = self.df['Tariffa_Mensile'] / self.df['Dati_Consumati']
        
        # Analisi delle relazioni tra variabili raggruppate per churn
        print(self.df.groupby('Churn')[['Età', 'Durata_Abbonamento', 'Tariffa_Mensile', 'Dati_Consumati']].mean())
        
        # Calcolo della correlazione tra variabili numeriche
        print("\nCorrelazione tra variabili numeriche:")
        print(self.df.select_dtypes(include=[np.number]).corr()) # Correlazione tra variabili numeriche escludendo 'Churn' perché non è numerica
    
    def preparazione_dati(self):
        print("Preparazione dei dati...")
        
        # Pulizia e mappatura robusta della colonna 'Churn'
        self.df['Churn'] = self.df['Churn'].astype(str).str.strip().str.lower()
        self.df['Churn'] = self.df['Churn'].map({'sì': 1, 'si': 1, 'no': 0})
    
        # Rimuove righe con valori non validi o conversione fallita
        self.df = self.df[self.df['Churn'].notna()]
        
        # Normalizzazione delle colonne numeriche
        numeriche = ['Età', 'Durata_Abbonamento', 'Tariffa_Mensile', 'Dati_Consumati', 'Costo_Gb']
        for col in numeriche:
            media = self.df[col].mean()
            dev_std = self.df[col].std()
            # Applica la normalizzazione z-score
            self.df[col] = (self.df[col] - media) / dev_std
        
        print("Dati preparati per l'analisi.")
    
    def salva_csv(self, nuovo_nome_file):
        # Ottieni la cartella del file originale
        cartella = os.path.dirname(self.file_path)
        # Crea il percorso completo per il nuovo file
        nuovo_percorso = os.path.join(cartella, nuovo_nome_file)
        # Salva il DataFrame nel nuovo percorso
        self.df.to_csv(nuovo_percorso, index=False)
        print(f"Dati salvati in '{nuovo_percorso}'.")


# Funzione principale con menu interattivo
def main():
    # Percorso del file CSV
    file_path = 'Mercoledi 23 Aprile/eser_pandas2/clienti_telecom.csv'
    # Creazione dell'oggetto AnalisiClienti
    analisi = AnalisiClienti(file_path)
    
    while True:
        # Menu delle opzioni
        print("\nMenu:")
        print("1. Esplora Dati")
        print("2. Pulisci Dati")
        print("3. Analisi Esplorativa")
        print("4. Preparazione Dati")
        print("5. Salva dati su nuovo CSV")
        print("6. Uscita")
        
        # Input dell'utente
        scelta = input("Scegli un'opzione: ")
        
        # Gestione delle opzioni con match-case
        match scelta:
            case '1':
                analisi.esplora_dati()
            case '2':
                analisi.pulisci_dati()
            case '3':
                analisi.analisi_esplorativa()
            case '4':
                analisi.preparazione_dati()
            case '5':
                nuovo_file = input("Inserisci il nome del nuovo file (es. clienti_telecom_pulito.csv): ")
                analisi.salva_csv(nuovo_file)
            case '6':
                print("Uscita dal programma.")
                break
                
            case _:
                print("Opzione non valida. Riprova.")

# Avvio del programma
if __name__ == "__main__":
    main()
