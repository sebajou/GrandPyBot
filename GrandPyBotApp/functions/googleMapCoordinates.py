import requests
from config import *


class Coordinates:

    @staticmethod
    def get_coordinates_from_api(title):
        """This function get coordinate from a given title with Google map API"""
        # https://maps.googleapis.com/maps/api/geocode/json?address=Pralognan+la+Vanoise,+CA&key=GOOGLE_MAP_API_KEY_COORDINATES
        URL = "https://maps.googleapis.com/maps/api/geocode/json?"
        TITLES = title
        PARAMS = {
            "address": TITLES,
            "key": GOOGLE_MAP_API_KEY_COORDINATES
        }
        data_coordinates = requests.get(url=URL, params=PARAMS)
        data_coordinates = data_coordinates.json()

        return data_coordinates

    @staticmethod
    def parse_coordinates_from_api(data_coordinates):

        lat = data_coordinates['results'][0]['geometry']['location']['lat']
        lng = data_coordinates['results'][0]['geometry']['location']['lng']
        lat = str(lat)
        lng = str(lng)

        coordinates = lat + ', ' + lng

        return coordinates

    def get_coordinates(self, title):

        data_coordinates = self.get_coordinates_from_api(title)
        coordinates = self.parse_coordinates_from_api(data_coordinates)

        return coordinates


