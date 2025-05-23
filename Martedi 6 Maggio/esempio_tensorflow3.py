import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt


# Caricamento del dataset (già suddiviso in train e test)
fashion_mnist = tf.keras.datasets.fashion_mnist.load_data()
(X_train_full, y_train_full), (X_test, y_test) = fashion_mnist

# Suddivisione in training e validation set
X_train, y_train = X_train_full[:-5000], y_train_full[:-5000]
X_valid, y_valid = X_train_full[-5000:], y_train_full[-5000:]

X_train = X_train / 255.0
X_valid = X_valid / 255.0
X_test = X_test / 255.0

class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
"Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

print(f"First training label corresponds to: {class_names[y_train[0]]}")


tf.random.set_seed(42)

model = tf.keras.Sequential()
model.add(tf.keras.layers.Input(shape=[28, 28]))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(300, activation="relu"))
model.add(tf.keras.layers.Dense(100, activation="relu"))
model.add(tf.keras.layers.Dense(10, activation="softmax"))

model.summary()

model.compile(
loss="sparse_categorical_crossentropy",
optimizer="sgd",
metrics=["accuracy"]
)

history = model.fit(
X_train, y_train,
epochs=30,
validation_data=(X_valid, y_valid)
)

pd.DataFrame(history.history).plot(
figsize=(8, 5), xlim=[0, 29], ylim=[0, 1], grid=True,
xlabel="Epoch", style=["r--", "r--.", "b-", "b-*"]
)
plt.title("Learning Curves")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.show()