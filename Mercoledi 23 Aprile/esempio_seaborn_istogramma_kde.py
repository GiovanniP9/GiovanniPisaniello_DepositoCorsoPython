import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="darkgrid")  # Configura seaborn per usare la palette di colori "darkgrid"
# Generare dati casuali
data = sns.load_dataset("penguins")
# Creare un istogramma con KDE
sns.histplot(data=data, x="flipper_length_mm", kde=True) # kde=True per aggiungere la densità
plt.title('Distribuzione Lunghezza Pinne dei Pinguini')
plt.show()
