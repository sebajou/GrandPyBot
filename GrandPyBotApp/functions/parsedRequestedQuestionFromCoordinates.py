import requests
from config import *


class ParsedRequestedQuestionFromCoordinates:
    """Give a key word for obtain wikipedia ressources and other from share coordinates"""

    @staticmethod
    def get_json_title_from_api(data_coordinates):
        """This function get coordinate from a given title with Google map API"""

        URL = "https://maps.googleapis.com/maps/api/geocode/json?"

        PARAMS = {
            "latlng": data_coordinates,
            "key": GOOGLE_MAP_API_KEY_COORDINATES
        }
        json_title = requests.get(url=URL, params=PARAMS)
        json_title = json_title.json()

        return json_title

    @staticmethod
    def get_long_name(json_title):
        try:
            return json_title['results'][0]['address_components'][1]['long_name']

        except (UnboundLocalError, IndexError, KeyError):
            return "Quelques part sur terre"

    def get_parsed_requested_question_from_coordinates(self, data_coordinates):

        json_title = self.get_json_title_from_api(data_coordinates)
        parsed_requested_question = self.get_long_name(json_title)

        return parsed_requested_question

