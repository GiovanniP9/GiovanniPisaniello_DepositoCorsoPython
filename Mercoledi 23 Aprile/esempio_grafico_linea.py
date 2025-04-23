import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5] # Dati per l'asse X
y = [2, 3, 5, 7, 11] # Dati per l'asse Y

plt.figure()
plt.plot(x, y) # Crea un grafico a linea
plt.title('Grafico a Linea') # Imposta il titolo del grafico
plt.xlabel('Asse X') # Imposta l'etichetta dell'asse X
plt.ylabel('Asse Y') # Imposta l'etichetta dell'asse Y
plt.show() # Mostra il grafico