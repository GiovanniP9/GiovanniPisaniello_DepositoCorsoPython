from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


iris = load_iris()
X = iris.data
y = iris.target

#standardizzazione dei dati
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Divisione del dataset in training e test set
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=77)

# Creazione del modello Decision Tree
model = DecisionTreeClassifier(random_state=77)
model.fit(X_train, y_train) # Addestramento del modello

y_pred = model.predict(X_test) # Predizione delle etichette per il set di test
print("classificazione report")
print(classification_report(y_test, y_pred, target_names=iris.target_names)) # Report di classificazione

#visualizzazione della matrice di confusione
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6)) # Imposta la dimensione della figura
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Matrice di Confusione')
plt.show() # Mostra la matrice di confusione