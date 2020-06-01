import string
import re
import requests
from GrandPyBotApp.functions.Parse import Parser


class TheWikiMediaParseCom(Parser):
    """ This class parse message from front input from user and return it to the Media Wiki API"""

    def get_message_from_api(message_to_api):

        url = 'https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch='+message_to_api+'&format=json'
        req = requests.get(url)
        return req
