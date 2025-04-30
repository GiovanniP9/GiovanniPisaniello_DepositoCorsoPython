import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report

# Carichiamo il dataset Iris
iris = load_iris()
X = iris.data
y = iris.target

# Dividiamo in training e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Definiamo i parametri da ottimizzare
param_grid = {
    'max_depth': [None, 3, 5, 7, 10],
    'criterion': ['gini', 'entropy'],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Creiamo il modello Decision Tree
tree = DecisionTreeClassifier(random_state=42)

# Grid Search con cross-validation
grid_search = GridSearchCV(tree, param_grid, cv=5, scoring='accuracy', n_jobs=-1, verbose=1)
grid_search.fit(X_train, y_train)

# Stampiamo i risultati della ricerca
print("Migliori parametri trovati:")
print(grid_search.best_params_)
print(f"Miglior punteggio di cross-validation: {grid_search.best_score_:.4f}")

# Testiamo il modello con i migliori parametri sul test set
best_tree = grid_search.best_estimator_
best_accuracy = best_tree.score(X_test, y_test)
print(f"Accuratezza sul test set con i migliori parametri: {best_accuracy:.4f}")

# Visualizziamo l'albero decisionale ottimizzato
plt.figure(figsize=(15, 10))
plot_tree(best_tree, feature_names=iris.feature_names, 
          class_names=iris.target_names, filled=True, fontsize=10)
plt.title("Decision Tree ottimizzato su dataset Iris")
plt.show()

# Report dettagliato di classificazione
y_pred = best_tree.predict(X_test)
print("\nReport di classificazione:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))
