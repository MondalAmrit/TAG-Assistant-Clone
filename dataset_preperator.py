from Datasets.BasicChat.prepare import get_dataset as basic_chat_data
from Datasets.WeatherForecast.prepare import get_dataset as weather_data
# from Datasets.GITcommandHandler.prepare import get_dataset as git_data
import pprint, csv
dataset = basic_chat_data() + weather_data()

print(len(dataset),"\n")
pprint.pprint(dataset[:8])

with open('C://users/Anirudh/Desktop/TAG_dataset.csv','w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(dataset)

print('Dataset uploaded to')