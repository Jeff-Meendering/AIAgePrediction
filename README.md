# Age Prediction Model

## Overview
This project uses TensorFlow to create and utilize a neural network for predicting your age based on your age. This project contains two main scripts:

1. **Model Builder (`model_builder.py`)**: This script builds and trains a machine learning model on a sequence of ages.
2. **Model User (`model_user.py`)**: This script loads the trained model and uses it to make age predictions based on user input.

## Requirements
- Python 3.x
- TensorFlow 2.x
- NumPy

## Setup

### Requirements

1. Python 3.x

### Installation

- ***Create and activate a virtual environment:***
   
   - For Windows
   ``` bash
    python -m venv venv
    .\venv\Scripts\activate
   ```

   - Fore macOS and Linux

    ``` bash
    python3 -m venv venv
    source venv/bin/activate
    ```
- Install required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Training the Model

To train the model, run the **model_builder.py** script. This script will train a model to learn the mapping of ages to themselves (identity mapping) which serves as a simple demonstration of using neural networks. The trained model will be saved as **age_model.keras**.

Run the command:

``` bash
python model_builder.py
```

### Predicting Ages

After training the model, you can use the model_user.py script to predict ages based on the input. The script will prompt you to enter an age, and it will output the predicted age.

To start predicting ages, run:

``` bash
python model_user.py
```

### Example
``` bash
Enter your age: 30
Predicted age for 30 is: 30.0
```
