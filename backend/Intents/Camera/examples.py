###########################################################################################
# It would better if the implementation like click photo or start video will be implemented
import random
ActionMap = ['Photo','Video']
IntentName = "Camera"

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

    queries = ['Open the camera','I want you to open my mobile camera','Open the laptop camera',
               "Why don't you open the camera","I need to click a photo","take a selfie",
               "camera on","camera on please","It would be better if you can open the camera",
               "click a photo of mine","open the camera quickly I need to take a photo","Open the cam"]
    tokens = [{}]
    res = create_examples( queries,tokens,'Photo',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])

    queries = ['Open the camera video',"I want to shoot a video","Start recording a video",
               "Let's take a video of me","Open cam and switch to video",
               "It would be better if you can start the video recording",
               "Hey something interesting is happening. Open the camera quickly. I need to shoot the video"]
    tokens = [{}]
    res = create_examples( queries,tokens,'Video',split=0.9 )
    dataset[0].extend(res[0])
    dataset[1].extend(res[1])