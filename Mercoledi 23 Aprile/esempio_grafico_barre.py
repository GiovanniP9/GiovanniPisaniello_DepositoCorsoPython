import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E'] # Categorie per l'asse X
values = [3, 7, 2, 5, 8] # Valori per l'asse Y

plt.figure() # Crea una nuova figura
plt.bar(categories, values) # Crea un grafico a barre
plt.title('Grafico a Barre') # Imposta il titolo del grafico
plt.xlabel('Categorie') # Imposta l'etichetta dell'asse X
plt.ylabel('Valori') # Imposta l'etichetta dell'asse Y
plt.show() # Mostra il grafico
# plt.savefig('grafico_a_barre.png') # Salva il grafico come immagine PNG