import string
import numpy as np
from keras.models import load_model

class SignDetec(object):

    alphabets = string.ascii_lowercase
    MAP_LETTER =  {}

    for i, letter in enumerate(alphabets):
        MAP_LETTER[letter] = i
    MAP_LETTER = {v:k for k, v in MAP_LETTER.items()}

    def __init__(self, model_path):
        self.model = load_model(model_path)
        print("\nModelo Carregado!")

    def predict_sing(self, img):
        self.pred = self.model.predict(img)
        return SignDetec.MAP_LETTER[np.argmax(self.pred)]