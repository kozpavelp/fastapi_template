import uvicorn
from fastapi import FastAPI
from app.api.handlers import router as predict_router

app = FastAPI()

"""
origins: list[str] = [
    "http://localhost",
    "http://localhost:3000"
]

allow_methods: list[str] = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]

allow_headers: list[str] = [
    "content-type",
    "authorization",
    "Set-Cookie",
    "Access-Control-Allow-Origin",
    "Access-Control-Allow-Headers"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=allow_methods,
    allow_headers=allow_headers
)
"""


app.include_router(predict_router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)
