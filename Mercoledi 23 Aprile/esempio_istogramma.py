import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)  # Genera 1000 dati casuali da una distribuzione normale

plt.figure()
plt.hist(data, bins= 30)
plt.title('Istogramma dei Dati Casuali')  # Imposta il titolo del grafico
plt.xlabel('Valori')  # Imposta l'etichetta dell'asse X
plt.ylabel('Frequenza')  # Imposta l'etichetta dell'asse Y
plt.show()  # Mostra il grafico
# plt.savefig('istogramma.png')  # Salva il grafico come immagine PNG