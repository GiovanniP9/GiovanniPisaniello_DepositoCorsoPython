import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class AnalisiTemperature:
    def __init__(self):
        self.df = None
    
    def genera_dati(self,):# Genera dati casuali per le temperature
        giorni = pd.date_range(start='2025-01-01', periods=30, freq='D')
        citta = ['Roma', 'Milano', 'Napoli']
        
        dati = []
        for g in giorni:
            for c in citta:
                temp = np.random.randint(-5, 41)  # Genera una temperatura casuale tra -5 e 40
                dati.append({'Giorno': g, 'Città': c, 'Temperatura': temp})
        self.df = pd.DataFrame(dati)
        print("Dati generati:")
    
    def calcola_statistiche(self):# Calcola le statistiche per ogni città
        if self.df is None:
            print("Nessun dato disponibile. Genera i dati prima di calcolare le statistiche.")
            return
        print("Statistiche città:")
        stats = self.df.groupby('Città')['Temperatura'].agg(['mean', 'median', 'min', 'max'])
        print(stats.rename(columns={'mean': 'Media', 'median': 'Mediana', 'min': 'Minimo', 'max': 'Massimo'}))
    
    def visualizza_grafico_citta(self, citta=None):
        if self.df is None:
            print("Nessun dato disponibile. Genera i dati prima di visualizzare il grafico.")
            return
        if citta is None:
            plt.figure(figsize=(10, 6))
            for c in self.df['Città'].unique(): # Itera su ogni città unica
                dati_citta = self.df[self.df['Città'] == c] # Filtra i dati per la città corrente
                plt.plot(dati_citta['Giorno'], dati_citta['Temperatura'], label=c) # Crea una linea per ogni città
            plt.title('Temperature giornaliere per città')
            plt.xlabel('Giorno')
            plt.ylabel('Temperatura (°C)')
            plt.legend()
            plt.show()
        else: # Se è specificata una città, visualizza solo i dati per quella città
            dati_citta = self.df[self.df['Città'] == citta]
            plt.figure(figsize=(10, 6))
            plt.plot(dati_citta['Giorno'], dati_citta['Temperatura'], label=citta, color='blue')
            plt.title(f'Temperature giornaliere per {citta}')
            plt.xlabel('Giorno')
            plt.ylabel('Temperatura (°C)')
            plt.legend()
            plt.show()

def main():
    analisi = AnalisiTemperature()
    
    while True:
        print("\nMenu:")
        print("1. Genera dati")
        print("2. Calcola statistiche")
        print("3. Visualizza grafico")
        print("4. Visualizza grafico per città")
        print("5. Esci")
        
        scelta = input("Scegli un'opzione: ")
        
        if scelta == '1':
            analisi.genera_dati()
        elif scelta == '2':
            analisi.calcola_statistiche()
        elif scelta == '3':
            analisi.visualizza_grafico_citta()
        elif scelta == '4':
            citta = input("Inserisci il nome della città: ")
            analisi.visualizza_grafico_citta(citta)
        elif scelta == '5':
            print("Uscita dal programma.")
            break
        else:
            print("Opzione non valida. Riprova.")

if __name__ == '__main__':
    main()
