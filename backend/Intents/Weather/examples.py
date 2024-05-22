#######################################
# Problem in Weather data
# It would be better if the weather actions will be based on the date rather than previous , current like things

import csv, re, random
# from protocol_activator import protocol_map_str

IntentMap = {
    "Current Weather Forecast" : 1,
    "Geo Location" : 2,
    "Past Weather Forecast" : 3,
    "Future Weather Forecast" : 4,
    "astronomy" : 5,
}
ActionMap = ['Current','Past','Future','GeoLocation','Astronomy']
IntentName = "Weather"

def generate_dataset(split = 0.9):
    """ Generates the dataset """
    #####################################
    # Actually this is not a correct method coz .csv is not considered.
    # But we can ignore it for now.
    # Open dataset.csv and get it's contents (Not done yet)
    
    # Add Synthetic data generation
    return generate_synthetic_dataset(split = split)

def create_examples( queries,SlotValues,TAG, split = 0.9 ):
    """ Creates dataset for the given actions based on queries and Slot Values """
    if TAG not in ActionMap:
        print('This is not a valid TAG name')
        return
    dataset = []
    for q in queries:
        for sv in SlotValues:
            dataset.append([q,f'{IntentName} {TAG}',sv])
    split_idx = int(len(dataset)*split)
    random.shuffle(dataset)
    return [dataset[:split_idx],dataset[split_idx:]]

def generate_synthetic_dataset(split = 0.9):
    """ Write down you synthetic examples here """
    dataset = [[],[]]
    # Current Weather Forecast
    queries = ['What is the current weather at {Location}', 'current weather status at {Location}', 'present weather condition in {Location}',
               'weather at {Location}','weather situation at {Location}','temperature at {Location}','heat at {Location}',
               'temperature in celsius at {Location}','temperature in fahrenheit at {Location}',
               'temperature in {Location}','humidity at {Location}','humidity in {Location}','moisture at {Location}',
               'wind speed at {Location}', 'Air Quality at {Location}', "today's weather at {Location} ?",
               'weather of {Location}', "{Location}'s weather", "weather of {Location} today", "{Location}'s weather report",
               "fetch me the weather report of {Location}", "give me the weather report of {Location}", 
               "why is it so hot in {Location}?", "why the weather changed suddenly at {Location}",
               "What's the current weather?", "Why don't you get the current wather of {Location}?",
               'Weather of {Location} on Friday', 'Weather of {Location} on Tuesday',
               "current weather forecase of {Location}"]
    tokens = ['New Delhi','delhi','Mumbai','Kolkata','Chennai','Bangloore','Moscow','New York','Shanghai','Tokyo',
                 'Pune','Hyderabad','Islamabad','Dhaka','columbo','Australia','India','Spain','Morocco',
                 'Paris','England','oslo','toronto','Agra','Lucknow','Muzafar nagar','vijayawada','Guntur',
                 'Vishakapatnam','Vellore','tirupati','jammu','kashmir','china','pakistan','egypt',
                 'isarel','saudi arabia']
    r = [{"Location":i} for i in tokens]
    res = create_examples( queries,r,'Current',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # Future Weather Forecast
    queries = ['tell me the future forecast of {Location}','future forecast of {Location}','future weather condition in {Location}',
               'next 3 days weather report of {Location}','tommorrow weather condition at {Location}',
               'tommorow temperature at {Location}','what would be the weather condition at {Location} tommorrow?',
               'give me the future forecast of {Location}', 'upcomming weather changes of {Location}',
               'Future Weather of {Location} on Friday', 'Future Weather of {Location} on Tuesday',
               "I need day after tommorrow's weather report for {Location}", "why don't you give me the future weather forecast for {Location}",
               "future weather forecast of {Location}"] 
    res = create_examples( queries,r,'Future',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # Past Weather Forecast
    queries = ['what is the weather condition at {Location}', 'previous weather condition in {Location}', 'past weather records of {Location}',
               'yesterday weather at {Location}','yesterday temperature at {Location}',
               'Past Weather of {Location} on Friday', 'Past Weather of {Location} on Tuesday',
               'yesterday humidity at {Location}', 'Can you fetch me the past weather report of {Location}',
               'previous weather forecast of {Location}', 'give me the details of previous weather condition at {Location}',
               ]
    res = create_examples( queries,r,'Past',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # Geo - location
    queries = ['get the co ordinates of {Location}', 'co-ords of {Location}','latitude and longitude of {Location}','location of {Location}',
               'geo location of {Location}', 'I need the co-ords of {Location}', 'where is {Location} located?',
               'I need the location of {Location}', 'find the location of {Location}', "{Location} location?"]
    res = create_examples( queries,r,'GeoLocation',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # Weather Report with date
    # queries = ['Weather on {Date}','What is the weather at {Location} on {Date}','weather of {Location} for {Date}',
    #            'Is the weather good on {Date}?','What will be the weather on {Date}']

    return dataset[0], dataset[1]