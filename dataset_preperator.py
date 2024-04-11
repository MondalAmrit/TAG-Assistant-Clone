# from Datasets.BasicChat.prepare import get_dataset
from Datasets.WeatherForecast.prepare import get_dataset

dataset = get_dataset()

print(len(dataset),"\n",dataset[:4])