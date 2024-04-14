from Datasets.BasicChat.prepare import get_dataset as basic_chat_data
from Datasets.WeatherForecast.prepare import get_dataset as weather_data
from Datasets.GITcommandHandler.prepare import get_dataset as git_data
from Datasets.InternetSearch.prepare import get_dataset as internet_data
from Datasets.MusicPlayer.prepare import get_dataset as music_data
from Datasets.YouTubeSearch.prepare import get_dataset as yt_data
from Datasets.SystemControlProtocol.prepare import get_dataset as sys_control_data

import pprint, csv
data_list = [basic_chat_data(), weather_data(), git_data(), internet_data(), music_data(), yt_data(), sys_control_data()]

dataset = {'train':[],'val':[]}
for i in data_list:
    dataset['train'].extend(i[0])
    dataset['val'].extend(i[1])

print(len(dataset['train']), len(dataset['val']),"\n")
pprint.pprint(dataset['train'][:8])
pprint.pprint(dataset['val'][:8])

for i in ('train','val'):
    with open(f'C://users/Anirudh/Desktop/TAG_dataset_{i}.csv','w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(dataset[i])

print('Dataset uploaded')