import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler

class Normalizer:
    def __init__(self):
        self.n = 100
        self.df = None
        self.df_normalized = None
    
    # metodo per generare i dati
    def generate_data(self):
        self.df = pd.DataFrame({
            'altezza': np.random.randint(150, 200, size=self.n),
            'peso': np.random.randint(50, 100, size=self.n),
            'età': np.random.randint(18, 80, size=self.n)
        })
        print("dati generati")
    #metodo per normalizzare i dati
    def normalize_data(self):
        if self.df is None:
            print("Genera i dati prima di normalizzarli")
            return
        scaler = MinMaxScaler()# crea un oggetto MinMaxScaler
        # normalizza i dati tra 0 e 1
        norm_data = scaler.fit_transform(self.df[['altezza', 'peso']])# normalizza solo altezza e peso
        self.df_normalized = pd.DataFrame(norm_data, columns=['altezza', 'peso'])# crea un nuovo DataFrame con i dati normalizzati
        self.df_normalized['età'] = self.df['età']# aggiunge la colonna età al DataFrame normalizzato
        print("dati normalizzati")
    
    # metodo per mostrare i dati
    def mostra_dati(self):
        if self.df is None or self.df_normalized is None:
            print("Genera e normalizza i dati prima di mostrarli")
            return
        print("Dati originali:")
        print(self.df.head())
        print("Dati normalizzati:")
        print(self.df_normalized.head())
    
    # metodo per mostrare i grafici
    def mostra_grafici(self):
        if self.df is None or self.df_normalized is None:
            print("Genera e normalizza i dati prima di mostrarli")
            return
        # creazione fascia eta per il grafico
        self.df['Fascia_eta'] = pd.cut(self.df['età'], bins=10)
        self.df_normalized['Fascia_eta'] = pd.cut(self.df_normalized['età'], bins=10)
        
        # grafico dei dati originali
        plt.figure(figsize=(10, 5))
        sns.scatterplot(data=self.df, x='altezza', y='peso', hue='Fascia_eta', palette='viridis')
        plt.title('Dati Originali - Età raggruppata')
        plt.legend(title="Fasce d'età", bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
        plt.tight_layout(rect=[0, 0, 0.85, 1])  # Spazio a destra per la legenda
        plt.show()
        
        # Grafico dei dati normalizzati
        plt.figure(figsize=(10, 5))
        sns.scatterplot(data=self.df_normalized, x='altezza', y='peso', hue='Fascia_eta', palette='viridis')
        plt.title('Dati Normalizzati - Età raggruppata')
        plt.legend(title="Fasce d'età", bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
        plt.tight_layout(rect=[0, 0, 0.85, 1])
        plt.show()
    
def main():
    normalizza = Normalizer()# crea un oggetto Normalizer
    while True:
        print("Menu:")
        print("1. Genera dati")
        print("2. Normalizza dati")
        print("3. Mostra dati")
        print("4. Mostra grafici")
        print("5. Esci")
        scelta = input("Scegli un'opzione: ")
        
        if scelta == '1':
            normalizza.generate_data()
        elif scelta == '2':
            normalizza.normalize_data()
        elif scelta == '3':
            normalizza.mostra_dati()
        elif scelta == '4':
            normalizza.mostra_grafici()
        elif scelta == '5':
            break
        else:
            print("Opzione non valida")

if __name__ == "__main__":
    main()