import requests
from config import *


class Coordinates:

    @staticmethod
    def get_coordinates_from_api(title):
        """This function get coordinate from a given title with Google map API"""
        the_url = "https://maps.googleapis.com/maps/api/geocode/json?"
        the_titles = title
        the_params = {
            "address": the_titles,
            "key": GOOGLE_MAP_API_KEY_COORDINATES
        }
        data_coordinates = requests.get(url=the_url, params=the_params)
        data_coordinates = data_coordinates.json()

        return data_coordinates

    @staticmethod
    def parse_coordinates_from_api(data_coordinates):
        """Parse data from API's json"""
        try:
            lat = data_coordinates['results'][0]['geometry']['location']['lat']
            lng = data_coordinates['results'][0]['geometry']['location']['lng']
            lat = str(lat)
            lng = str(lng)
        except (UnboundLocalError, IndexError, KeyError):
            print("No coordinates corresponding to the request.")
            atlantide = "45.9996836, -73.9187669"
            return atlantide

        coordinates = lat + ', ' + lng
        return coordinates

    def get_coordinates(self, title):
        """Execude fonction of Coordinates class in the aim to obtain coordinates from a given title"""
        data_coordinates = self.get_coordinates_from_api(title)
        coordinates = self.parse_coordinates_from_api(data_coordinates)

        return coordinates

    @staticmethod
    def get_formatted_address(data_coordinates):
        """Extract formatted address from coordinates"""
        try:
            return data_coordinates['results'][0]['formatted_address']
        except (UnboundLocalError, IndexError, KeyError):
            return "Quelque part sur terre"
