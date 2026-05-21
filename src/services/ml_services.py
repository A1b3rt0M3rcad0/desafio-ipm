"""Serviço de predição do modelo ML com execução em thread pool."""

from src.ml.scaler import SCALER
from src.ml.model import MODEL
from typing import List
import numpy as np
from pydantic import BaseModel
from concurrent.futures import ThreadPoolExecutor
import asyncio

class MLInputPredictionDTO(BaseModel):
    a:int
    b:int

class MLOutputPredictionDTO(BaseModel):
    message:str
    prediction:int

_executor = ThreadPoolExecutor(max_workers=4)

class MLPredictionService:
    def __init__(self):
        self.__scaler = SCALER
        self.__model = MODEL
        self.__executor = _executor

    async def execute(self, data: MLInputPredictionDTO) -> MLOutputPredictionDTO:
        """Executa a predição em thread separada para não bloquear o event loop."""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(self.__executor, self.__predict_sync, data)

    def __predict_sync(self, data: MLInputPredictionDTO) -> MLOutputPredictionDTO:
        """Aplica o scaler e executa a predição de forma síncrona."""
        data_array = np.array([[data.a, data.b]])
        scaled_data = self.__scaler.scale(X=data_array)
        prediction = self.__model.predict(scaled_data)
        result = prediction.tolist()[0]
        return MLOutputPredictionDTO(message="Is Positive" if result > 0 else "Is Negative", prediction=result)

if __name__ == "__main__":

    async def main():
        service = MLPredictionService()
        input_data = MLInputPredictionDTO(a=5, b=3)
        prediction = await service.execute(input_data)
        print(f"Predicted class: {prediction}")

    asyncio.run(main())
    asyncio.run(main())
    asyncio.run(main())
    asyncio.run(main())
    asyncio.run(main())
    asyncio.run(main())
    asyncio.run(main())