# Fast API imports
from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse as res
from fastapi.requests import Request as req
from fastapi.middleware.cors import CORSMiddleware

# Router imports
from routers.api.v1 import intentResponse

app = FastAPI(title='TAG | Chatbot')

# CORS Settings
origins = [
    "http://localhost:5173"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(intentResponse.router, prefix='/api/v1', tags=['IntentResponse'])

@app.get('/')
def home_main():
    return "API is available at /api/v1/"