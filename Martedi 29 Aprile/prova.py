# Importiamo le librerie necessarie
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

# Creiamo un dataset sintetico con una relazione lineare
np.random.seed(42)
X = np.random.rand(100, 1) * 10 # Valori tra 0 e 10
y = 3 * X + 5 + np.random.randn(100, 1) * 2 # Relazione lineare con rumore

# Suddividiamo il dataset in training e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creiamo e addestriamo il modello di regressione lineare
model = LinearRegression()
model.fit(X_train, y_train)

# Facciamo previsioni sul test set
y_pred = model.predict(X_test)

# Calcoliamo il coefficiente di determinazione R^2
r2 = r2_score(y_test, y_pred)

# Stampiamo il valore di R^2
print(f"Coefficiente di determinazione R^2: {r2:.2f}")