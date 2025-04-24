import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Impostiamo uno stile seaborn
sns.set_theme(style="darkgrid")

# Generiamo dati di esempio
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Creiamo il grafico
plt.figure(figsize=(8, 4))
sns.lineplot(x=x, y=y)
plt.title("Grafico di sin(x) con seaborn")
plt.xlabel("Asse X")
plt.ylabel("Asse Y")
plt.show()