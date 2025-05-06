import tensorflow as tf

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