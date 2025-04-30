import xgboost as xgb
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler  # Import per la normalizzazione

# Carica il dataset kc_house_data_clean.csv
dataset_path = "Mercoledi 30 Aprile\kc_house_data_cleaned.csv"
housing_data = pd.read_csv(dataset_path)

housing_data = housing_data.drop(columns=['date'])  # Rimuovi colonne non necessarie

# Prepara i dati: separa features e target (assumiamo che 'price' sia la variabile target)
X = housing_data.drop('price', axis=1)
y = housing_data['price']

# Normalizzazione delle features
feature_scaler = StandardScaler()
X_scaled = feature_scaler.fit_transform(X)
X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns)  # Mantiene i nomi delle colonne

# Normalizzazione del target (price)
y_scaler = StandardScaler()
y_scaled = y_scaler.fit_transform(y.values.reshape(-1, 1)).flatten()

# Split dei dati in training e test set (usando i dati normalizzati)
X_train, X_test, y_train, y_test = train_test_split(X_scaled_df, y_scaled, test_size=0.2, random_state=42)

# Crea il DMatrix per XGBoost
dtrain = xgb.DMatrix(X_train, label=y_train, missing=np.nan)
dtest = xgb.DMatrix(X_test, label=y_test, missing=np.nan)

# Parametri iniziali (fissi per questo esempio)
params = {
    'objective': 'reg:squarederror',
    'eta': 0.1,
    'max_depth': 6,
}

# Definizione della griglia per alpha e lambda
param_grid = {
    'alpha': [0, 0.1, 0.5, 1],
    'lambda': [0, 0.1, 0.5, 1]
}

best_params = {}
best_rmse = float("inf")

# Ricerca a griglia
for alpha in param_grid['alpha']:
    for lambda_ in param_grid['lambda']:
        params['alpha'] = alpha
        params['lambda'] = lambda_
        cv_results = xgb.cv(
            params,
            dtrain,
            num_boost_round=100,
            nfold=5,
            metrics="rmse",
            early_stopping_rounds=10,
            seed=42,
            verbose_eval=False
        )
        mean_rmse = cv_results['test-rmse-mean'].min()
        print(f"alpha: {alpha}, lambda: {lambda_}, RMSE: {mean_rmse:.4f}")
        if mean_rmse < best_rmse:
            best_rmse = mean_rmse
            best_params = {'alpha': alpha, 'lambda': lambda_}
            best_rounds = cv_results['test-rmse-mean'].argmin() + 1

print(f"Migliori parametri: {best_params} con RMSE: {best_rmse:.4f} in {best_rounds} rounds")

# Addestramento del modello finale con i migliori parametri
final_params = params.copy()
final_params.update(best_params)
final_model = xgb.train(
    final_params,
    dtrain,
    num_boost_round=best_rounds
)
# Valutazione sul test set
y_pred = final_model.predict(dtest)
test_rmse = np.sqrt(np.mean((y_pred - y_test)**2))
print(f"RMSE normalizzato sul test set: {test_rmse:.4f}")
# Visualizzazione dell'importanza delle features
print("\nImportanza delle features:")
feature_importance = final_model.get_score(importance_type='weight')
sorted_importance = sorted(feature_importance.items(), key=lambda x: x[1], reverse=True)
for feature, importance in sorted_importance[:10]:  # Top 10 features
    print(f"{feature}: {importance}")

