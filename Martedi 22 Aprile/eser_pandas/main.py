import pandas as pd
import numpy as np

# generazione casuale di un DataFrame di esempio
nomi= {'Anna', 'Luca', 'Marco', 'Giulia', 'Paolo', 'Sara', 'Marta', 'Davide', 'Elisa', 'Francesco'}
citta = {'Roma', 'Milano', 'Napoli', 'Torino', 'Firenze', 'Bologna', 'Venezia', 'Palermo', 'Genova', 'Verona'}

dati = {
    'Nome': np.random.choice(list(nomi), 20),
    'Età': np.random.randint(18, 70, 20),
    'Città': np.random.choice(list(citta), 20),
    'Salario': np.random.uniform(1500, 5000, 20).astype(float),
}	
df = pd.DataFrame(dati)
# Stampa del DataFrame originale
print("DataFrame Originale:")
print(df)

#aggiunta di errori nei dati
df.loc[0, 'Nome'] = np.nan  # valore mancante
df.loc[1, 'Età'] = 200  # valore non valido
df.loc[2, 'Salario'] = -1000  # valore negativo
df.loc[3, 'Città'] = np.nan  # valore mancante
df.loc[4, 'Nome'] = 'Marco'  # duplicato
df.loc[5, 'Nome'] = 'Marco'  # duplicato
df.loc[6, 'Età'] = np.nan  # valore mancante
df.loc[7, 'Salario'] = np.nan  # valore mancante

#visualizzazione delle prime righe del DataFrame
print("\nPrime righe del DataFrame con errori:")
print(df.head())
#visualizzazione delle ultime righe del DataFrame
print("\nUltime righe del DataFrame con errori:")
print(df.tail())

#visualizzazione tipo di dati
print("\nTipo di dati delle colonne:")
print(df.dtypes)
#visualizzazione statistiche descrittive
print("\nStatistiche descrittive:")
print(df.describe())
#statistiche aggiuntive: mediana e deviazione standard
print("\nMediana eta:")
print(df['Età'].median())
print("\nDeviazione standard eta:")
print(df['Età'].std())
print("\nMediana salario:")
print(df['Salario'].median())
print("\nDeviazione standard salario:")
print(df['Salario'].std())

#rimozione dei duplicati
df = df.drop_duplicates('Nome')  # Rimozione dei duplicati in base alla colonna 'Nome'
#rimozione delle righe con valori non validi
df = df[(df['Età'] >= 0) & (df['Età'] <= 70)]  # Rimozione delle righe con età non valida
df = df[df['Salario'] >= 0]  # Rimozione delle righe con salario negativo

# Gestione dei dati mancanti
df['Età'].fillna(df['Età'].mean(), inplace=True)  # Sostituzione dei valori mancanti con la media
df['Salario'].fillna(df['Salario'].mean(), inplace=True)  # Sostituzione dei valori mancanti con la media
df['Città'].fillna('Sconosciuta', inplace=True)  # Sostituzione dei valori mancanti con 'Sconosciuta'
df['Nome'].fillna('Sconosciuto', inplace=True)  # Sostituzione dei valori mancanti con 'Sconosciuto'

#aggiunta di una nuova colonna per indicare la categoria di età
def categoria_eta(eta):
    if eta <= 18:
        return 'Giovane'
    elif eta <= 65:
        return 'Adulto'
    else:
        return 'Anziano'


df['Categoria_Eta'] = df['Età'].apply(categoria_eta)  # Applicazione della funzione per creare la nuova colonna 

# Stampa del DataFrame pulito
print("\nDataFrame dopo la pulizia:")
print(df)
#salvataggio del DataFrame pulito in un file CSV
df.to_csv('DataFrame_pulito.csv', index=False)  # Salvataggio del DataFrame pulito in un file CSV
print("\nDataFrame pulito salvato in 'DataFrame_pulito.csv'")