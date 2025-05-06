from tensorflow import keras
from keras import layers
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

#Caricamento dataset
housing = fetch_california_housing()
X_train_full, X_test, y_train_full, y_test = train_test_split(
    housing.data, housing.target, random_state=42)
X_train, X_valid, y_train, y_valid = train_test_split(
    X_train_full, y_train_full, random_state=42)

#Normalization: adattamento PRIMA del grafo
normalization_layer = layers.Normalization()
normalization_layer.adapt(X_train)

#Layer e struttura manuale
hidden1 = layers.Dense(30, activation="relu")
hidden2 = layers.Dense(30, activation="relu")
concat_layer = layers.Concatenate()
outputlayer = layers.Dense(1)

#Input simbolico
input = layers.Input(shape=X_train.shape[1:])  # es. 8 feature

#Costruzione del grafo computazionale
normalized = normalization_layer(input)       # normalizzazione (dopo adapt)
h1 = hidden1(normalized)                       # primo hidden layer
h2 = hidden2(h1)                               # secondo hidden layer
concat = concat_layer([normalized, h2])        # percorso wide + deep
output = outputlayer(concat)                  # output finale

#Costruzione modello
model = keras.Model(inputs=[input], outputs=[output])

#Compilazione
model.compile(
    loss="mse",
    optimizer=keras.optimizers.Adam(learning_rate=2e-4),  # learning rate più basso per evitare overfitting
    metrics=["RootMeanSquaredError"]
)

#Addestramento
history1 = model.fit(
    X_train, y_train,
    epochs=40,
    validation_data=(X_valid, y_valid)
)

#Plot
pd.DataFrame(history1.history).plot(
    figsize=(8, 5), xlim=[0, 40], ylim=[0, 3], grid=True,
    xlabel="Epoch", style=["r--", "r--.", "b-", "b-*"]
)
plt.title("Learning Curves")
plt.show()

from pathlib import Path
from time import strftime
import tensorflow as tf

# Funzione per creare una directory unica per ogni esecuzione
def get_run_logdir(root_logdir="my_logs"):
    return Path(root_logdir) / strftime("run_%Y_%m_%d_%H_%M_%S")

run_logdir = get_run_logdir()

# Callback
tensorboard_cb = tf.keras.callbacks.TensorBoard(
log_dir=run_logdir,
profile_batch=(100, 200) # opzionale: profila solo i batch da 100 a 200
)

# Addestramento del modello
history = model.fit(
X_train, y_train,
epochs=30,
validation_data=(X_valid, y_valid),
callbacks=[tensorboard_cb]
)

