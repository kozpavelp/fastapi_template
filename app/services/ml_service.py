from transformers import pipeline

from app.dao.db_model_dao import DBModelDAO
from app.schemas.schemas import ResultResponse, TextRequest


class MLService:
    def __init__(self):
        self.model = pipeline("sentiment-analysis")

    def predict(self, text: str):
        result = self.model(text)[0]
        return {"label": result["label"], "confidence": result["score"]}


ml_service = MLService()


async def predict_text(request: TextRequest):
    """
    Функция для предсказания текста. Данные передаются на обработку,
    результат сохраняется в базе данных и возвращается пользователю.
    """
    prediction = ml_service.predict(request.text)
    data = {
        "name": request.text,
        "description": prediction["label"],
        "note": f"Confidence: {prediction['confidence']}"
    }
    await DBModelDAO.add_data(**data)
    return {**prediction, **data} # TODO можно убрать


async def get_results():
    """
    Функция для получения всех результатов предсказаний из базы данных.
    """
    results = await DBModelDAO.find_all()
    return [ResultResponse(
        label=result.description,
        confidence=float(result.note.split(": ")[1]),
        name=result.name,
        description=result.description
    ) for result in results]
