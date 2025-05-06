# Import delle librerie per manipolazione dati e modelli ML
import pandas as pd
import numpy as np
from sklearn.model_selection import KFold, GridSearchCV
from xgboost import XGBRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import make_scorer, mean_squared_log_error

# 1) Caricamento del dataset
train = pd.read_csv(r"Lunedi 5 Maggio\esercizio_analisi\train.csv")
test  = pd.read_csv(r"Lunedi 5 Maggio\esercizio_analisi\test.csv")

# 2) Preprocessing: codifica della variabile categorica
le = LabelEncoder()
train["Sex_enc"] = le.fit_transform(train["Sex"])
test["Sex_enc"]  = le.transform(test["Sex"])

# 3) Rimozione valori negativi nel target
train = train[train["Calories"] >= 0]
# Rimozione outlier con metodo IQR su variabili numeriche
num_cols = ["Age","Height","Weight","Duration","Heart_Rate","Body_Temp","Calories"]
for col in num_cols:
    Q1, Q3 = train[col].quantile([0.25, 0.75])
    IQR = Q3 - Q1
    train = train[(train[col] >= Q1 - 1.5*IQR) & (train[col] <= Q3 + 1.5*IQR)]

# 4) Creazione di nuove feature per migliorare la prediction
train["BMI"]           = train["Weight"] / ((train["Height"]/100)**2)
test["BMI"]            = test["Weight"]  / ((test["Height"]/100)**2)
train["HR_Duration"]   = train["Heart_Rate"] * train["Duration"]
test["HR_Duration"]    = test["Heart_Rate"] * test["Duration"]
train["Temp_Duration"] = train["Body_Temp"]  * train["Duration"]
test["Temp_Duration"]  = test["Body_Temp"]  * test["Duration"]

# Rimozione outlier sulle nuove feature con metodo IQR
for col in ["BMI", "HR_Duration", "Temp_Duration"]:
    Q1, Q3 = train[col].quantile([0.25, 0.75])
    IQR = Q3 - Q1
    train = train[(train[col] >= Q1 - 1.5 * IQR) & (train[col] <= Q3 + 1.5 * IQR)]

# 4) Definizione delle feature e del target
FEATURES = [
    "Sex_enc","Age","Height","Weight",
    "Duration","Heart_Rate","Body_Temp",
    "BMI","HR_Duration","Temp_Duration"
]
TARGET   = "Calories"
X        = train[FEATURES]
y        = train[TARGET]
X_test   = test[FEATURES]

# 5) GridSearchCV con MSLE come metrica
def msle_scorer(y_true, y_pred):
    y_pred = np.maximum(y_pred, 0)  # Forza y_pred ≥ 0
    return mean_squared_log_error(y_true, y_pred)

param_grid = {
    'n_estimators':      [100, 200],
    'max_depth':         [3, 5],
    'learning_rate':     [0.05, 0.1],
    'subsample':         [0.8, 1.0],
    'colsample_bytree':  [0.8, 1.0]
}
xgb = XGBRegressor(objective='reg:squarederror', random_state=73)
cv = KFold(n_splits=5, shuffle=True, random_state=42)
grid = GridSearchCV(
    xgb,
    param_grid,
    scoring=make_scorer(msle_scorer, greater_is_better=False),
    cv=cv, n_jobs=-1, verbose=1
)
grid.fit(X, y)

print("Best params:", grid.best_params_)
print("Best CV MSLE: %.6f" % (-grid.best_score_))
best_msle = -grid.best_score_
print("Best CV RMSLE: %.6f" % (np.sqrt(best_msle)))

model = grid.best_estimator_

# 6) Predizione su test set
preds = model.predict(X_test)
preds = np.maximum(preds, 0)  # Forza predizioni ≥ 0

# 7) Creazione file di submission
submission = pd.DataFrame({
    "id": test["id"],
    "Calories": preds
})
submission.to_csv("submission.csv", index=False)
print("Wrote submission.csv with", len(submission), "rows.")