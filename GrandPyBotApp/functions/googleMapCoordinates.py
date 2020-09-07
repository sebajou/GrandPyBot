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

        try:
            lat = data_coordinates['results'][0]['geometry']['location']['lat']
            lng = data_coordinates['results'][0]['geometry']['location']['lng']
            lat = str(lat)
            lng = str(lng)
        except UnboundLocalError:
            print("No coordinates corresponding to the request.")
            atlantide = "45.9996836, -73.9187669"
            return atlantide
        except IndexError:
            print("No coordinates corresponding to the request.")
            atlantide = "45.9996836, -73.9187669"
            return atlantide
        except KeyError:
            print("Empty Request")
            atlantique = "34.97532, -40.85828"
            return atlantique

        coordinates = lat + ', ' + lng
        return coordinates

    def get_coordinates(self, title):

        data_coordinates = self.get_coordinates_from_api(title)
        coordinates = self.parse_coordinates_from_api(data_coordinates)

        return coordinates

    @staticmethod
    def get_formatted_address(data_coordinates):
        try:
            return data_coordinates['results'][0]['formatted_address']
        except UnboundLocalError:
            return "Quelques part sur terre"
        except IndexError:
            return "Quelques part sur terre"
        except KeyError:
            return "Quelques part sur terre"


