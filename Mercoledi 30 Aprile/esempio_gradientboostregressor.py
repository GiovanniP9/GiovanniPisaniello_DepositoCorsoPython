import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Caricamento del dataset California Housing
print("Caricamento del dataset California Housing...")
housing = fetch_california_housing()
X, y = housing.data, housing.target
feature_names = housing.feature_names
print(f"Dataset caricato: {X.shape[0]} campioni con {X.shape[1]} caratteristiche")

# Standardizzazione delle caratteristiche
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Divisione del dataset in training e test set
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
print(f"Training set: {X_train.shape[0]} campioni")
print(f"Test set: {X_test.shape[0]} campioni")

# Creazione e addestramento del modello Gradient Boosting Regressor
print("\nAddestramento del Gradient Boosting Regressor...")
gbr = GradientBoostingRegressor(
    n_estimators=100,      # Numero di alberi di decisione
    learning_rate=0.1,     # Tasso di apprendimento
    max_depth=3,           # Profondità massima degli alberi
    subsample=0.8,         # Percentuale di campioni utilizzati per ogni albero
    random_state=42        # Seed per la riproducibilità
)

# Addestramento del modello
gbr.fit(X_train, y_train)

# Previsioni sul training e test set
y_train_pred = gbr.predict(X_train)
y_test_pred = gbr.predict(X_test)

# Valutazione delle prestazioni
train_mse = mean_squared_error(y_train, y_train_pred)
test_mse = mean_squared_error(y_test, y_test_pred)
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

print("\nRisultati:")
print(f"MSE sul training set: {train_mse:.4f}")
print(f"MSE sul test set: {test_mse:.4f}")
print(f"R² sul training set: {train_r2:.4f}")
print(f"R² sul test set: {test_r2:.4f}")

# Visualizzazione dell'importanza delle caratteristiche
importances = gbr.feature_importances_
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(12, 6))
plt.title('Importanza delle caratteristiche')
plt.bar(range(X.shape[1]), importances[indices], align='center')
plt.xticks(range(X.shape[1]), [feature_names[i] for i in indices], rotation=90)
plt.tight_layout()

# Visualizzazione delle previsioni vs valori reali
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_test_pred, alpha=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)
plt.xlabel('Valori reali')
plt.ylabel('Previsioni')
plt.title('Previsioni vs Valori reali')
plt.tight_layout()

# Visualizzazione dell'errore di previsione
plt.figure(figsize=(10, 6))
plt.scatter(y_test_pred, y_test_pred - y_test, alpha=0.5)
plt.hlines(y=0, xmin=y_test_pred.min(), xmax=y_test_pred.max(), colors='r', linestyles='--')
plt.xlabel('Previsioni')
plt.ylabel('Residui')
plt.title('Residui vs Previsioni')
plt.tight_layout()

plt.show()
