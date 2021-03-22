from fbchat import Client
from fbchat.models import *
from time import strftime
import configparser
import requests


class Config():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.cfg')
        self.login = config['credentials']['nickname']
        self.password = config['credentials']['password']
        self.conversation_id = config['settings']['conversation_id']
        self.api_key = config['openweathermap']['api_key']


class Bot(Client):
    conversation_id = Config().conversation_id

    def most(self):
        time = int(strftime('%H')+strftime('%M'))
        if 0000 <= time <= 1030 or 1100 <= time <= 1200 or 1300 <= time <= 1330 or 1430 <= time <= 1600 or 1730 <= time <= 2359:
            return "Most jest otwarty."
        else:
            return "Most jest zamknięty."

    def pogoda(self, city):
        api_key = Config().api_key
        params = {'q': city, 'APPID': api_key, 'units': 'metric'}
        r = requests.get(
            "https://api.openweathermap.org/data/2.5/weather", params)
        if r.status_code == 200:
            r_json = r.json()
            temp = r_json['main']['temp']
            status = r_json['weather'][0]['description']
            wind_speed = r_json['wind']['speed']
            return ("Pogoda w {}\r\n"
                    "Temperatura: {}°C\r\n"
                    "Status: {}\r\n"
                    "Prędkość wiatru {} m/s".format(city, temp, status, wind_speed))
        else:
            return "Something went wrong... correct command usage example: pogoda Gizycko,pl"

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        commands = {}
        self.markAsDelivered(thread_id, thread_type)
        msg = message_object.text.lower()
        print("{} said: {}".format(author_id, message_object.text))
        for command_name in dir(self):
            commands[command_name] = getattr(self, command_name)
        command, args = (msg.split(" ", 1) + [" "])[:2]
        if command in commands and author_id != self.uid:
            if len(args) > 1:
                self.send(Message(commands[command](
                    args)), thread_id=self.conversation_id)
            else:
                self.send(Message(commands[command]()),
                          thread_id=self.conversation_id)


if __name__ == "__main__":
    cfg = Config()
    bot = Bot(cfg.login, cfg.password)
    bot.listen()
