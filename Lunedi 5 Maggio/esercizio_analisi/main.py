# Import delle librerie per manipolazione dati e modelli ML
import pandas as pd
import numpy as np
from sklearn.model_selection import KFold, cross_val_score
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import LabelEncoder

# 1) Caricamento del dataset di train (con target 'Calories') e del dataset di test (senza 'Calories')
train = pd.read_csv(r"Lunedi 5 Maggio\esercizio_analisi\train.csv")
test  = pd.read_csv(r"Lunedi 5 Maggio\esercizio_analisi\test.csv")

# 2) Preprocessing: codifica della variabile categorica 'Sex' in valori numerici (0/1)
le = LabelEncoder()
train["Sex_enc"] = le.fit_transform(train["Sex"])
test["Sex_enc"]  = le.transform(test["Sex"])

# 3) Definizione delle feature (variabili indipendenti) e del target (variabile dipendente)
FEATURES = ["Sex_enc", "Age", "Height", "Weight", "Duration", "Heart_Rate", "Body_Temp"]
TARGET   = "Calories"
X        = train[FEATURES]
y        = train[TARGET]
X_test   = test[FEATURES]

# 4) Inizializzazione del modello Gradient Boosting Regressor con iperparametri scelti
model = GradientBoostingRegressor(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=5,
    subsample=0.8,
    random_state=42
)

# 5) Validazione incrociata 5‐fold per stimare l'errore RMSE sul training set
cv = KFold(n_splits=5, shuffle=True, random_state=1)
rmse_scores = -cross_val_score(
    model, X, y,
    scoring="neg_root_mean_squared_error",
    cv=cv,
    n_jobs=-1
)
print("CV RMSE: %.4f ± %.4f" % (rmse_scores.mean(), rmse_scores.std()))

# 6) Addestramento finale su tutti i dati di train e previsione dei 'Calories' per il set di test
model.fit(X, y)
preds = model.predict(X_test)

# 7) Creazione del file di submission in formato CSV
submission = pd.DataFrame({
    "id": test["id"],
    "Calories": preds
})
submission.to_csv("submission.csv", index=False)
print("Wrote submission.csv with", len(submission), "rows.")