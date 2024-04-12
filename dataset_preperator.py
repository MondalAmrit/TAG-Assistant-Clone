from Datasets.BasicChat.prepare import get_dataset as basic_chat_data
from Datasets.WeatherForecast.prepare import get_dataset as weather_data
import pprint, random
dataset = basic_chat_data() + weather_data()
random.shuffle(dataset)

print(len(dataset),"\n")
pprint.pprint(dataset[:4])
