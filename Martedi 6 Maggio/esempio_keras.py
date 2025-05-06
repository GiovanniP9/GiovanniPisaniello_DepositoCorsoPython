import tensorflow as tf
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

housing = fetch_california_housing()
X_train_full, X_test, y_train_full, y_test = train_test_split(
    housing.data, housing.target, random_state=42)
X_train, X_valid, y_train, y_valid = train_test_split(
    X_train_full, y_train_full, random_state=42)

#Imposta il seed per riproducibilità
tf.random.set_seed(42)

#Layer di normalizzazione senza input_shape
norm_layer = tf.keras.layers.Normalization()

#Costruzione del modello con API funzionale
inputs = tf.keras.Input(shape=X_train.shape[1:])
x = norm_layer(inputs)
x = tf.keras.layers.Dense(50, activation="relu")(x)
x = tf.keras.layers.Dense(50, activation="relu")(x)
x = tf.keras.layers.Dense(50, activation="relu")(x)
outputs = tf.keras.layers.Dense(1)(x)

model = tf.keras.Model(inputs=inputs, outputs=outputs)

#Compilazione
optimizer = tf.keras.optimizers.Adam(learning_rate=2e-4) #Learning rate più basso per evitare overfitting
model.compile(loss="mse", optimizer=optimizer, metrics=["RootMeanSquaredError"])

#Adattamento della normalizzazione
norm_layer.adapt(X_train)

#Addestramento
history = model.fit(
    X_train, y_train,
    epochs=50,
    validation_data=(X_valid, y_valid)
)

#grafico delle metriche
import pandas as pd
import matplotlib.pyplot as plt

pd.DataFrame(history.history).plot(figsize=(8, 5), grid=True, xlabel="Epoch", style=["r--", "r--.", "b-", "b-*"])
plt.title("Learning Curves")
plt.show()