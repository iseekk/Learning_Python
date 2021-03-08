class WeatherService:
    @staticmethod
    def barometer():
        """...some alien things happen in the background..."""
        pass


class Forecaster1:
    def __init__(self, weather_service):
        self.weather_service = weather_service

    def forecast(self):
        reading = self.weather_service.barometer()
        reply = {"rising": "It is going to rain",
                 "falling": "Looks clear",
                 }
        return reply[reading]


class Forecaster2:
    def __init__(self):
        self.weather_service = WeatherService()

    def forecast(self):
        reading = self.weather_service.barometer()
        reply = {"rising": "It is going to rain",
                 "falling": "Looks clear",
                 }
        return reply[reading]


class Forecaster3(WeatherService):

    def forecast(self):
        reading = self.barometer()
        reply = {"rising": "It is going to rain",
                 "falling": "Looks clear",
                 }
        return reply[reading]
