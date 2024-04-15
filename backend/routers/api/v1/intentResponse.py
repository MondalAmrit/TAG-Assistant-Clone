from fastapi import APIRouter
from pydantic import BaseModel
router = APIRouter()

class ArgsResponse(BaseModel):
    query_id: str
    arg: str
    value: str

@router.post('/intentResponse',tags=['IntentResponse'])
def generate_reponse(query: str):
    return {'result':'ok','response':'This endpoint will generate the reponses', 'prompt':query}

@router.post('/argsResponse')
def args_response(resp: ArgsResponse):
    return {'result':'ok','response':'This will handle the case where input is needed.', 'Your Input':resp}