from joblib import load
import numpy as np
from pathlib import Path

class Scaler:

    def __init__(self, model_path:Path) -> None:
        self.model = load(model_path)

    def scale(self, X: np.ndarray) -> np.ndarray:
        return self.model.transform(X)

SCALER = Scaler(Path(__file__).parent.parent.parent/ "models" / 'scaler.joblib')