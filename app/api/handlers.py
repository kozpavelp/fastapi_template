from fastapi import APIRouter, Depends
from app.schemas.schemas import ResultResponse
from app.services.ml_service import predict_text as predict_text_service, get_results as get_results_service

router = APIRouter(prefix="/api", tags=["api"])


@router.get("")  # Если указывать путь, то он будет относительным префикса роутера.
async def get_hello(name: str):  # Валидация входных данных
    return {"message": "Hello, " + name}


@router.post("/predict")
async def predict_text(text_service=Depends(predict_text_service)):
    return text_service


@router.get("/results", response_model=list[ResultResponse])
async def get_results(results_service=Depends(get_results_service)):
    return results_service
