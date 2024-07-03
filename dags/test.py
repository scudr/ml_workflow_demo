import unittest
from MLSystem import MLSystem  # Asegúrate de que la clase MLSystem está en el archivo MLSystem.py
import pandas as pd

class TestMLSystem(unittest.TestCase):

    def setUp(self):
        # Configuración antes de cada prueba
        self.ml_system = MLSystem('train/train.csv', 'Target')
        self.ml_system.load_data()

    def test_load_data(self):
        # Verificar que los datos se cargan correctamente
        self.assertIsNotNone(self.ml_system.data)
        self.assertIsInstance(self.ml_system.data, pd.DataFrame)

    def test_train_model(self):
        # Verificar que el modelo se entrena correctamente
        self.ml_system.train_model()
        self.assertIsNotNone(self.ml_system.model)

    def test_predict(self):
        # Verificar que se puede hacer una predicción
        self.ml_system.train_model()
        predictions = self.ml_system.predict('test/test.csv')
        self.assertIsNotNone(predictions)
        self.assertIsInstance(predictions, pd.Series)

if __name__ == '__main__':
    unittest.main()


