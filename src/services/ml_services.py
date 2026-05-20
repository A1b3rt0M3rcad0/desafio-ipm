from src.ml.scaler import SCALER
from src.ml.model import MODEL
from typing import List
import numpy as np
from pydantic import BaseModel

class MLInputPredictionDTO(BaseModel):
    input_data: List[List[int]]

class MLOutputPredictionDTO(BaseModel):
    predicted_class: List[int]

class MLPredictionService:
    def __init__(self):
        self.__scaler = SCALER
        self.__model = MODEL

    def execute(self, input_data: MLInputPredictionDTO) -> MLOutputPredictionDTO:
        data_array = np.array(input_data.input_data)
        scaled_data = self.__scaler.scale(X=data_array)
        prediction = self.__model.predict(scaled_data)
        return MLOutputPredictionDTO(predicted_class=prediction.tolist())

if __name__ == "__main__":
    # Example usage
    service = MLPredictionService()
    input_data = MLInputPredictionDTO(input_data=[[5, 3], [-200, 40]])
    prediction = service.execute(input_data)
    print(f"Predicted class: {prediction}")