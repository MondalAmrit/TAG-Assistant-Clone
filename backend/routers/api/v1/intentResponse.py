from fastapi import APIRouter
from pydantic import BaseModel
from cmd_executor import check_cmd
router = APIRouter()

class ArgsResponse(BaseModel):
    query_id: str
    arg: str
    value: str

@router.post('/intentResponse',tags=['IntentResponse'])
def generate_reponse(query: dict):
    try:
        resp = check_cmd(query['query'])
        resp['status'] = True
        return resp
    except:
        return {'status': False, 'response':'Internal Server Error'}

@router.post('/argsResponse')
def args_response(resp: ArgsResponse):
    return {'status':True,'response':'This will handle the case where input is needed.', 'Your Input':resp}