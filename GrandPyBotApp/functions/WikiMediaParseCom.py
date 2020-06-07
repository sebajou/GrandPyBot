import requests
from GrandPyBotApp.functions.Parse import Parser


class TheWikiMediaParseCom(Parser):
    """ This class parse message from front input from user and return it to the Media Wiki API"""

    def get_title_from_api(self, message_to_api):
        # API Get search to obtain a json with title for next extract from other API request
        URL = "https://fr.wikipedia.org/w/api.php"

        PARAMS = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": message_to_api
        }

        r = requests.get(url=URL, params=PARAMS)
        title = r.json()

        return title

    def get_extract_from_api(self, title):
        # API Get extract from WikiMedia API
        URL = "https://fr.wikipedia.org/w/api.php"

        PARAMS = {
            "action": "query",
            "prop": "extracts",
            "exsentences": "10",
            "exlimit": "1",
            "titles": "Pralognan-la-Vanoise",
            "explaintext": "1",
            "format": "json"
        }

        r = requests.get(url=URL, params=PARAMS)
        extract = r.json()

        return extract
