import sys
import os

# Add the directory containing shared Python files to the module search path
shared_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Model'))
sys.path.append(shared_dir)

# This function is in the "/TAG-ASSISTANT-CLONE/Model/"
from get_models import get_gpt, get_bert_classification, get_bert_slot_filling

#####################################
# Works like a CMD from chat UI

intentMapIdxtoVal = {0: 'Week Day',
 1: 'Datetime',
 2: 'BasicChat',
 3: 'Logout',
 4: 'Sleep',
 5: 'Shutdown',
 6: 'Time Zone',
 7: 'Future Weather Forecast',
 8: 'Current Date',
 9: 'Geo Location',
 10: 'Brightness',
 11: 'Image Search',
 12: 'Product Search',
 13: 'Volume',
 14: 'YouTube Search',
 15: 'Open Website',
 16: 'Past Weather Forecast',
 17: 'Year',
 18: 'Current Weather Forecast',
 19: 'Music',
 20: 'TimeStamp',
 21: 'Restart',
 22: 'Battery',
 23: 'Current Time',
 24: 'Information'}

GPTmodel = get_gpt()
BERTmodel = get_bert_classification()
BERTSlotFilling = get_bert_slot_filling()

def check_cmd(query: str):
    # Check for calculation
    try:
        return  {'isResponse':True, 'response':eval(query.replace('x','*').replace('X','*'))}
    except:
        pass

    # Check for the function Command
    cmd = query.split()[0]
    if (cmd[0] != '@'):
        intent, p = BERTmodel.predict(query)
        intent = intentMapIdxtoVal[intent]
        print({"Query":query,'Intent':intent,"Probability":p})
        if intent == "BasicChat":
            return {'isResponse':True, 'response':GPTmodel.generate(query)}
        else:
            return {'isResponse':False, 'response':intent, 'args': BERTSlotFilling.predict(query)}
    else:
        # Execute the function.
        return {'isResponse':False, 'response': query.split()[0][1:], 'args': ''}
        # return f'{query.split()[0][0:]} is called'