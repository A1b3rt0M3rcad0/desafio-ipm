from joblib import load
import numpy as np
from pathlib import Path

class Model:

    def __init__(self, model_path:Path) -> None:
        self.model = load(model_path)

    def predict(self, X: np.ndarray) -> np.ndarray:
        return self.model.predict(X)
    
MODEL = Model(Path(__file__).parent.parent.parent/ "models" / 'random_forest_model.joblib')