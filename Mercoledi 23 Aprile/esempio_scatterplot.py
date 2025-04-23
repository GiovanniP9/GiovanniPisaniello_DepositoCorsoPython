import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)  # Dati casuali per l'asse X
y = np.random.rand(50)  # Dati casuali per l'asse Y

plt.figure()  # Crea una nuova figura
plt.scatter(x, y)  # Crea un grafico a dispersione (scatter plot)
plt.title('Grafico a Dispersione')  # Imposta il titolo del grafico
plt.xlabel('Asse X')  # Imposta l'etichetta dell'asse X
plt.ylabel('Asse Y')  # Imposta l'etichetta dell'asse Y
plt.show()  # Mostra il grafico
# plt.savefig('grafico_a_dispersione.png')  # Salva il grafico come immagine PNG