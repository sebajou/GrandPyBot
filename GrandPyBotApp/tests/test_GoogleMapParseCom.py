import GrandPyBotApp.functions.GoogleMapParseCom as script
import requests
import pytest
from GrandPyBotApp import app

GOOGLE_MAP_API_KEY = app.config['GOOGLE_MAP_API_KEY']


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

    def test_parse_message_from_front(self):
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
        parse = script.TheGoogleMapParseCom()
        assert [word for word in parse.parse_message_from_front(message_from_front=message_to_parse1) if word in ["openclassrooms"]]
        assert [word for word in parse.parse_message_from_front(message_from_front=message_to_parse2) if word in ["gare", "lyon", "paris"]]
        assert [word for word in parse.parse_message_from_front(message_from_front=message_to_parse3) if word in ["vieux", "port", "marseille"]]
        assert [word for word in parse.parse_message_from_front(message_from_front=message_to_parse4) if word in ["venise"]]
        assert [word for word in parse.parse_message_from_front(message_from_front=message_to_parse5) if word in ["antilles"]]
        assert [word for word in parse.parse_message_from_front(message_from_front=message_to_parse6) if word in ["tunisie"]]
        assert [word for word in parse.parse_message_from_front(message_from_front=message_to_parse7) if word in ["hong-kong"]]
        assert [word for word in parse.parse_message_from_front(message_from_front=message_to_parse8) if word in ["barbade"]]
        assert [word for word in parse.parse_message_from_front(message_from_front=message_to_parse9) if word in ["timor", "oriental"]]

    """def test_send_message_to_api(self):
        to_api_request_localisation = self.api_request_localisation
        assert script.TheGoogleMapParseCom.send_message_to_api(to_api_request_localisation).status_code == 200
"""
