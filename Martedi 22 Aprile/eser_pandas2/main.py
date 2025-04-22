import pandas as pd
import numpy as np

# Dati di esempio
prodotti = {'Laptop', 'Mouse', 'Tastiera', 'Monitor', 'Stampante'}
citta = {'Roma', 'Milano', 'Napoli', 'Torino', 'Firenze'}

df = pd.DataFrame({
    'Prodotto': np.random.choice(list(prodotti), 10),
    'Quantita': np.random.randint(1, 50, 10),
    'Prezzo Unitario': np.random.uniform(50, 500, 10),
    'Citta': np.random.choice(list(citta), 10)
})

# aggiunta colonna totale vendite
df['Totale Vendite'] = df['Quantita'] * df['Prezzo Unitario']

#totale vendite per prodotto
def mostra_vendite_prodotto():
    totale_vendite_prodotto = df.groupby('Prodotto')['Totale Vendite'].sum().sort_values(ascending=False)# ordina in modo decrescente
    print("Totale vendite per prodotto:")
    print(totale_vendite_prodotto)

#prodotto piu venduto in quantita
def prodotto_piu_venduto():
    prodotto_piu_venduto = df.groupby('Prodotto')['Quantita'].sum().idxmax()
    print(f"Prodotto più venduto in quantità: {prodotto_piu_venduto}")


#citta con volume di vendite piu alto
def citta_volume_vendite():
    citta_volume_vendite = df.groupby('Citta')['Totale Vendite'].sum().idxmax()
    print(f"Città con volume di vendite più alto: {citta_volume_vendite}")



#nuovo dataframe con vendite totali superiori a 1000
def vendite_superiori():
    vendite_superiori = df[df['Totale Vendite'] > 1000]
    print("DataFrame con vendite totali superiori a 1000:")
    print(vendite_superiori)


#ordinamento del dataframe in base al totale vendite in modo decrescente
def ordina_dataframe():
    df_ordinato = df.sort_values(by='Totale Vendite', ascending=False)
    print("DataFrame ordinato in base al totale vendite:")
    print(df_ordinato)


#numero vendite per citta
def vendite_per_citta():
    vendite_per_citta = df['Citta'].counts()
    print("Numero vendite per città:")
    print(vendite_per_citta)

#pivot personalizzata
def pivot_personalizzata():
    print("Crea la tua tabella pivot personalizzata:")
    print("Colonne disponibili:", list(df.columns))
    
    index = input("Scegli la colonna da usare come indice: ")
    columns = input("Scegli la colonna da usare come colonne: ")
    values = input("Scegli la colonna da usare come valori: ")
    aggfunc = input("Scegli la funzione di aggregazione (sum, mean, count): ")
    
    try:
        pivot_df = df.pivot_table(index=index, columns=columns, values=values, aggfunc=aggfunc)
        print("Tabella pivot personalizzata:")
        print(pivot_df)
    except KeyError as e:
        print(f"Errore: {e}. Assicurati che le colonne scelte siano valide.")

#funzione principale
def main():
    print("Benvenuto nel programma di analisi delle vendite!")
    while True:
        print("\nMenu:")
        print("1. Mostra totale vendite per prodotto")
        print("2. Prodotto più venduto in quantità")
        print("3. Città con volume di vendite più alto")
        print("4. DataFrame con vendite totali superiori a 1000")
        print("5. Ordina DataFrame in base al totale vendite")
        print("6. Numero vendite per città")
        print("7. Crea tabella pivot personalizzata")
        print("8. Esci")

        scelta = input("Scegli un'opzione (1-8): ")

        match scelta:
            case "1":
                mostra_vendite_prodotto()
            case "2":
                prodotto_piu_venduto()
            case "3":
                citta_volume_vendite()
            case "4":
                vendite_superiori()
            case "5":
                ordina_dataframe()
            case "6":
                vendite_per_citta()
            case "7":
                pivot_personalizzata()
            case "8":
                print("Uscita dal programma.")
                break
            case _:
                print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()
