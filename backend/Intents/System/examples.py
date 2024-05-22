# from protocol_activator import protocol_map_str
import random
intentMap = {
    'Volume': 1,
    'Brightness' : 2,
    'System Down': 3,
    'Battery': 4,
    'Datetime':5,
}
ActionMap = ['Volume','Brightness','Shutdown','Sleep','Restart','Logout','Battery','Datetime']
IntentName = "System"

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
        print('This is not a valid TAG name: ',TAG)
        raise 'Invalid TAG Name'
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
    # Volume
    queries = ['can you set the volume to {Quantity}', 'make the volume to {Quantity}', 'put the volume at {Quantity}',
               'set the volume to {Quantity}','increase the volume by {Quantity}','change the volume by {Quantity}', 
            'up the volume by {Quantity}', 'decrease the volume by {Quantity}','change the volume by {Quantity}', 
            'drop the volume by {Quantity}','I think it is better to set the volume at {Quantity}',
            "why don't you leave the volume at {Quantity}","volume {Quantity}",
            "I want you to make the volume as {Quantity}", "I think its better to set the volume to {Quantity}",
            "I need the volume to stay at {Quantity}", "Why don't you set the volume to {Quantity}?",
            "Vol to {Quantity}", "{Quantity} volume.","I need volume to be {Quantity}"]
    tokens = [{"Quantity":str(i)} for i in range(101)]
    res = create_examples( queries,tokens,'Volume',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # Brightness
    queries = ['can you set the brightness to {Quantity}', 'make the brightness to {Quantity}', 'put the brightness at {Quantity}',
               'set the brightness to {Quantity}',
               'increase the brightness by {Quantity}','change the brightness by {Quantity}', 'up the brightness by {Quantity}',
               'decrease the brightness by {Quantity}','change the brightness by {Quantity}', 'drop the brightness by {Quantity}',
               'I think it is better to set the brightness at {Quantity}', "Why don't you set the brightness at {Quantity}?", "brightness {Quantity}",
               "I want you to make the brightness as {Quantity}", "make the brightness bar to {Quantity}",
               "brightness to {Quantity}", "{Quantity} brightness.","I need brightness to be {Quantity}"]
    res = create_examples( queries,tokens,'Brightness',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # Shutdown
    queries = ["Shut down the system", "Turn off the computer", "Power off the PC",
        "Shutdown the device", "Switch off the machine", "Close down the system",
        "Turn off the device", "Power off the computer", "Shutdown the PC",
        "Turn off the laptop", "Shutdown the laptop", "Power off the laptop",
        "I said Shut down the system", "Simply Shutdown", "shutdown","shut down",
        "Just shut down", "Just shutdown", "I want you to shutdown", "Why don't you shutdown?",
        "Stay off forever", "I need you to be offline forever"]
    tokens = [{}]
    res = create_examples( queries,tokens,'Shutdown',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # Sleep
    queries = ["Put the system to sleep", "Hibernate the computer", "Sleep the PC",
        "Put the computer to sleep", "Sleep the device", "Hibernate the PC",
        "Put the machine to sleep", "Hibernate the device", "Just put it to sleep",
        "Why don't you sleep", "Sleep", "sleep the system", "I want you to put the system to sleep",
        "Just simply sleep", "go to sleep","I want you to sleep"]
    res = create_examples( queries,tokens,'Sleep',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # Restart
    queries = ["Restart the system", "Reboot the computer", "Restart the PC",
        "Restart the device", "Reboot the machine", "Restart the laptop",
        "Reboot","Restart system", "I want you to restart", "Why don't you restart?",
        "Make the system go off and come back online", "off and on the system",
        "restart", "restart the system", "I want you to put the system to restart",
        "Just simply restart", "go to restart","I want you to restart"]
    res = create_examples( queries,tokens,'Restart',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # Logout
    queries = ["Log out from the system", "Logout from the computer", "Sign out from the PC",
        "Log out from the device", "Logout from the machine", "Sign out from the laptop",
        "Get me logged out from this device", "I need to logout", "logout",
        "Why don't you logout", "logout the system", "I want you to put the system to logout",
        "Just Simply logout", "go to logout","I want you to logout"]
    res = create_examples( queries,tokens,'Logout',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # Battery
    queries = ["Check battery percentage", "What's the battery level?", "Battery percentage",
        "How much charge is left?", "Battery status", "Show battery percentage",
        "Battery level", "Check remaining charge", "Percentage of battery left",
        "What's the charge level?", "Battery charge", "Remaining battery percentage",
        "Current battery level", "Battery percent", "How much battery is remaining?",
        "Check remaining battery time", "How much time left on battery?",
        "Battery time remaining", "Remaining battery time", "Battery time left",
        "Show battery time left", "Time left on battery", "Battery time",
        "What's the remaining battery time?", "Battery remaining time",
        "Remaining time on battery", "Battery time remaining",
        "How much time is left on the battery?", "Battery remaining charge time",
        "How much time do I have on my battery?", "Check charger status", "Is the charger plugged in?",
        "Charger plugged status", "Charger status", "Charger plugged",
        "Show charger status", "Is the laptop plugged in?", "Charger plugged in",
        "What's the charger status?", "Is the laptop charging?",
        "Is the laptop plugged into power?", "Is the charger connected?",
        "Show charger connection", "Power supply status", "Is the laptop on power?",
        "what's the battery?","How is the battery?","Battery stats","Battery","Get the whole info about battery",
        "I need full battery info","Any problem with battery?"
        ]
    res = create_examples( queries,tokens,'Battery',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # Date time (full datetime)
    queries = ["Get current date and time", "What's the current date and time?",
        "Current date and time", "Show current date and time", "Get today's date and time",
        "Display current date and time", "Current datetime", "Check date and time now",
        "Current time and date", "What time is it now?", "Show today's date and time",
        "Get the current time and date", "Time and date now", "What's the time and date?",
        "Current date time", "What's the time now?", "Check the current date and time",
        "Current system time and date", "Tell me the time and date now", "Now's date and time"]
    res = create_examples( queries,tokens,'Datetime',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])
    # Date time (current Date)
    queries = ["Get current date", "What's the current date?", "Current date",
        "Show current date", "Get today's date", "Display current date",
        "Check date now", "Today's date", "What's today's date?",
        "Show today's date", "Get the date now", "Today's day", "Current day",
        "What date is it today?", "Date today", "Tell me today's date",
        "Now's date"]    
    res = create_examples( queries,tokens,'Datetime',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])
    # Date time (current time)
    queries = ["Get current time", "What's the current time?", "Current time",
        "Show current time", "Check time now", "What time is it now?",
        "Tell me the time now", "Time now", "Display current time",
        "Check the time now", "What's the time?", "Now's time",
        "What's the time right now?", "Current system time", "Time right now",
        "Show system time", "System time now", "Time of the day",
        "Check the current time", "What time is it?"]    
    res = create_examples( queries,tokens,'Datetime',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])
    # Date time (timezone)
    queries = ["Get time zone", "What's the current time zone?", "Current time zone",
        "Show time zone", "Check time zone", "What time zone is it now?",
        "Time zone now", "Display current time zone", "Time zone",
        "Tell me the time zone now", "Current time zone info", "Now's time zone",
        "What's the timezone?", "System timezone", "Get the timezone now",
        "Show the system timezone", "Check system timezone", "Timezone information",
        "Current timezone", "Check current time zone"]    
    res = create_examples( queries,tokens,'Datetime',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])
    # Date time (timestamp)
    queries = ["Get timestamp", "What's the current timestamp?", "Current timestamp",
        "Show timestamp", "Check timestamp", "What's the timestamp now?",
        "Timestamp now", "Display current timestamp", "Get the current timestamp",
        "Tell me the timestamp now", "Current timestamp info", "Now's timestamp",
        "What's the timestamp?", "System timestamp", "Get the timestamp now",
        "Show the system timestamp", "Check system timestamp", "Timestamp information",
        "Current system timestamp", "Check current timestamp"]    
    res = create_examples( queries,tokens,'Datetime',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])
    # Date time (week day)
    queries = ["Get day of the week", "What's the day of the week today?",
        "Day of the week today", "Show day of the week", "Check day of the week now",
        "What day of the week is it now?", "Day of the week now", "Display day of the week",
        "Today's day of the week", "Tell me the day of the week now", "Day today",
        "Current day of the week", "What's today's day of the week?",
        "Now's day of the week", "What's the day today?", "System day of the week",
        "Check current day of the week", "Today's day", "Check today's day of the week",
        "What's today?"]    
    res = create_examples( queries,tokens,'Datetime',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])
    # Date time (Year)
    queries = ["Get current year", "What's the current year?", "Current year",
        "Show current year", "Check year now", "What year is it now?",
        "Year now", "Display current year", "Get the current year",
        "Tell me the year now", "Current year info", "Now's year",
        "What's the year?", "System year", "Get the year now",
        "Show the system year", "Check system year", "Year information",
        "Current system year", "Check current year", "Is this year 2024?"]    
    res = create_examples( queries,tokens,'Datetime',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    return dataset[0], dataset[1]