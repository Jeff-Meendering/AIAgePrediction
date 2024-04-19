import tensorflow as tf
import numpy as np

ages = np.array(range(1, 91), dtype=float)
true_ages = np.array(range(1, 91), dtype=float)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))

model.fit(ages, true_ages, epochs=100)

model.save("age_model.keras")

print("Finished training the model")
