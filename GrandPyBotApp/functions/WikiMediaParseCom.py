import requests
from GrandPyBotApp.functions.Parse import Parser
import json


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

    @staticmethod
    def json_title(media_wiki_request_search_result):
        # Load media_wiki_request_search_result in a subscriptable objet: a json
        chaine_bytes = media_wiki_request_search_result.read()
        chaine = chaine_bytes.decode("utf8")
        data = json.loads(chaine)
        # Wiki media API json results from request for title.
        return_results = data['query']['search'][0]['title']
        return return_results

    @staticmethod
    def json_extract(media_wiki_request_extract_result):
        # Loop in Wiki media API json results from request for extract text Wiki.
        media_wiki_request_extract_result = json.loads(media_wiki_request_extract_result.read().decode("utf8"))
        # Loop in Wiki media API json results from request for title.
        for json_content in media_wiki_request_extract_result["query"]['pages']:
            for json_content2 in media_wiki_request_extract_result["query"]['pages'][json_content]:
                if json_content2 == 'extract':
                    json_content3 = media_wiki_request_extract_result["query"]['pages'][json_content][json_content2]

        string_extract = json_content3

        return string_extract
