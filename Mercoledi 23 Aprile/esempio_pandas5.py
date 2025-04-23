import pandas as pd
# Creazione di un DataFrame da un dizionario
data = {'nome': ['Alice', 'Bob'],
'età': [25, 30]}
df = pd.DataFrame(data)
# Caricamento di un DataFrame da un file CSV
file_path = 'Mercoledi 23 Aprile\data.csv'
df_csv = pd.read_csv(file_path)

# Visualizzazione delle statistiche descrittive
print(df.describe())
# Rimozione dei valori mancanti
df_clean = df.dropna()

# Selezione di una colonna
ages = df['età']
# Filtraggio basato su una condizione
adults = df[df['età'] >= 18]
print (adults)

# # Ordinamento dei dati per età
# df_sorted = df.sort_values(by='età')
# # Unione di due DataFrame
# merged_df = pd.merge(df, df_csv, on='nome')

# Applicazione di una funzione a una colonna
df['età_doppia'] = df['età'].apply(lambda x: x * 2)

# Esportazione di un DataFrame in un file CSV
df.to_csv('data_output.csv', index=False)

df.to_json('data.json', index=False)
