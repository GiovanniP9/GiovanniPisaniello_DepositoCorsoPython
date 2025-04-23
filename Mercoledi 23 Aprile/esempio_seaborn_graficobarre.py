import seaborn as sns
import matplotlib.pyplot as plt

# Dati di esempio
tips = sns.load_dataset("tips")

# Creare un grafico a barre
sns.barplot(x="day", y="total_bill", data=tips)
plt.title('Conto Totale per Giorno')
plt.show()