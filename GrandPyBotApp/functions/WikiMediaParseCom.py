import string
import re
import requests
from GrandPyBotApp.functions.Parse import Parser


class TheWikiMediaParseCom(Parser):
    """ This class parse message from front input from user and return it to the Media Wiki API"""

    def get_title_from_api(self, message_to_api):
        # API Get search to obtain a json with title for next extract from other API request
        # https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch=port+vieux+marseille&format=json
        url = 'https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch='+message_to_api+'&format=json'
        req_title = requests.get(url)
        return req_title

    def get_extract_from_api(self, title):
        # API Get extract from WikiMedia API
        # https://fr.wikipedia.org/w/api.php?action=query&prop=extracts&exsentences=10&exlimit=1&titles=Vieux-Port_de_Marseille&explaintext=1&formatversion=2
        pass
