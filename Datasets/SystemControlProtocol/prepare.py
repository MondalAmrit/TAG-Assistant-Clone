import csv, re, random
from protocol_activator import protocol_map_str

intentMap = {
    'volume': 1,
    'brightness' : 2,
    'systemdown': 3,
    'battery': 4,
    'datetime':5,
}

def rephrase(l):
    patterns = {f'#{k}#':v for k,v in intentMap.items()}
    patterns['#PROTOCOL_CODE#'] = protocol_map_str['SystemControlProtocol']

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

def generate_data(val_list,prompts,generate_type = 'volume', inc = None):
    dataset = []
    for v in val_list:
        for p in prompts:
            dataset.append([p+str(v),f'<INTENT> {protocol_map_str["SystemControlProtocol"]} {intentMap[generate_type]} </INTENT> <PARAMS> qty={str(v)} </PARAMS> ' +
                            (f'inc={inc} </PARAMS> ' if inc and generate_type in ('volume','brightness') else '')])
    return dataset

def generate_single_data(lst,inp_type = None):
    dataset = []
    for i in lst:
        dataset.append([i,f'<INTENT> {protocol_map_str["SystemControlProtocol"]} {intentMap["datetime"]} </INENT> ' +
                        (f'<PARAMS> inp_type={inp_type} </PARAMS>' if inp_type else '')])
    return dataset

