import pandas as pd

# Creazione di un DataFrame con dati di esempio
data = {
 'Nome': ['Alice', 'Bob', 'Carla'],
 'Età': [25, 30, 22],
 'Città': ['Roma', 'Milano', 'Napoli']
}
df = pd.DataFrame(data)
# Stampa del DataFrame originale
print("DataFrame Originale:")
print(df)
 
# Selezione delle righe dove l'età è superiore a 23
df_older = df[df['Età'] > 23] # Filtriamo le righe in cui l'età è maggiore di 23
 
# Stampa delle righe selezionate
print("\nPersone con età superiore a 23 anni:")
print(df_older)

# Aggiungiamo una nuova colonna per indicare se la persona è maggiorenne
df['Maggiorenne'] = df['Età'] >= 18 # Verifichiamo se l'età è maggiore o uguale a 18 per aggiungere una nuova colonna che da valore True o False

# Stampa del DataFrame con la nuova colonna
print("\nDataFrame con colonna 'Maggiorenne':")
print(df)