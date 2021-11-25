import tensorflow as tf
from tensorflow import keras
import numpy as np
import NBADataService

class Model(object):

    x_train = NBADataService.
    y_train = NBADataService.

    def __init__(self, input_loss="sparse_categorical_crossentropy", input_optimizer="adam"):
        self.model = keras.models.Sequential([
            keras.layers.Dense(20, activation="relu"),
            keras.layers.Dense(20, activation="relu"),
            keras.layers.Dense(1, activation="sigmoid")
        ])
        self.model.compile(input_loss, input_optimizer, metrics="accuracy")

    def train(self, epochs=10):
        self.history = self.model.fit(x_train, y_train, epochs)

    def analyze_training(self):
        pd.DataFrame(self.history.history).plot(figsize=(16, 10))

    def make_prediction(self, away_team, home_team, year):
        #Make sure that the home_team and away_team formatting with the model is consistent.
        return f"{home_team} has a {model.predict(x_test)}% chance of winning"

    def save_model(self, file_path):
        self.model.save(file_path)

    def load_model(self, file_path):
        self.model = keras.models.load_model(file_path)