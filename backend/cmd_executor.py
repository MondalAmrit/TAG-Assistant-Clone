from Model.get_models import GPTmodel, BERTmodel, BERTSlotFilling

#####################################
# Works like a CMD from chat UI

intentMapIdxtoVal = {0: 'Current Weather Forecast',
 1: 'BasicChat',
 2: 'Logout',
 3: 'Product Search',
 4: 'YouTube Search',
 5: 'Year',
 6: 'Battery',
 7: 'Open Website',
 8: 'Datetime',
 9: 'TimeStamp',
 10: 'Information',
 11: 'Past Weather Forecast',
 12: 'Restart',
 13: 'Image Search',
 14: 'Sleep',
 15: 'Music',
 16: 'Week Day',
 17: 'Current Date',
 18: 'Current Time',
 19: 'Time Zone',
 20: 'Future Weather Forecast',
 21: 'Brightness',
 22: 'Geo Location',
 23: 'Volume',
 24: 'Shutdown'}

def check_cmd(query: str):
    # Check for calculation
    try:
        return eval(query.replace('x','*').replace('X','*'))
    except:
        pass

    # Check for the function Command
    cmd = query.split()[0]
    if (cmd[0] != '@'):
        intent = intentMapIdxtoVal[BERTmodel.predict(query.lower())]
        if intent == "BasicChat":
            return {'isResponse':True, 'response':GPTmodel.generate(query)}
        else:
            return {'isResponse':False, 'response':intent, 'args': BERTSlotFilling.predict(query)}
    else:
        # Execute the function.
        return {'isResponse':False, 'response': query.split()[0][1:], 'args': ''}
        # return f'{query.split()[0][0:]} is called'