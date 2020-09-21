import requests
from config import *


class ParsedRequestedQuestionFromCoordinates:
    """Give a key word for obtain wikipedia resources and other from share coordinates"""

    @staticmethod
    def get_json_title_from_api(data_coordinates):
        """This function get coordinate from a given title with Google map API"""

        the_url = "https://maps.googleapis.com/maps/api/geocode/json?"

        the_params = {
            "latlng": data_coordinates,
            "key": GOOGLE_MAP_API_KEY_COORDINATES
        }
        json_title = requests.get(url=the_url, params=the_params)
        json_title = json_title.json()

        return json_title

    @staticmethod
    def get_long_name(json_title):
        """Extract Name of location from Google Map's json API"""
        try:
            return json_title['results'][0]['address_components'][1]['long_name']

        except (UnboundLocalError, IndexError, KeyError):
            return "Quelque part sur terre"

    def get_parsed_requested_question_from_coordinates(self, data_coordinates):
        """Extract Name of location from Google Map's json API after request this API"""
        json_title = self.get_json_title_from_api(data_coordinates)
        parsed_requested_question = self.get_long_name(json_title)

        return parsed_requested_question
