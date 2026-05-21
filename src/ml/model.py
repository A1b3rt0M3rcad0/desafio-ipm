"""Carregamento do modelo RandomForest e predição."""

from joblib import load
import numpy as np
from pathlib import Path

class Model:

    def __init__(self, model_path:Path) -> None:
        """Carrega o modelo a partir do arquivo joblib no caminho especificado."""
        self.model = load(model_path)

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Retorna a predição do modelo para os dados de entrada."""
        return self.model.predict(X)
    
MODEL = Model(Path(__file__).parent.parent.parent/ "models" / 'random_forest_model.joblib')