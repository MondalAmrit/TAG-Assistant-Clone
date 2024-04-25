from backend.Intents.Chat.examples import get_dataset as chat_examples
from backend.Intents.Weather.examples import get_dataset as weather_examples
from backend.Intents.GIT.examples import get_dataset as git_examples
from backend.Intents.Internet.examples import get_dataset as internet_examples
from backend.Intents.Music.examples import get_dataset as music_examples
from backend.Intents.YouTube.examples import get_dataset as youtube_examples
from backend.Intents.System.examples import get_dataset as system_examples

import pprint, csv
data_list = [chat_examples(), weather_examples(), git_examples(), 
             internet_examples(), music_examples(), youtube_examples(), system_examples()]


dataset = {'train':[],'val':[]}
for i in data_list:
    dataset['train'].extend(i[0])
    dataset['val'].extend(i[1])

print(len(dataset['train']), len(dataset['val']),"\n")
pprint.pprint(dataset['train'][:4])
pprint.pprint(dataset['val'][:4])

for i in ('train','val'):
    with open(f'C://users/Anirudh/Desktop/TAG_dataset_{i}.csv','w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(dataset[i])

print('Dataset uploaded')