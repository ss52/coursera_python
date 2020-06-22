import requests
import pprint
from dateutil.parser import parse


API_KEY = '27387f3bcd9017aa04ecae71a6e8c45e'


class OpenWeatherForecast:
    def get(self, city):
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}'
        res = requests.get(url).json()
        forecast_data = res['main']['feels_like']

        return forecast_data


class CityInfo:
    def __init__(self, city, weather_source=None):
        self.city = city
        self._OWF = weather_source or OpenWeatherForecast()

    def weather_forecast(self):
        forecast = self._OWF.get(self.city)
        return forecast


def _main():
    city_info = CityInfo("Saint Petersburg")
    forecast = city_info.weather_forecast()
    pprint.pprint(forecast)


if __name__ == '__main__':
    _main()
