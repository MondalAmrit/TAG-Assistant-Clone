import csv, random

ActionMap = ['SetAlarm', 'StopAlarm', 'StartStopwatch', 'StopStopwatch', 'SetTimer', 'StopTimer', 'ShowCompass', 'TurnOnTorch', 'TurnOffTorch']
IntentName = "Tool"

def generate_dataset(split=0.9):
    """Generates the dataset"""
    return generate_synthetic_dataset(split=split)

def create_examples(queries, SlotValues, TAG, split=0.9):
    """Creates dataset for the given actions based on queries and Slot Values"""
    if TAG not in ActionMap:
        print('This is not a valid TAG name: ', TAG)
        return
    dataset = []
    for q in queries:
        for sv in SlotValues:
            dataset.append([q,f'{IntentName} {TAG}',sv])
    split_idx = int(len(dataset) * split)
    random.shuffle(dataset)
    return [dataset[:split_idx], dataset[split_idx:]]

def generate_synthetic_dataset(split=0.9):
    """Write down your synthetic examples here"""
    dataset = [[], []]

    # SetAlarm
    queries = [
        "Set an alarm for {Time}", "Please set an alarm for {Time}", "Can you set an alarm for {Time}",
        "Wake me up at {Time}", "Alarm for {Time}", "Set alarm at {Time}", "Set the alarm to {Time}",
        "Schedule an alarm for {Time}", "I need an alarm at {Time}", "Set my alarm for {Time}"
    ]
    times = ["7 AM", "6:30 AM", "5 PM", "8 AM", "9 PM"]
    r = [{"Time": i} for i in times]
    res = create_examples(queries, r, 'SetAlarm', split=0.9)
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # StopAlarm
    queries = [
        "Stop the alarm", "Please stop the alarm", "Can you stop the alarm", "Turn off the alarm", "Disable the alarm",
        "Stop the alarm now", "Turn off the alarm now", "Can you disable the alarm", "Please turn off the alarm",
        "Stop my alarm"
    ]
    r = [{}]
    res = create_examples(queries, r, 'StopAlarm', split=0.9)
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # StartStopwatch
    queries = [
        "Start the stopwatch", "Please start the stopwatch", "Can you start the stopwatch", "Start the timer",
        "Begin the stopwatch", "Initiate the stopwatch", "Start my stopwatch", "Can you initiate the stopwatch",
        "Please begin the stopwatch", "Start the stopwatch now"
    ]
    r = [{}]
    res = create_examples(queries, r, 'StartStopwatch', split=0.9)
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # StopStopwatch
    queries = [
        "Stop the stopwatch", "Please stop the stopwatch", "Can you stop the stopwatch", "End the stopwatch",
        "Halt the stopwatch", "Terminate the stopwatch", "Stop my stopwatch", "Can you halt the stopwatch",
        "Please end the stopwatch", "Stop the stopwatch now"
    ]
    r = [{}]
    res = create_examples(queries, r, 'StopStopwatch', split=0.9)
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # SetTimer
    queries = [
        "Set a timer for {Duration}", "Please set a timer for {Duration}", "Can you set a timer for {Duration}",
        "Timer for {Duration}", "Set timer for {Duration}", "Set the timer to {Duration}",
        "Schedule a timer for {Duration}", "I need a timer for {Duration}", "Set my timer for {Duration}",
        "Set the timer for {Duration}"
    ]
    durations = ["5 minutes", "10 minutes", "30 seconds", "1 hour", "15 minutes"]
    r = [{"Duration": i} for i in durations]
    res = create_examples(queries, r, 'SetTimer', split=0.9)
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # StopTimer
    queries = [
        "Stop the timer", "Please stop the timer", "Can you stop the timer", "Turn off the timer", "Disable the timer",
        "Stop the timer now", "Turn off the timer now", "Can you disable the timer", "Please turn off the timer",
        "Stop my timer"
    ]
    r = [{}]
    res = create_examples(queries, r, 'StopTimer', split=0.9)
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # ShowCompass
    queries = [
        "Show me the compass", "Please show me the compass", "Can you show me the compass", "Open the compass",
        "Display the compass", "Show the compass", "Open my compass", "Can you display the compass",
        "Please open the compass", "Show the compass now"
    ]
    r = [{}]
    res = create_examples(queries, r, 'ShowCompass', split=0.9)
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # TurnOnTorch
    queries = [
        "Turn on the torch", "Please turn on the torch", "Can you turn on the torch", "Switch on the torch",
        "Activate the torch", "Light the torch", "Turn on my torch", "Can you activate the torch",
        "Please switch on the torch", "Turn the torch on now"
    ]
    r = [{}]
    res = create_examples(queries, r, 'TurnOnTorch', split=0.9)
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    # TurnOffTorch
    queries = [
        "Turn off the torch", "Please turn off the torch", "Can you turn off the torch", "Switch off the torch",
        "Deactivate the torch", "Extinguish the torch", "Turn off my torch", "Can you deactivate the torch",
        "Please switch off the torch", "Turn the torch off now"
    ]
    r = [{}]
    res = create_examples(queries, r, 'TurnOffTorch', split=0.9)
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    return dataset[0], dataset[1]
