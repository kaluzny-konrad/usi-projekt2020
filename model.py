import keras
import settings
import numpy as np

class Model:
    """Klasa Model określająca czy opinia jest pozytywna czy negatywna."""
    def __init__(self):
        """Przygotowanie wyuczonego modelu."""
        self.model = keras.models.load_model(settings.model_dir)

    def predict(self, sample_text):
        """Przewiduje czy opinia jest pozytywna czy negatywna."""
        prediction = self.model.predict(np.array([sample_text]))
        return float(prediction)