def getSyntheticData():
    dataset = []
    # Volume
    volume_levels = [0, 10, 20, 35, 30, 40, 50, 60, 70, 80, 90, 100]
    prompts = ['can you set the volume to ', 'make the volume to ', 'put the volume at ',
               'set the volume to ']
    dataset.extend(generate_data(volume_levels,prompts))
    volume_levels = [0,10,20,30]
    prompts = ['increase the volume by ','change the volume by ', 'up the volume by ']
    dataset.extend(generate_data(volume_levels,prompts, inc = 'Y'))
    volume_levels = [-10,-20,-30]
    prompts = ['decrease the volume by ','change the volume by ', 'drop the volume by ']
    dataset.extend(generate_data(volume_levels,prompts, inc = 'Y'))

    # Brightness
    volume_levels = [0, 10, 20, 35, 30, 40, 50, 60, 70, 80, 90, 100]
    prompts = ['can you set the brightness to ', 'make the brightness to ', 'put the brightness at ',
               'set the brightness to ']
    dataset.extend(generate_data(volume_levels,prompts, generate_type='brightness'))
    volume_levels = [0,10,20,30]
    prompts = ['increase the brightness by ','change the brightness by ', 'up the brightness by ']
    dataset.extend(generate_data(volume_levels,prompts, generate_type='brightness', inc = 'Y'))
    volume_levels = [-10,-20,-30]
    prompts = ['decrease the brightness by ','change the brightness by ', 'drop the brightness by ']
    dataset.extend(generate_data(volume_levels,prompts, generate_type='brightness', inc = 'Y'))

    # System Down
    prompts = [
        "Shut down the system", "Turn off the computer", "Power off the PC",
        "Shutdown the device", "Switch off the machine", "Close down the system",
        "Turn off the device", "Power off the computer", "Shutdown the PC",
        "Turn off the laptop", "Shutdown the laptop", "Power off the laptop"
    ]
    for i in prompts:
        dataset.append([i,f'<INTENT> {protocol_map_str["SystemControlProtocol"]} 3 </INTENT> <PARAMS> method=shutdown </PARAMS> <TEXT> Shutting Down </TEXT>'])
    prompts = [
        "Put the system to sleep", "Hibernate the computer", "Sleep the PC",
        "Put the computer to sleep", "Sleep the device", "Hibernate the PC",
        "Put the machine to sleep", "Hibernate the device"
    ]
    for i in prompts:
        dataset.append([i,f'<INTENT> {protocol_map_str["SystemControlProtocol"]} 3 </INTENT> <PARAMS> method=sleep </PARAMS> <TEXT> Sleeping </TEXT>'])
    prompts = [
        "Restart the system", "Reboot the computer", "Restart the PC",
        "Restart the device", "Reboot the machine", "Restart the laptop"
    ]
    for i in prompts:
        dataset.append([i,f'<INTENT> {protocol_map_str["SystemControlProtocol"]} 3 </INTENT> <PARAMS> method=restart </PARAMS> <TEXT> Restarting </TEXT>'])
    prompts = [
        "Log out from the system", "Logout from the computer", "Sign out from the PC",
        "Log out from the device", "Logout from the machine", "Sign out from the laptop"
    ]
    for i in prompts:
        dataset.append([i,f'<INTENT> {protocol_map_str["SystemControlProtocol"]} 3 </INTENT> <PARAMS> method=logout </PARAMS> <TEXT> Logging out </TEXT>'])

    # Battery
    prompts = [
        "Check battery percentage", "What's the battery level?", "Battery percentage",
        "How much charge is left?", "Battery status", "Show battery percentage",
        "Battery level", "Check remaining charge", "Percentage of battery left",
        "What's the charge level?", "Battery charge", "Remaining battery percentage",
        "Current battery level", "Battery percent", "How much battery is remaining?"
    ]
    for i in prompts:
        dataset.append([i,f'<INTENT> {protocol_map_str["SystemControlProtocol"]} 4 </INTENT> <PARAMS> spec="battery" </PARAMS>'])
    prompts = [
        "Check remaining battery time", "How much time left on battery?",
        "Battery time remaining", "Remaining battery time", "Battery time left",
        "Show battery time left", "Time left on battery", "Battery time",
        "What's the remaining battery time?", "Battery remaining time",
        "Remaining time on battery", "Battery time remaining",
        "How much time is left on the battery?", "Battery remaining charge time",
        "How much time do I have on my battery?"
    ]
    for i in prompts:
        dataset.append([i,f'<INTENT> {protocol_map_str["SystemControlProtocol"]} 4 </INTENT> <PARAMS> spec="time" </PARAMS>'])
    prompts = [
        "Check charger status", "Is the charger plugged in?",
        "Charger plugged status", "Charger status", "Charger plugged",
        "Show charger status", "Is the laptop plugged in?", "Charger plugged in",
        "What's the charger status?", "Is the laptop charging?",
        "Is the laptop plugged into power?", "Is the charger connected?",
        "Show charger connection", "Power supply status", "Is the laptop on power?"
    ]
    for i in prompts:
        dataset.append([i,f'<INTENT> {protocol_map_str["SystemControlProtocol"]} 4 </INTENT> <PARAMS> spec="charger" </PARAMS>'])
    prompts = ["what's the battery?","How is the battery?","Battery stats","Battery"]
    for i in prompts:
        dataset.append([i,f'<INTENT> {protocol_map_str["SystemControlProtocol"]} 4 </INTENT> <TEXT> </TEXT>'])
    
    # DateTime
    prompts = [
        "Get current date and time", "What's the current date and time?",
        "Current date and time", "Show current date and time", "Get today's date and time",
        "Display current date and time", "Current datetime", "Check date and time now",
        "Current time and date", "What time is it now?", "Show today's date and time",
        "Get the current time and date", "Time and date now", "What's the time and date?",
        "Current date time", "What's the time now?", "Check the current date and time",
        "Current system time and date", "Tell me the time and date now", "Now's date and time"
    ]
    dataset.extend(generate_single_data(prompts))
    promptse = [
        "Get current date", "What's the current date?", "Current date",
        "Show current date", "Get today's date", "Display current date",
        "Check date now", "Today's date", "What's today's date?",
        "Show today's date", "Get the date now", "Today's day", "Current day",
        "What date is it today?", "Date today", "Tell me today's date",
        "Now's date"
    ]
    dataset.extend(generate_single_data(prompts, inp_type='date'))
    prompts = [
        "Get current time", "What's the current time?", "Current time",
        "Show current time", "Check time now", "What time is it now?",
        "Tell me the time now", "Time now", "Display current time",
        "Check the time now", "What's the time?", "Now's time",
        "What's the time right now?", "Current system time", "Time right now",
        "Show system time", "System time now", "Time of the day",
        "Check the current time", "What time is it?"
    ]
    dataset.extend(generate_single_data(prompts, inp_type='time'))
    prompts = [
        "Get time zone", "What's the current time zone?", "Current time zone",
        "Show time zone", "Check time zone", "What time zone is it now?",
        "Time zone now", "Display current time zone", "Time zone",
        "Tell me the time zone now", "Current time zone info", "Now's time zone",
        "What's the timezone?", "System timezone", "Get the timezone now",
        "Show the system timezone", "Check system timezone", "Timezone information",
        "Current timezone", "Check current time zone"
    ]
    dataset.extend(generate_single_data(prompts, inp_type='zone'))
    prompts = [
        "Get timestamp", "What's the current timestamp?", "Current timestamp",
        "Show timestamp", "Check timestamp", "What's the timestamp now?",
        "Timestamp now", "Display current timestamp", "Get the current timestamp",
        "Tell me the timestamp now", "Current timestamp info", "Now's timestamp",
        "What's the timestamp?", "System timestamp", "Get the timestamp now",
        "Show the system timestamp", "Check system timestamp", "Timestamp information",
        "Current system timestamp", "Check current timestamp"
    ]
    dataset.extend(generate_single_data(prompts, inp_type='stamp'))
    prompts = [
        "Get day of the week", "What's the day of the week today?",
        "Day of the week today", "Show day of the week", "Check day of the week now",
        "What day of the week is it now?", "Day of the week now", "Display day of the week",
        "Today's day of the week", "Tell me the day of the week now", "Day today",
        "Current day of the week", "What's today's day of the week?",
        "Now's day of the week", "What's the day today?", "System day of the week",
        "Check current day of the week", "Today's day", "Check today's day of the week",
        "What's today?"
    ]
    dataset.extend(generate_single_data(prompts, inp_type='week'))
    prompts = [
        "Get current year", "What's the current year?", "Current year",
        "Show current year", "Check year now", "What year is it now?",
        "Year now", "Display current year", "Get the current year",
        "Tell me the year now", "Current year info", "Now's year",
        "What's the year?", "System year", "Get the year now",
        "Show the system year", "Check system year", "Year information",
        "Current system year", "Check current year"
    ]
    dataset.extend(generate_single_data(prompts, inp_type='year'))
    return dataset