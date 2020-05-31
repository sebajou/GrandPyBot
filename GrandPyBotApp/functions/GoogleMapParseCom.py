import string
import re
import requests
from GrandPyBotApp.functions.Parse import Parser
from GrandPyBotApp import app


GOOGLE_MAP_API_KEY = app.config['GOOGLE_MAP_API_KEY']


class TheGoogleMapParseCom(Parser):
    """ This class parse message from front input from user and return it to the Google Map API"""

    def send_message_to_api(message_to_api):
        url = 'https://maps.googleapis.com/maps/api/staticmap?center='+message_to_api+',CA&zoom=14&size=400x400&key='+GOOGLE_MAP_API_KEY
        req = requests.get(url)
        return req