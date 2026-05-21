"""Carregamento do MinMaxScaler e transformação de dados."""

from joblib import load
import numpy as np
from pathlib import Path

class Scaler:

    def __init__(self, model_path:Path) -> None:
        """Carrega o scaler a partir do arquivo joblib no caminho especificado."""
        self.model = load(model_path)

    def scale(self, X: np.ndarray) -> np.ndarray:
        """Aplica a transformação de escala nos dados de entrada."""
        return self.model.transform(X)

SCALER = Scaler(Path(__file__).parent.parent.parent/ "models" / 'scaler.joblib')