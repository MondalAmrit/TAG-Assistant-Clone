import csv, re
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

def get_dataset(limit =  None):
    """
    Generates the dataset
    """
    dataset = []
    # Open dataset.csv and get it's contents
    with open('Datasets/WeatherForecast/dataset.csv') as f:
        reader = csv.reader(f)
        dataset = rephrase(list(reader)[:limit] if limit else list(reader))
    
    # Replace #PROTOCOL_CODE# and #<intent>#
    

    # Add Synthetic data generation
    if not (limit and len(dataset) < limit):
        dataset.extend(getSyntheticData())
    return dataset

def getSyntheticData():
    """
    Add Your Synthetic Data here and normal data in the csv file
    """
    dataset = []

    locations = ['New Delhi','delhi','Mumbai','Kolkata','Chennai','Bangloore','Moscow','New York','Shanghai','Tokyo']
    prompts = ['What is the current weather at ', 'current weather status at ', 'present weather condition in ',
               'weather at ']
    for l in locations:
        for p in prompts:
            # Text will not be displayed in this case as the results will be shown from the protocol
            dataset.append([p+l,f"<INTENT> {protocol_map_str['WeatherProtocol']} {IntentMap['current forecast']} </INTENT><PARAMS> {l} </PARAMS><TEXT></TEXT>"])

    propmts = ['tell me the future forecast of ','future forecast of ','future weather condition in ']
    for l in locations:
        for p in prompts:
            # Text will not be displayed in this case as the results will be shown from the protocol
            dataset.append([p+l,f"<INTENT> {protocol_map_str['WeatherProtocol']} {IntentMap['future forecast']} </INTENT><PARAMS> {l} </PARAMS><TEXT></TEXT>"])

    prompts = ['what is the weather condition at ', 'previous weather condition in ']
    for l in locations:
        for p in prompts:
            # Text will not be displayed in this case as the results will be shown from the protocol
            dataset.append([p+l,f"<INTENT> {protocol_map_str['WeatherProtocol']} {IntentMap['previous forecast']} </INTENT><PARAMS> {l} </PARAMS><TEXT></TEXT>"])

    prompts = ['get the co ordinates of ', 'co-ords of ','latitude and longitude of ','location of ']
    for l in locations:
        for p in prompts:
            # Text will not be displayed in this case as the results will be shown from the protocol
            dataset.append([p+l,f"<INTENT> {protocol_map_str['WeatherProtocol']} {IntentMap['geo location']} </INTENT><PARAMS> {l} </PARAMS><TEXT></TEXT>"])

    return dataset