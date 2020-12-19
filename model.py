import keras
import settings
import numpy as np

class Model:
    def __init__(self):
        """Przygotowanie wyuczonego modelu."""
        self.model = keras.models.load_model(settings.model_dir)

    def predict(self, sample_text):
        prediction = self.model.predict(np.array([sample_text]))
        return float(prediction)