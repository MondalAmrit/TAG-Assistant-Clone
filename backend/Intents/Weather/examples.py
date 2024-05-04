import csv, re, random
from protocol_activator import protocol_map_str

IntentMap = {
    "Current Weather Forecast" : 1,
    "Geo Location" : 2,
    "Past Weather Forecast" : 3,
    "Future Weather Forecast" : 4,
    "astronomy" : 5,
}

def get_dataset(split = 0.9, limit =  None):
    """ Generates the dataset """
    dataset = []
    # Open dataset.csv and get it's contents (Not done yet)
    
    # Add Synthetic data generation
    if not (limit and len(dataset) < limit):
        res = synthetic_examples_dataset(split = split)
        dataset[0].extend(res[0])
        dataset[1].extend(res[1])
        
    return dataset[0], dataset[1]

def create_examples( queries,tokens,TAG, split = 0.9 ):
    """ Creates dataset for the given actions based on queries and tokens """
    dataset = []
    for q in queries:
        for t in tokens:
            dataset.append([q.replace('#tkn#',t,1),TAG])
    split_idx = int(len(dataset)*split)
    return [dataset[:split_idx],dataset[split_idx:]]

def synthetic_examples_dataset(split = 0.9):
    """ Write down you synthetic examples here """
    dataset = []
    # Current Weather Forecast
    queries = ['What is the current weather at #tkn#', 'current weather status at #tkn#', 'present weather condition in #tkn#',
               'weather at #tkn#','weather situation at #tkn#','temperature at #tkn#','heat at #tkn#',
               'temperature in celsius at #tkn#','temperature in fahrenheit at #tkn#',
               'temperature in #tkn#','humidity at #tkn#','humidity in #tkn#','moisture at #tkn#',
               'wind speed at #tkn#', 'Air Quality at #tkn#',
               'weather of #tkn#', "#tkn#'s weather", "weather of #tkn# today", "#tkn#'s weather report",
               "fetch me the weather report of #tkn#", "give me the weather report of #tkn#", 
               "why is it so hot in #tkn#?", "why the weather changed suddenly at #tkn#"]
    tokens = ['New Delhi','delhi','Mumbai','Kolkata','Chennai','Bangloore','Moscow','New York','Shanghai','Tokyo',
                 'Pune','Hyderabad','Islamabad','Dhaka','columbo','Australia','India','Spain','Morocco',
                 'Paris','England','oslo','toronto','Agra','Lucknow','Muzafar nagar','vijayawada','Guntur',
                 'Vishakapatnam','Vellore','tirupati','jammu','kashmir','china','pakistan','egypt',
                 'isarel','saudi arabia']
    
    res = create_examples( queries,tokens,'Current Weather Forecast',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # Future Weather Forecast
    queries = ['tell me the future forecast of #tkn#','future forecast of #tkn#','future weather condition in #tkn#',
               'next 3 days weather report of #tkn#','tommorrow weather condition at #tkn#',
               'tommorow temperature at #tkn#','what would be the weather condition at #tkn# tommorrow?',
               'give me the future forecast of #tkn#', 'upcomming weather changes of #tkn#',
               "I need day after tommorrow's weather report for #tkn#", "why don't you give me the future weather forecast for #tkn#"] 
    res = create_examples( queries,tokens,'Future Weather Forecast',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # Past Weather Forecast
    queries = ['what is the weather condition at #tkn#', 'previous weather condition in #tkn#', 'past weather records of #tkn#',
               'previous 3 days weather report of #tkn#','yesterday weather at #tkn#','yesterday temperature at #tkn#',
               'yesterday humidity at #tkn#', 'Can you fetch me the past weather report of #tkn#',
               'previous weather forecast of #tkn#', 'give me the details of previous weather condition at #tkn#',
               ]
    res = create_examples( queries,tokens,'Past Weather Forecast',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # Geo - location
    queries = ['get the co ordinates of #tkn#', 'co-ords of #tkn#','latitude and longitude of #tkn#','location of #tkn#',
               'geo location of #tkn#', 'I need the co-ords of #tkn#', 'where is #tkn# located?',
               'I need the location of #tkn#', 'find the location of #tkn#',]
    res = create_examples( queries,tokens,'Geo Location',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])