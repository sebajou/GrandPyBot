import GrandPyBotApp.functions.WikiMediaParseCom as script
import json


class TestParse:

    def setup_method(self):
        # For test parsed message to the front
        self.sentence_to_parse1 = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
        self.sentence_to_parse2 = "Que peux-tu me dire à propos de la gare de Lyon à Paris ?"
        self.sentence_to_parse3 = "Je voudrais aller au vieux port à Marseille, tu connais ?"
        self.sentence_to_parse4 = "Ah ! Venise, c'est tellement romantique, j'aimerais beaucoup y aller. "
        self.sentence_to_parse5 = "Cet été, je pars dans les Antilles. "
        self.sentence_to_parse6 = "Ma femme veut qu'on parte en vacances en Tunisie. Elle veut qu'on aille dans un " \
                                  "hôtel. "
        self.sentence_to_parse7 = "Je veux partir pour Hong-Kong !"
        self.sentence_to_parse8 = "GrandPyBot, dis-moi tout sur la Barbade. "
        self.sentence_to_parse9 = "Est-ce que tu es allé au Timor oriental ? "

        # For verify the good shape of message send for API request
        self.api_request_localisation = "pralognan"

        # Json for simulate media wiki title request result
        self.media_wiki_request_result = {"batchcomplete": "", "continue": {"sroffset": 10, "continue": "-||"},
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

        # Json for simulate the media wiki extract request result
        self.media_wiki_request_extract_result = {"batchcomplete": "", "query": {"pages": {
            "586449": {"pageid": 586449, "ns": 0, "title": "Pralognan-la-Vanoise",
                       "extract": "Pralognan-la-Vanoise  est une commune fran\u00e7aise situ\u00e9e dans le d\u00e9partement de la Savoie, en r\u00e9gion Auvergne-Rh\u00f4ne-Alpes. Village de montagne du massif de la Vanoise, en Tarentaise, il comptait 724 habitants en 2017.\nLe village est une station touristique d'\u00e9t\u00e9 et de sports d'hiver install\u00e9e au c\u0153ur du parc national de la Vanoise, proposant de nombreuses activit\u00e9s sportives de montagne, telles que la randonn\u00e9e (les sentiers de grande randonn\u00e9e GR 5 et GR 55 y passent) ou des via ferrata.\n\n\n== G\u00e9ographie ==\n\n\n=== Situation ===\nPralognan-la-Vanoise est la derni\u00e8re commune de la vall\u00e9e de Bozel (Tarentaise). Le centre du village, situ\u00e9 \u00e0 environ 1 400 m\u00e8tres d'altitude, s'\u00e9tablit au confluent des vall\u00e9es glaciaires de la Gli\u00e8re et de Chavi\u00e8re. Toutes deux constituent des points de passage vers la vall\u00e9e de la Maurienne par le col de la Vanoise (2 517 m\u00e8tres) ou le col de Chavi\u00e8re (2 796 m\u00e8tres).\n\n\n=== Communes limitrophes ===\n\n\n=== G\u00e9ologie et relief, hydrographie ===\n\nLe Doron de Pralognan \u2014 form\u00e9 en amont de diff\u00e9rents cours d'eau (torrent de la Gli\u00e8re, du Dard et nant de la Cr\u00e9p\u00e9na, puis du ruisseau d'Isertan) \u2014 et le Doron de Chavi\u00e8re se rejoignent dans la commune. En aval, il conflue avec le Doron de Champagny pour former le Doron de Bozel.\n\n\n=== Climat ===\nLa situation de Pralognan-la-Vanoise, d'une altitude d'environ 1 400 m, la place dans un milieu continental montagnard caract\u00e9ris\u00e9 par une humidit\u00e9 marqu\u00e9e. Les hivers sont plus froids et neigeux, et la saison estivale douce avec parfois des \u00e9pisodes orageux."}}}}

    def test_parse_message_from_front(self):
        # Also test limit : none, only stop word, blank string ...
        message_to_parse1 = self.sentence_to_parse1
        message_to_parse2 = self.sentence_to_parse2
        message_to_parse3 = self.sentence_to_parse3
        message_to_parse4 = self.sentence_to_parse4
        message_to_parse5 = self.sentence_to_parse5
        message_to_parse6 = self.sentence_to_parse6
        message_to_parse7 = self.sentence_to_parse7
        message_to_parse8 = self.sentence_to_parse8
        message_to_parse9 = self.sentence_to_parse9
        # Control that word in message_to_parse are present in a given list
        parse = script.TheWikiMediaParseCom()
        assert [word for word in parse.parse_message_from_front(message_from_front=message_to_parse1) if word in ["openclassrooms"]]
        assert [word for word in parse.parse_message_from_front(message_from_front=message_to_parse2) if word in ["gare", "lyon", "paris"]]
        assert [word for word in parse.parse_message_from_front(message_from_front=message_to_parse3) if word in ["vieux", "port", "marseille"]]
        assert [word for word in parse.parse_message_from_front(message_from_front=message_to_parse4) if word in ["venise"]]
        assert [word for word in parse.parse_message_from_front(message_from_front=message_to_parse5) if word in ["antilles"]]
        assert [word for word in parse.parse_message_from_front(message_from_front=message_to_parse6) if word in ["tunisie"]]
        assert [word for word in parse.parse_message_from_front(message_from_front=message_to_parse7) if word in ["hong-kong"]]
        assert [word for word in parse.parse_message_from_front(message_from_front=message_to_parse8) if word in ["barbade"]]
        assert [word for word in parse.parse_message_from_front(message_from_front=message_to_parse9) if word in ["timor", "oriental"]]

    def test_json_parser_search(self, monkeypatch):
        # Do mock to mock API Wiki Media message: 2 mock, one for title search, one for extract.
        # mock1: https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch=port+vieux+marseille&format=json
        media_wiki_request_result2 = self.media_wiki_request_result

        class MockSearchResponse:
            def read(self):
                results_string = json.dumps(media_wiki_request_result2)
                results_bytes = results_string.encode()
                return results_bytes

        def mock_json_return_from_wiki_api(media_wiki_request_search_result):
            response = MockSearchResponse()
            return response

        monkeypatch.setattr('GrandPyBotApp.functions.WikiMediaParseCom.TheWikiMediaParseCom.get_title_from_api',
                            mock_json_return_from_wiki_api)

        response = mock_json_return_from_wiki_api(self.media_wiki_request_result)

        json_title_rep = script.TheWikiMediaParseCom()

        assert json_title_rep.json_title(response) == "Pralognan-la-Vanoise"

    def test_json_parser_extract(self, monkeypatch):
        # mock2: https://fr.wikipedia.org/w/api.php?action=query&prop=extracts&exsentences=10&exlimit=1&titles=Pralognan-la-Vanoise&explaintext=1&format=json
        media_wiki_request_extract_result2 = self.media_wiki_request_extract_result

        class MockSearchResponse:
            def read(self):
                results_string = json.dumps(media_wiki_request_extract_result2)
                results_bytes = results_string.encode()
                return results_bytes

        def mock_json_return_from_wiki_api(media_wiki_request_extract_result):
            response = MockSearchResponse()
            return response

        monkeypatch.setattr('GrandPyBotApp.functions.WikiMediaParseCom.TheWikiMediaParseCom.get_extract_from_api',
                            mock_json_return_from_wiki_api)

        response = mock_json_return_from_wiki_api(media_wiki_request_extract_result2)

        assert script.TheWikiMediaParseCom.json_extract(response) == "Pralognan-la-Vanoise  est une commune fran\u00e7aise situ\u00e9e dans le d\u00e9partement de la Savoie, en r\u00e9gion Auvergne-Rh\u00f4ne-Alpes. Village de montagne du massif de la Vanoise, en Tarentaise, il comptait 724 habitants en 2017.\nLe village est une station touristique d'\u00e9t\u00e9 et de sports d'hiver install\u00e9e au c\u0153ur du parc national de la Vanoise, proposant de nombreuses activit\u00e9s sportives de montagne, telles que la randonn\u00e9e (les sentiers de grande randonn\u00e9e GR 5 et GR 55 y passent) ou des via ferrata.\n\n\n== G\u00e9ographie ==\n\n\n=== Situation ===\nPralognan-la-Vanoise est la derni\u00e8re commune de la vall\u00e9e de Bozel (Tarentaise). Le centre du village, situ\u00e9 \u00e0 environ 1 400 m\u00e8tres d'altitude, s'\u00e9tablit au confluent des vall\u00e9es glaciaires de la Gli\u00e8re et de Chavi\u00e8re. Toutes deux constituent des points de passage vers la vall\u00e9e de la Maurienne par le col de la Vanoise (2 517 m\u00e8tres) ou le col de Chavi\u00e8re (2 796 m\u00e8tres).\n\n\n=== Communes limitrophes ===\n\n\n=== G\u00e9ologie et relief, hydrographie ===\n\nLe Doron de Pralognan \u2014 form\u00e9 en amont de diff\u00e9rents cours d'eau (torrent de la Gli\u00e8re, du Dard et nant de la Cr\u00e9p\u00e9na, puis du ruisseau d'Isertan) \u2014 et le Doron de Chavi\u00e8re se rejoignent dans la commune. En aval, il conflue avec le Doron de Champagny pour former le Doron de Bozel.\n\n\n=== Climat ===\nLa situation de Pralognan-la-Vanoise, d'une altitude d'environ 1 400 m, la place dans un milieu continental montagnard caract\u00e9ris\u00e9 par une humidit\u00e9 marqu\u00e9e. Les hivers sont plus froids et neigeux, et la saison estivale douce avec parfois des \u00e9pisodes orageux."
