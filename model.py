import keras
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization
import tensorflow as tf
from tensorflow.keras import layers
import re
import string
import settings

def custom_standardization(input_data):
    lowercase = tf.strings.lower(input_data)
    stripped_html = tf.strings.regex_replace(lowercase, '<br />', ' ')
    return tf.strings.regex_replace(stripped_html,
                                    '[%s]' % re.escape(string.punctuation),
                                    '')

class Model:
    def __init__(self):
        """Przygotowanie modelu ML."""
        model = keras.models.load_model(settings.model_dir)
        max_features = 10000
        sequence_length = 250
        vectorize_layer = TextVectorization(
            standardize=custom_standardization,
            max_tokens=max_features,
            output_mode='int',
            output_sequence_length=sequence_length)
        self.model = tf.keras.Sequential([
            vectorize_layer,
            model,
            layers.Activation('sigmoid')
            ])

    def predict(self, text_to_predict):
        """Pobiera string, zwaraca prawdopodobieństwo, że jest to recenzja pozytywna."""
        return float(self.model.predict([text_to_predict]))