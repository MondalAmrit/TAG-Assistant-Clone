import csv, re, random
from protocol_activator import protocol_map_str

IntentMap = {
    "current forecast" : 1,
    "geo location" : 2,
    "previous forecast" : 3,
    "future forecast" : 4,
    "astronomy" : 5,
}

def rephrase(l):
    patterns = {f'#{k}#':v for k,v in IntentMap.items()}
    patterns['#PROTOCOL_CODE#'] = protocol_map_str['WeatherProtocol']

    for i in l:
        for k,v in patterns.items():
            i[1] = re.sub(k,str(v),i[1])
    return l

def get_dataset(split = 0.9, limit =  None):
    """
    Generates the dataset
    """
    dataset = []
    # Open dataset.csv and get it's contents
    with open('Datasets/WeatherForecast/dataset.csv') as f:
        reader = csv.reader(f)
        dataset = rephrase(list(reader)[:limit] if limit else list(reader))
    
    # Add Synthetic data generation
    if not (limit and len(dataset) < limit):
        dataset.extend(getSyntheticData())
        
    split_idx = int(split*len(dataset))
    random.shuffle(dataset)
    return dataset[:split_idx], dataset[split_idx:]

def get_data(locations,prompts,intent):
    dataset = []
    for l in locations:
        for p in prompts:
            dataset.append([p+l,f"<INTENT> {protocol_map_str['WeatherProtocol']} {IntentMap[intent]} </INTENT><PARAMS> location={l} </PARAMS>", f'WeatherProtocol {intent}'])
    return dataset

def getSyntheticData():
    """
    Add Your Synthetic Data here and normal data in the csv file
    """
    dataset = []

    locations = ['New Delhi','delhi','Mumbai','Kolkata','Chennai','Bangloore','Moscow','New York','Shanghai','Tokyo',
                 'Pune','Hyderabad','Islamabad','Dhaka','columbo','Australia','India','Spain','Morocco',
                 'Paris','England','oslo','toronto','Agra','Lucknow','Muzafar nagar','vijayawada','Guntur',
                 'Vishakapatnam','Vellore','tirupati','jammu','kashmir','china','pakistan','egypt',
                 'isarel','saudi arabia']
    
    # Current forecast prompts
    prompts = ['What is the current weather at ', 'current weather status at ', 'present weather condition in ',
               'weather at ','weather situation at ','temperature at ','heat at ',
               'temperature in celsius at ','temperature in fahrenheit at ',
               'temperature in ','humidity at ','humidity in ','moisture at ',
               'wind speed at ', 'Air Quality at ']
    dataset.extend(get_data(locations,prompts,'current forecast'))

    # Future forecast prompts
    prompts = ['tell me the future forecast of ','future forecast of ','future weather condition in ',
               'next 3 days weather report of ','tommorrow weather condition at ',
               'tommorow temperature at ',]
    dataset.extend(get_data(locations,prompts,'future forecast'))

    # previous forecast prompts
    prompts = ['what is the weather condition at ', 'previous weather condition in ', 'past weather records of ',
               'previous 3 days weather report of ','yesterday weather at ','yesterday temperature at ',
               'yesterday humidity at ']
    dataset.extend(get_data(locations,prompts,'previous forecast'))

    # geo location prompts
    prompts = ['get the co ordinates of ', 'co-ords of ','latitude and longitude of ','location of ',
               'geo location of ',]
    dataset.extend(get_data(locations,prompts,'geo location'))

    return dataset