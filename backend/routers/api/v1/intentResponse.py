from fastapi import APIRouter
from pydantic import BaseModel
from cmd_executor import check_cmd
from action_executor import executor
router = APIRouter()

@router.post('/intentResponse',tags=['IntentResponse'])
def generate_reponse(query: dict):
    try:
        resp = check_cmd(query['query'])
        resp['status'] = True
        return resp
    except:
        return {'status': False, 'response':'Internal Server Error'}

@router.post('/executeIntent', tags=['Execute Intent'])
def execute_intent(query: dict):
    try:
        print(query)
        print('calling the intent ',query['query'])
        res = executor(query['query'],query['actionArgs'])
        return {'status': True, 'isResponse': res != None, 'response': res}
    except:
        return {'status': False, 'response': 'Internal Server Error'}