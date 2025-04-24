import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class VisitatoriParco:
    def __init__(self, giorni=365, media=2000, deviazione=500, trend_max = 1000):
        self.giorni = giorni
        self.media = media
        self.deviazione = deviazione
        self.trend_max = trend_max
        self.df = None
    
    # genero i dati per i visitatori del parco
    def genera_dati(self):
        np.random.seed(30) # Per riproducibilità
        date_range = pd.date_range(start="2023-01-01", periods=self.giorni) # Genera un range di date
        visitatori_base = np.random.normal(loc=self.media, scale=self.deviazione, size=self.giorni) # Genera visitatori casuali
        trend = np.linspace(0, self.trend_max, self.giorni) # Genera un trend crescente
        visitatori = np.maximum(visitatori_base + trend, 0) # Assicura che i visitatori non siano negativi
        self.df = pd.DataFrame({
            "Data": date_range,
            "Visitatori": visitatori
        }).set_index("Data")
    
    #metodo per le statistiche mensili della media e della deviazione standard
    def statistiche_mensili(self):
        if self.df is None:
            print("Genera i dati prima di calcolare le statistiche mensili.")
            return None
        media_mensile = self.df['Visitatori'].resample('ME').mean() # Media mensile dei visitatori
        deviazione_mensile = self.df['Visitatori'].resample('ME').std() # Deviazione standard mensile
        return media_mensile, deviazione_mensile
    
    #metodo per il grafico dei visitatori giornalieri con media mobile a 7 giorni per mostrare la tendenza settimanale
    def grafico_visitatori_giornaliero(self):
        plt.figure(figsize=(14, 7))
        sns.lineplot(data=self.df, x=self.df.index, y='Visitatori', label='Visitatori Giornalieri', color='blue', alpha=0.5)
        sns.lineplot(x=self.df.index, y=self.df['Visitatori'].rolling(window=7).mean(), label='Media Mobile 7 Giorni', color='red')# il rolling window è settato a 7 giorni cosi da avere una media mobile settimanale
        plt.title('Visitatori Giornalieri con Media Mobile a 7 Giorni')
        plt.xlabel('Data')
        plt.ylabel('Numero di Visitatori')
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()
    
    # metodo per il grafico della media mensile dei visitatori
    def grafico_media_mensile(self):
        media_mensile, _ = self.statistiche_mensili() # Ottiene la media mensile
        plt.figure(figsize=(14, 7))
        sns.lineplot(x=media_mensile.index.strftime('%Y-%m'), y=media_mensile.values, marker='o', label='Media Mensile', color='green')
        plt.title('Media Mensile dei Visitatori')
        plt.xlabel('Data')
        plt.ylabel('Numero di Visitatori')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.legend()
        plt.show()
    
    def grafici_combinati(self):
        media_mensile, _ = self.statistiche_mensili()
        
        fig, axs = plt.subplots(2, 1, figsize=(14, 10))
        
        #grafico visitatori giornalieri con media mobile a 7 giorni
        sns.lineplot(data=self.df, x=self.df.index, y='Visitatori', label='Visitatori Giornalieri', color='blue', alpha=0.5, ax=axs[0])
        sns.lineplot(x=self.df.index, y=self.df['Visitatori'].rolling(window=7).mean(), label='Media Mobile 7 Giorni', color='red', ax=axs[0]) # il rolling window è settato a 7 giorni cosi da avere una media mobile settimanale
        axs[0].set_title('Visitatori Giornalieri con Media Mobile a 7 Giorni')
        axs[0].set_xlabel('Data')
        axs[0].set_ylabel('Numero di Visitatori')
        axs[0].grid(True)
        axs[0].legend()
        
        #grafico media mensile dei visitatori
        sns.lineplot(x=media_mensile.index.strftime('%Y-%m'), y=media_mensile.values, marker='o', label='Media Mensile', color='green', ax=axs[1])
        axs[1].set_title('Media Mensile dei Visitatori')
        axs[1].set_xlabel('Mese')
        axs[1].set_ylabel('Visitatori Medi')
        axs[1].tick_params(axis='x', rotation=45)
        axs[1].grid(True)
        axs[1].legend()
        
        plt.tight_layout()
        plt.show()
        


def main():
    parco = VisitatoriParco()
    parco.genera_dati()
    while True:
        print("Menu:")
        print("1. Mostra statistiche mensili")
        print("2. Grafico visitatori giornalieri")
        print("3. Grafico media mensile")
        print("4. Grafici combinati")
        print("5. Uscita")
        scelta = input("Scegli un'opzione (1-5): ")
        
        match scelta:
            case '1':
                media_mensile, deviazione_mensile = parco.statistiche_mensili()
                print("Media Mensile:\n", media_mensile)
                print("Deviazione Standard Mensile:\n", deviazione_mensile)
            case '2':
                parco.grafico_visitatori_giornaliero()
            case '3':
                parco.grafico_media_mensile()
            case '4':
                parco.grafici_combinati()
            case '5':
                print("Uscita dal programma.")
                break
            case _:
                print("Opzione non valida. Riprova.")
                
if __name__ == "__main__":
    main()
       