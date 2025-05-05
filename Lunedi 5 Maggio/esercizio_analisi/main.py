import pandas as pd
import numpy as np
from sklearn.model_selection import KFold, cross_val_score
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import LabelEncoder

# 1) load data
train = pd.read_csv(r"Lunedi 5 Maggio\esercizio_analisi\train.csv")     # must contain columns: id, Sex, Age, Height, Weight, Duration, Heart_Rate, Body_Temp, Calories
test  = pd.read_csv(r"Lunedi 5 Maggio\esercizio_analisi\test.csv")      # same as above minus the Calories column

# 2) basic cleaning / feature engineering
#    encode "Sex" as 0/1
le = LabelEncoder()
train["Sex_enc"] = le.fit_transform(train["Sex"])
test["Sex_enc"]  = le.transform(test["Sex"])

FEATURES = ["Sex_enc", "Age", "Height", "Weight", "Duration", "Heart_Rate", "Body_Temp"]
TARGET   = "Calories"

X = train[FEATURES]
y = train[TARGET]
X_test = test[FEATURES]

# 3) instantiate and cross‐validate a model
model = GradientBoostingRegressor(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=5,
    subsample=0.8,
    random_state=42
)

# 3a) quick 5‐fold CV to check performance (mean R^2 or negative RMSE)
cv = KFold(n_splits=5, shuffle=True, random_state=1)
rmse_scores = -cross_val_score(
    model, X, y,
    scoring="neg_root_mean_squared_error",
    cv=cv,
    n_jobs=-1
)
print("CV RMSE: %.4f ± %.4f" % (rmse_scores.mean(), rmse_scores.std()))

# 4) fit on full train and predict
model.fit(X, y)
preds = model.predict(X_test)

# 5) write submission
submission = pd.DataFrame({
    "id": test["id"],
    "Calories": preds
})
submission.to_csv("submission.csv", index=False)
print("Wrote submission.csv with", len(submission), "rows.")