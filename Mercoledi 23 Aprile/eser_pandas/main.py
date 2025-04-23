import pandas as pd
import numpy as np

class VenditeMensili:
    def __init__(self):
        self.df = None
        self.df_pivot = None
        self.df_global = None

    def genera_dati(self):
        data_range = pd.date_range(start='2025-01-01', end='2025-01-31', freq='D')  # Genera un intervallo di date giornaliere tra il 1 gennaio 2025 e il 31 gennaio 2025
        citta = ['Roma', 'Milano', 'Napoli']  # Lista di città
        prodotti = ['Pizza', 'Pasta', 'Gelato']  # Lista di prodotti

        # Creazione di un DataFrame con dati casuali
        data = {
            'Data': np.random.choice(data_range, size=31),  # Seleziona casualmente 31 date dall'intervallo
            'Città': np.random.choice(citta, size=31),  # Seleziona casualmente 31 città dalla lista	
            'Prodotto': np.random.choice(prodotti, size=31),  # Seleziona casualmente 31 prodotti dalla lista
            'Vendite': np.random.randint(1, 100, size=31)  # Genera casualmente 31 vendite tra 1 e 100
        }
        self.df = pd.DataFrame(data)  # Crea un DataFrame con i dati generati
        print("Dati generati.")

    def crea_pivot(self):
        if self.df is None:
            print("Genera prima i dati.")
            return
        # Creazione pivot per vendite medie di ciascun prodotto per città
        self.df_pivot = self.df.pivot_table(values='Vendite', index='Prodotto', columns='Città', aggfunc='mean')  # Crea una tabella pivot per calcolare le vendite medie di ciascun prodotto per città
        print("Tabella pivot creata.")

    def calcola_globali(self):
        if self.df is None:
            print("Genera prima i dati.")
            return
        # Vendite globali per prodotto
        self.df_global = self.df.groupby('Prodotto')['Vendite'].sum().reset_index()  # Calcola le vendite globali per prodotto e resetta l'indice
        print("Vendite globali calcolate.")

    def salva_file(self, formato="csv"):
        # Salvataggio dei dati in file CSV, JSON o Excel
        if formato == "csv":
            if self.df is not None:
                self.df.to_csv('vendite.csv', index=False)  # Salva il DataFrame originale in un file CSV
            if self.df_pivot is not None:
                self.df_pivot.to_csv('vendite_pivot.csv')  # Salva la tabella pivot in un file CSV
            if self.df_global is not None:
                self.df_global.to_csv('vendite_globali.csv', index=False)  # Salva le vendite globali in un file CSV
            print("File CSV salvati.")
        elif formato == "json":
            if self.df is not None:
                self.df.to_json('vendite.json', orient='records', lines=True)  # Salva il DataFrame in formato JSON
            if self.df_pivot is not None:
                self.df_pivot.to_json('vendite_pivot.json', orient='records', lines=True)  # Salva la tabella pivot in formato JSON
            if self.df_global is not None:
                self.df_global.to_json('vendite_globali.json', orient='records', lines=True)  # Salva le vendite globali in formato JSON
            print("File JSON salvati.")
        elif formato == "excel":
            # Creazione di un nuovo file Excel con i vari fogli
            with pd.ExcelWriter('vendite.xlsx', engine='openpyxl') as writer:
                if self.df is not None:
                    self.df.to_excel(writer, sheet_name='Vendite', index=False)  # Scrive il DataFrame originale nel foglio 'Vendite'
                if self.df_pivot is not None:
                    self.df_pivot.to_excel(writer, sheet_name='Pivot', index=False)  # Scrive la tabella pivot nel foglio 'Pivot'
                if self.df_global is not None:
                    self.df_global.to_excel(writer, sheet_name='Globali', index=False)  # Scrive le vendite globali nel foglio 'Globali'
            print("File Excel salvato con nuovi fogli.")

    def stampa_tutto(self):
        # Output dei dati
        if self.df is not None:
            print("\nDati originali:")
            print(self.df)  # Stampa i dati originali
        if self.df_pivot is not None:
            print("\nTabella pivot:")
            print(self.df_pivot)  # Stampa la tabella pivot
        if self.df_global is not None:
            print("\nVendite globali:")
            print(self.df_global)  # Stampa le vendite globali

# === MENU INTERATTIVO ===
def menu():
    vendite = VenditeMensili()
    while True:
        print("\nMENU ANALISI VENDITE MENSILI")
        print("1. Genera dati")
        print("2. Crea tabella pivot")
        print("3. Calcola vendite globali")
        print("4. Salva tutti i file")
        print("5. Stampa tutti i dati")
        print("0. Esci")

        scelta = input("Scegli un'opzione: ")

        match scelta:
            case "1":
                vendite.genera_dati()
            case "2":
                vendite.crea_pivot()
            case "3":
                vendite.calcola_globali()
            case "4":
                formato = input("Scegli il formato (csv, json, excel): ").lower()
                if formato in ["csv", "json", "excel"]:
                    vendite.salva_file(formato)
                else:
                    print("Formato non valido.")
            case "5":
                vendite.stampa_tutto()
            case "0":
                print("Uscita dal programma.")
                break
            case _:
                print("Opzione non valida.")

if __name__ == "__main__":
    menu()