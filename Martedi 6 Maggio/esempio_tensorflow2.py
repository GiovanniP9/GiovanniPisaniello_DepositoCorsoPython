import tensorflow as tf
tf.random.set_seed(42)

model = tf.keras.Sequential([
tf.keras.Input(shape=(28, 28)),
tf.keras.layers.Flatten(),
tf.keras.layers.Dense(300, activation="relu"),
tf.keras.layers.Dense(100, activation="relu"),
tf.keras.layers.Dense(10, activation="softmax")
])

model.summary()
