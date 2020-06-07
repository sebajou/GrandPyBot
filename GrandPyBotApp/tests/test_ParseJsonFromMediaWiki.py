import requests
import GrandPyBotApp.functions.ParseJsonFromMediaWiki as script
import GrandPyBotApp.functions.WikiMediaParseCom as script2
import json


def test_json_parser(monkeypatch):
    # Do mock to mock API Wiki Media message: 2 mock, one for title search, one for extract.
    # mock1: https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch=port+vieux+marseille&format=json
    media_wiki_request_result = {"batchcomplete": "", "continue": {"sroffset": 10, "continue": "-||"},
                                 "query": {"searchinfo": {"totalhits": 158}, "search": [
                                     {"ns": 0, "title": "Pralognan-la-Vanoise", "pageid": 586449, "size": 45575,
                                      "wordcount": 4586,
                                      "snippet": "Pour les articles homonymes, voir Vanoise. <span class=\"searchmatch\">Pralognan</span>-la-Vanoise est une commune fran\u00e7aise situ\u00e9e dans le d\u00e9partement de la Savoie, en r\u00e9gion Auvergne-Rh\u00f4ne-Alpes",
                                      "timestamp": "2020-05-06T09:06:02Z"},
                                     {"ns": 0, "title": "Hockey Courchevel M\u00e9ribel Pralognan",
                                      "pageid": 2991927, "size": 7450, "wordcount": 379,
                                      "snippet": "M\u00e9ribel <span class=\"searchmatch\">Pralognan</span> (HCMP) est un club fran\u00e7ais de hockey sur glace bas\u00e9 en Savoie et regroupant trois municipalit\u00e9s\u00a0: Courchevel, M\u00e9ribel et <span class=\"searchmatch\">Pralognan</span>-la-Vanoise",
                                      "timestamp": "2020-04-15T07:33:34Z"},
                                     {"ns": 0, "title": "Doron de Pralognan", "pageid": 6399507, "size": 2780,
                                      "wordcount": 267,
                                      "snippet": "Quelles sources sont attendues\u00a0? Comment ajouter mes sources\u00a0? Le Doron de <span class=\"searchmatch\">Pralognan</span> est une rivi\u00e8re fran\u00e7aise de Savoie, dans le massif de la Vanoise. Elle",
                                      "timestamp": "2018-11-03T00:04:48Z"},
                                     {"ns": 0, "title": "Lac des Vaches", "pageid": 10416661, "size": 5808,
                                      "wordcount": 546,
                                      "snippet": "(Canada). Le lac des Vaches est un lac situ\u00e9 en France sur la commune de <span class=\"searchmatch\">Pralognan</span>-la-Vanoise, dans le d\u00e9partement de la Savoie en r\u00e9gion Auvergne-Rh\u00f4ne-Alpes",
                                      "timestamp": "2019-06-23T08:02:38Z"},
                                     {"ns": 0, "title": "Cassandre (s\u00e9rie t\u00e9l\u00e9vis\u00e9e)",
                                      "pageid": 9456207, "size": 40169, "wordcount": 3510,
                                      "snippet": "Malinowski\u00a0: Jules Tournage\u00a0: en septembre et octobre 2017 notamment \u00e0 <span class=\"searchmatch\">Pralognan</span>-la-Vanoise et au col de la Chambotte. R\u00e9alisation\u00a0: \u00c9ric Le Roux Sc\u00e9nario\u00a0:",
                                      "timestamp": "2020-05-23T21:45:40Z"},
                                     {"ns": 0, "title": "Massif de la Vanoise", "pageid": 99158, "size": 15183,
                                      "wordcount": 1870,
                                      "snippet": "Vanoise. Ensuite, par extension, il s'organisait autour de la commune de <span class=\"searchmatch\">Pralognan</span>-la-Vanoise, et du Doron, la rivi\u00e8re qui la traverse, ainsi que ses affluents",
                                      "timestamp": "2020-03-02T14:10:37Z"},
                                     {"ns": 0, "title": "Gli\u00e8re (Savoie)", "pageid": 10219306, "size": 3956,
                                      "wordcount": 329,
                                      "snippet": "torrent situ\u00e9 en France dans le massif de la Vanoise sur la commune de <span class=\"searchmatch\">Pralognan</span>-la-Vanoise, dans le d\u00e9partement de la Savoie. Le torrent de la Gli\u00e8re",
                                      "timestamp": "2018-07-27T18:04:30Z"},
                                     {"ns": 0, "title": "Refuge du Roc de la P\u00eache", "pageid": 3417451,
                                      "size": 4723, "wordcount": 544,
                                      "snippet": "d\u00e9partement de la Savoie en r\u00e9gion Auvergne-Rh\u00f4ne-Alpes sur la commune de <span class=\"searchmatch\">Pralognan</span>. Ce refuge a \u00e9t\u00e9 construit en 1996 sur un ancien alpage tenu par des moines",
                                      "timestamp": "2020-05-25T17:35:16Z"},
                                     {"ns": 0, "title": "Col de la Vanoise", "pageid": 928898, "size": 10057,
                                      "wordcount": 1290,
                                      "snippet": "parc national de la Vanoise. Il permet l'acc\u00e8s entre les localit\u00e9s de <span class=\"searchmatch\">Pralognan</span>-la-Vanoise et Termignon, appartenant respectivement aux vall\u00e9es de la",
                                      "timestamp": "2018-03-31T16:15:23Z"},
                                     {"ns": 0, "title": "Aiguille de la Vanoise", "pageid": 1048095, "size": 4465,
                                      "wordcount": 404,
                                      "snippet": "L'aiguille de la Vanoise est un sommet du massif de la Vanoise dominant <span class=\"searchmatch\">Pralognan</span>-la-Vanoise. Elle est r\u00e9put\u00e9e pour sa grande face nord de 300 \u00e0 400 m de",
                                      "timestamp": "2020-04-19T16:28:46Z"}]}}

    class MockSearchResponse:

        def read(self):
            results_string = json.dumps(media_wiki_request_result)
            results_bytes = results_string.encode()
            return results_bytes

    def mock_json_return_from_wiki_api(media_wiki_request_search_result):
        response = MockSearchResponse()
        return response

    monkeypatch.setattr('GrandPyBotApp.functions.WikiMediaParseCom.TheWikiMediaParseCom.get_title_from_api',
                        mock_json_return_from_wiki_api)

    response = mock_json_return_from_wiki_api(media_wiki_request_result)

    assert script.ParseJson.json_title(response) == "Pralognan-la-Vanoise"
    # mock2: https://fr.wikipedia.org/w/api.php?action=query&prop=extracts&exsentences=10&exlimit=1&titles=Vieux-Port_de_Marseille&explaintext=1&formatversion=2

