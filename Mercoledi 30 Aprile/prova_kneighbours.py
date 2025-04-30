import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

# Caricamento del dataset Iris
iris = datasets.load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

# Standardizzazione dei dati
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-Nearest Neighbors Classification with cross-validation
# Split data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Basic KNN with k=5
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

# Calcolo dell'accuratezza
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuratezza del modello K-Nearest Neighbors: {accuracy:.2f}")

# Using cross-validation for more robust assessment
cv_scores = cross_val_score(knn, X_scaled, y, cv=5)
print(f"Accuratezza con cross-validation (k=5): {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")

# Find optimal k using GridSearchCV
k_values = list(range(1, 11))  # Limitato a 10 vicini
accuracies = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)
    print(f"Accuratezza con {k} vicini: {accuracy:.4f}")

# Visualizza i risultati per diversi valori di k
plt.figure(figsize=(10, 6))
plt.plot(k_values, accuracies, marker='o', linestyle='-')
plt.title('Accuratezza del KNN in funzione del numero di vicini (k)')
plt.xlabel('Numero di vicini (k)')
plt.ylabel('Accuratezza')
plt.grid(True)
plt.xticks(np.arange(1, 11, 1))  # Aggiornato per mostrare tutti i valori da 1 a 10
plt.show()

# Trova il migliore valore di k
best_k = k_values[np.argmax(accuracies)]
print(f"\nMiglior valore di k: {best_k} con accuratezza: {max(accuracies):.4f}")

# KNN con il miglior valore di k
best_knn = KNeighborsClassifier(n_neighbors=best_k)
best_knn.fit(X_train, y_train)
y_pred_best = best_knn.predict(X_test)
accuracy_best = accuracy_score(y_test, y_pred_best)
print(f"Accuratezza del modello K-Nearest Neighbors con k ottimale: {accuracy_best:.4f}")

