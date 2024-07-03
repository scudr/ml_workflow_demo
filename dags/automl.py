from pycaret.classification import setup, compare_models, finalize_model, save_model, tune_model
import pandas as pd

class MLSystem:
    def __init__(self, data_path, target):
        self.data_path = data_path
        self.target = target
        self.model = None
        self.tuned_model = None

    def load_data(self):
        self.data = pd.read_csv(self.data_path)

    def train_model(self):
        exp = setup(data=self.data, 
                    target=self.target, 
                    session_id=123)
        best_model = compare_models()
        self.model = finalize_model(best_model)
        save_model(self.model, 'best_model')

    def tune_model(self):
        self.tuned_model = tune_model(self.model)
        save_model(self.tuned_model, 'best_model_tuned')

    def predict(self, data_path):
        data = pd.read_csv(data_path)
        predictions = self.tuned_model.predict(data) if self.tuned_model else self.model.predict(data)
        return predictions

if __name__ == "__main__":
    ml_system = MLSystem('train/train.csv', 'Target')
    ml_system.load_data()
    ml_system.train_model()
    ml_system.tune_model()


# from pycaret.classification import setup, compare_models, finalize_model, save_model
# import pandas as pd

# class MLSystem:
#     def __init__(self, data_path, target):
#         self.data_path = data_path
#         self.target = target
#         self.model = None

#     def load_data(self):
#         self.data = pd.read_csv(self.data_path)

#     def train_model(self):
#         exp = setup(data=self.data, 
#                     target=self.target, 
#                     session_id=123)
#         best_model = compare_models()
#         self.model = finalize_model(best_model)
#         save_model(self.model, 'best_model')

#     def predict(self, data_path):
#         data = pd.read_csv(data_path)
#         predictions = self.model.predict(data)
#         return predictions

# if __name__ == "__main__":
#     ml_system = MLSystem('train/train.csv', 'Target')
#     ml_system.load_data()
#     ml_system.train_model()
