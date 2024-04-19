import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model('age_model.keras')
print('Model loaded')

def predict_age(input_age):
    return model.predict([np.array([input_age])]).flatten()[0]

if __name__ == "__main__":
    while True:
        try:
            input_age = float(input("Enter your age: "))
            predicted_age = predict_age(input_age)
            print(f"Predicted age for {input_age} is: {predicted_age:.1f}")
        except ValueError:
            print("Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nExiting program.")
            break