"""
    def setup_method(self):

        self.message_for_wiki_search_api = "pralognan"

    def test_return_from_wiki_api_title(self, monkeypatch):
        # For test parsed message to the front
"""



"""
    def setup_method(self):
        # For test parsed message to the front
        self.media_wiki_request_result = {"batchcomplete":"","continue":{"sroffset":10,"continue":"-||"},"query":{"searchinfo":{"totalhits":158},"search":[{"ns":0,"title":"Pralognan-la-Vanoise","pageid":586449,"size":45575,"wordcount":4586,"snippet":"Pour les articles homonymes, voir Vanoise. <span class=\"searchmatch\">Pralognan</span>-la-Vanoise est une commune fran\u00e7aise situ\u00e9e dans le d\u00e9partement de la Savoie, en r\u00e9gion Auvergne-Rh\u00f4ne-Alpes","timestamp":"2020-05-06T09:06:02Z"},{"ns":0,"title":"Hockey Courchevel M\u00e9ribel Pralognan","pageid":2991927,"size":7450,"wordcount":379,"snippet":"M\u00e9ribel <span class=\"searchmatch\">Pralognan</span> (HCMP) est un club fran\u00e7ais de hockey sur glace bas\u00e9 en Savoie et regroupant trois municipalit\u00e9s\u00a0: Courchevel, M\u00e9ribel et <span class=\"searchmatch\">Pralognan</span>-la-Vanoise","timestamp":"2020-04-15T07:33:34Z"},{"ns":0,"title":"Doron de Pralognan","pageid":6399507,"size":2780,"wordcount":267,"snippet":"Quelles sources sont attendues\u00a0? Comment ajouter mes sources\u00a0? Le Doron de <span class=\"searchmatch\">Pralognan</span> est une rivi\u00e8re fran\u00e7aise de Savoie, dans le massif de la Vanoise. Elle","timestamp":"2018-11-03T00:04:48Z"},{"ns":0,"title":"Lac des Vaches","pageid":10416661,"size":5808,"wordcount":546,"snippet":"(Canada). Le lac des Vaches est un lac situ\u00e9 en France sur la commune de <span class=\"searchmatch\">Pralognan</span>-la-Vanoise, dans le d\u00e9partement de la Savoie en r\u00e9gion Auvergne-Rh\u00f4ne-Alpes","timestamp":"2019-06-23T08:02:38Z"},{"ns":0,"title":"Cassandre (s\u00e9rie t\u00e9l\u00e9vis\u00e9e)","pageid":9456207,"size":40169,"wordcount":3510,"snippet":"Malinowski\u00a0: Jules Tournage\u00a0: en septembre et octobre 2017 notamment \u00e0 <span class=\"searchmatch\">Pralognan</span>-la-Vanoise et au col de la Chambotte. R\u00e9alisation\u00a0: \u00c9ric Le Roux Sc\u00e9nario\u00a0:","timestamp":"2020-05-23T21:45:40Z"},{"ns":0,"title":"Massif de la Vanoise","pageid":99158,"size":15183,"wordcount":1870,"snippet":"Vanoise. Ensuite, par extension, il s'organisait autour de la commune de <span class=\"searchmatch\">Pralognan</span>-la-Vanoise, et du Doron, la rivi\u00e8re qui la traverse, ainsi que ses affluents","timestamp":"2020-03-02T14:10:37Z"},{"ns":0,"title":"Gli\u00e8re (Savoie)","pageid":10219306,"size":3956,"wordcount":329,"snippet":"torrent situ\u00e9 en France dans le massif de la Vanoise sur la commune de <span class=\"searchmatch\">Pralognan</span>-la-Vanoise, dans le d\u00e9partement de la Savoie. Le torrent de la Gli\u00e8re","timestamp":"2018-07-27T18:04:30Z"},{"ns":0,"title":"Refuge du Roc de la P\u00eache","pageid":3417451,"size":4723,"wordcount":544,"snippet":"d\u00e9partement de la Savoie en r\u00e9gion Auvergne-Rh\u00f4ne-Alpes sur la commune de <span class=\"searchmatch\">Pralognan</span>. Ce refuge a \u00e9t\u00e9 construit en 1996 sur un ancien alpage tenu par des moines","timestamp":"2020-05-25T17:35:16Z"},{"ns":0,"title":"Col de la Vanoise","pageid":928898,"size":10057,"wordcount":1290,"snippet":"parc national de la Vanoise. Il permet l'acc\u00e8s entre les localit\u00e9s de <span class=\"searchmatch\">Pralognan</span>-la-Vanoise et Termignon, appartenant respectivement aux vall\u00e9es de la","timestamp":"2018-03-31T16:15:23Z"},{"ns":0,"title":"Aiguille de la Vanoise","pageid":1048095,"size":4465,"wordcount":404,"snippet":"L'aiguille de la Vanoise est un sommet du massif de la Vanoise dominant <span class=\"searchmatch\">Pralognan</span>-la-Vanoise. Elle est r\u00e9put\u00e9e pour sa grande face nord de 300 \u00e0 400 m de","timestamp":"2020-04-19T16:28:46Z"}]}}
        self.media_wiki_request_parsed = "Pralognan-la-Vanoise est une commune française située dans le département de la Savoie, en région Auvergne-Rhône-Alpes"

    def test_json_parser(self):

        json_parsed = script.ParseJson()
        assert json_parsed.json_parser(self.media_wiki_request_result) == self.media_wiki_request_parsed
"""

"""
>>> payload = {'key1': 'value1', 'key2': 'value2'}
>>> r = requests.get('https://httpbin.org/get', params=payload)

    class MockSearchResponse:
        def read(self):
            results_string = json.dumps(self.media_wiki_request_result)
            results_bytes = results_string.encode()
            return results_bytes

    def mock_json_return_from_wiki_api(self, media_wiki_request):
        return MockResponse()

    monkeypatch.setattr('script.ParseJson.json_parser', mock_json_return_from_wiki_api)
"""
