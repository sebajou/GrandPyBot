import requests
from GrandPyBotApp.functions.Parse import Parser


class TheWikiMediaParseCom(Parser):
    """ This class parse message from front input from user and return it to the Media Wiki API"""

    @staticmethod
    def get_title_from_api(message_to_api):
        """API Get search to obtain a json with title for next extract from other API request"""
        the_url = "https://fr.wikipedia.org/w/api.php"

        the_params = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": message_to_api
        }

        r_object = requests.get(url=the_url, params=the_params)

        media_wiki_request_search_result = r_object.json()

        return media_wiki_request_search_result

    @staticmethod
    def get_extract_from_api(title):
        """API Get extract from WikiMedia API"""
        the_url = "https://fr.wikipedia.org/w/api.php"
        the_title = title
        the_params = {
            "action": "query",
            "prop": "extracts",
            "exsentences": "10",
            "exlimit": "1",
            "titles": the_title,
            "explaintext": "1",
            "format": "json"
        }

        r = requests.get(url=the_url, params=the_params)
        extract = r.json()

        return extract

    @staticmethod
    def json_title(media_wiki_request_search_result):
        """Load media_wiki_request_search_result in a subscriptable objet: a json"""
        try:
            return_results = media_wiki_request_search_result['query']['search'][0]['title']
        except (UnboundLocalError, IndexError, TypeError):
            print("No result on media wiki")
            return "Atlantide"
        except KeyError:
            return "Empty request"

        return return_results

    @staticmethod
    def json_extract(media_wiki_request_extract_result):
        """Extract extract Wikipedia data from json"""
        # Loop in Wiki media API json results from request for extract text Wiki.
        # media_wiki_request_extract_result = json.loads(media_wiki_request_extract_result.read().decode("utf8"))
        string_extract = ""
        # Loop in Wiki media API json results from request for title.
        for json_content in media_wiki_request_extract_result["query"]['pages']:
            for json_content2 in media_wiki_request_extract_result["query"]['pages'][json_content]:
                if json_content2 == 'extract':
                    string_extract = media_wiki_request_extract_result["query"]['pages'][json_content][json_content2]

        return string_extract
