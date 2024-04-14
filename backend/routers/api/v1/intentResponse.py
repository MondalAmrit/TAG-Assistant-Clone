from fastapi import APIRouter
from pydantic import BaseModel
router = APIRouter()

class ArgsResponse(BaseModel):
    query_id: str
    arg: str
    value: str

@router.post('/api/v1/intentResponse',tags=['IntentResponse'])
def generate_reponse(query: str):
    return  {'result':'ok','response':'This endpoint will generate the reponses', 'input query':query}

@router.post('/api/v1/argsResponse')
def args_response(resp: ArgsResponse):
    return {'result':'ok','response':'This will handle the case where input is needed.', 'Your Input':resp}