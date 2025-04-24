import seaborn as sns
import matplotlib.pyplot as plt

#configuro seaborn per usare la palette di colori "darkgrid"
sns.set_theme(style="darkgrid")

# Dati di esempio
tips = sns.load_dataset("tips")

# Creare un grafico a barre
sns.barplot(x="day", y="total_bill", data=tips)
plt.title('Conto Totale per Giorno')
plt.show()