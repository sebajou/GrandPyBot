import json


class ParseJson:
    """On back end Parse Json from API Media wiki."""

    @staticmethod
    def json_title(media_wiki_request_search_result):
        # Load media_wiki_request_search_result in a subscriptable objet: a json
        media_wiki_request_search_result = json.loads(media_wiki_request_search_result.read().decode("utf8"))
        # Wiki media API json results from request for title.
        return media_wiki_request_search_result['query']['search'][0]['title']

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
