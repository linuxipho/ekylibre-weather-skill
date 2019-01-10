from mycroft import MycroftSkill, intent_file_handler


class EkylibreWeather(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('weather.ekylibre.intent')
    def handle_weather_ekylibre(self, message):
        self.speak_dialog('weather.ekylibre')


def create_skill():
    return EkylibreWeather()

