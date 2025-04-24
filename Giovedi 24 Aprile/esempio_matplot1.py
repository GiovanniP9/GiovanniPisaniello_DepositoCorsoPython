import matplotlib.pyplot as plt
import numpy as np

# Generiamo dati di esempio
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Creiamo il grafico
plt.figure(figsize=(8, 4))            # imposta la dimensione della figura (larghezza, altezza)
plt.plot(x, y)                        # disegna y in funzione di x
plt.title("Grafico di sin(x)")        # titolo del grafico
plt.xlabel("Asse X")                  # etichetta asse X
plt.ylabel("Asse Y")                  # etichetta asse Y
plt.grid(True)                        # mostra la griglia
plt.show()                            # visualizza il grafico