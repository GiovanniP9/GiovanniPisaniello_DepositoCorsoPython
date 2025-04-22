import pandas as pd

# Dati di esempio
data = {
'Data': ['2021-01-01', '2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
'Città': ['Roma', 'Milano', 'Napoli', 'Roma', 'Milano'],
'Prodotto': ['Mouse', 'Tastiera', 'Mouse', 'Tastiera', 'Mouse'],
'Vendite': [100, 200, 150, 300, 250]
}
df = pd.DataFrame(data)

grouped_df = df.groupby('Prodotto').sum()


grouped_df['Vendite Totali'] = grouped_df['Vendite']

print(grouped_df)