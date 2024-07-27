from pydantic import BaseModel


class TextRequest(BaseModel):
    text: str


class ResultResponse(BaseModel):
    label: str
    confidence: float
    name: str
    description: str
    