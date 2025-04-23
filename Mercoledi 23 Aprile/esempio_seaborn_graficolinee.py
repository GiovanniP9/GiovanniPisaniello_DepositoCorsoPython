import seaborn as sns
import matplotlib.pyplot as plt

# Dati di esempio
fmri = sns.load_dataset("fmri")
# Creare un grafico a linee
sns.lineplot(x="timepoint", y="signal", data=fmri, hue="region", style="event") #hue="region" per colorare le linee in base alla regione e style="event" per differenziare gli eventi
plt.title('Segnale FMRI nel Tempo')
plt.show()
