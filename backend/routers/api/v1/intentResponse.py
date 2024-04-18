from fastapi import APIRouter
from pydantic import BaseModel
from ...Model.get_model import model
router = APIRouter()

class ArgsResponse(BaseModel):
    query_id: str
    arg: str
    value: str

@router.post('/intentResponse',tags=['IntentResponse'])
def generate_reponse(query: dict):
    return {'result':'ok','response':model.generate(query['query']), 'prompt':query['query']}

@router.post('/argsResponse')
def args_response(resp: ArgsResponse):
    return {'result':'ok','response':'This will handle the case where input is needed.', 'Your Input':resp}