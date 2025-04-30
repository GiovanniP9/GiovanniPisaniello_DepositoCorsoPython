import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler

# Load the dataset
data_path = "Martedi 29 Aprile\esercizio_prezzi_case_usa\kc_house_data_cleaned.csv"
df = pd.read_csv(data_path)

# Display basic information
print("Dataset shape:", df.shape)
print("\nFeatures in the dataset:")
print(df.columns.tolist())
print("\nDataset info:")
print(df.info())
print("\nSummary statistics:")
print(df.describe())

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Prepare features and target
X = df.drop('price', axis=1)  # Assuming 'price' is the target variable
y = df['price']

# Calculate mean of target variable for normalization
price_mean = y.mean()

#drop date
X = X.drop('date', axis=1)
# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a basic Gradient Boosting model
print("\nTraining a basic Gradient Boosting model...")
gb_model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
gb_model.fit(X_train_scaled, y_train)

# Make predictions
y_pred_train = gb_model.predict(X_train_scaled)
y_pred_test = gb_model.predict(X_test_scaled)

# Evaluate the model
print("\nModel Evaluation:")
print(f"Train R² score: {r2_score(y_train, y_pred_train):.4f}")
print(f"Test R² score: {r2_score(y_test, y_pred_test):.4f}")
rmse_train = np.sqrt(mean_squared_error(y_train, y_pred_train))
rmse_test = np.sqrt(mean_squared_error(y_test, y_pred_test))
mae_train = mean_absolute_error(y_train, y_pred_train)
mae_test = mean_absolute_error(y_test, y_pred_test)
# Original metrics
print(f"Train RMSE: ${rmse_train:.2f}")
print(f"Test RMSE: ${rmse_test:.2f}")
print(f"Train MAE: ${mae_train:.2f}")
print(f"Test MAE: ${mae_test:.2f}")
# Normalized metrics
norm_rmse_train = rmse_train / price_mean
norm_rmse_test = rmse_test / price_mean
norm_mae_train = mae_train / price_mean
norm_mae_test = mae_test / price_mean
print(f"Normalized Train RMSE: {norm_rmse_train:.4f}")
print(f"Normalized Test RMSE: {norm_rmse_test:.4f}")
print(f"Normalized Train MAE: {norm_mae_train:.4f}")
print(f"Normalized Test MAE: {norm_mae_test:.4f}")

# Feature importance
feature_importance = pd.DataFrame(
    {'Feature': X.columns, 'Importance': gb_model.feature_importances_}
).sort_values('Importance', ascending=False)

print("\nFeature Importance:")
print(feature_importance.head(10))

# Plot feature importance
plt.figure(figsize=(12, 6))
plt.barh(feature_importance['Feature'][:10], feature_importance['Importance'][:10])
plt.xlabel('Importance')
plt.title('Top 10 Feature Importance')
plt.gca().invert_yaxis()  # To display the most important feature at the top
plt.tight_layout()
plt.savefig('feature_importance.png')
plt.show()

# Plot actual vs predicted values
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred_test, alpha=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs Predicted House Prices')
plt.tight_layout()
plt.savefig('actual_vs_predicted.png')
plt.show()

# Hyperparameter tuning with GridSearchCV
print("\nPerforming hyperparameter tuning (this may take a while)...")
param_grid = {
    'n_estimators': [100, 200],
    'learning_rate': [0.05, 0.1],
    'max_depth': [3, 5],
    'min_samples_split': [2, 5],
    'subsample': [0.8, 1.0]
}

grid_search = GridSearchCV(
    GradientBoostingRegressor(random_state=42),
    param_grid=param_grid,
    cv=3,
    n_jobs=-1,
    scoring='neg_mean_squared_error',
    verbose=1
)

grid_search.fit(X_train_scaled, y_train)

# Best parameters and model
print("\nBest parameters:", grid_search.best_params_)
best_gb_model = grid_search.best_estimator_

# Evaluate the tuned model
y_pred_test_tuned = best_gb_model.predict(X_test_scaled)
print("\nTuned Model Evaluation:")
print(f"Test R² score: {r2_score(y_test, y_pred_test_tuned):.4f}")
rmse_test_tuned = np.sqrt(mean_squared_error(y_test, y_pred_test_tuned))
mae_test_tuned = mean_absolute_error(y_test, y_pred_test_tuned)
# Original metrics
print(f"Test RMSE: ${rmse_test_tuned:.2f}")
print(f"Test MAE: ${mae_test_tuned:.2f}")
# Normalized metrics
norm_rmse_test_tuned = rmse_test_tuned / price_mean
norm_mae_test_tuned = mae_test_tuned / price_mean
print(f"Normalized Test RMSE: {norm_rmse_test_tuned:.4f}")
print(f"Normalized Test MAE: {norm_mae_test_tuned:.4f}")

# Save the model results to a file
results = {
    "Basic Model": {
        "R2 Score": r2_score(y_test, y_pred_test),
        "RMSE": rmse_test,
        "MAE": mae_test,
        "Normalized RMSE": norm_rmse_test,
        "Normalized MAE": norm_mae_test
    },
    "Tuned Model": {
        "R2 Score": r2_score(y_test, y_pred_test_tuned),
        "RMSE": rmse_test_tuned,
        "MAE": mae_test_tuned,
        "Normalized RMSE": norm_rmse_test_tuned,
        "Normalized MAE": norm_mae_test_tuned
    }
}

results_df = pd.DataFrame(results)
print("\nResults comparison:")
print(results_df)
results_df.to_csv('gradient_boosting_results.csv')

print("\nGradient Boosting analysis completed!")