import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# plt.rcParams['figure.figsize'] = [10, 6] # Imposta la dimensione predefinita delle figure
# plt.rcParams['figure.dpi'] = 100 # Imposta la risoluzione delle figure in DPI
# plt.rcParams['figure.facecolor'] = 'white' # Colore di sfondo della figura


# # Configura Seaborn
# sns.set_theme(style="darkgrid")
# # Crea alcuni dati
# data = np.random.normal(size=100) # Genera 100 dati casuali da una distribuzione normale
# # Crea un grafico
# sns.histplot(data, kde=True) # Aggiungi una linea di densità 
# plt.title('Distribuzione dei dati')
# plt.show() # Mostra il grafico 

fig = plt.figure() # Crea una nuova figura
fig.patch.set_facecolor('lightblue') # Imposta il colore di sfondo della figura
ax = fig.add_subplot(111) # Aggiungi un sottogruppo alla figura
ax.set_title('Titolo del grafico') # Imposta il titolo del grafico
ax.set_xlabel('Asse X') # Imposta l'etichetta dell'asse X
plt.show() # Mostra il grafico