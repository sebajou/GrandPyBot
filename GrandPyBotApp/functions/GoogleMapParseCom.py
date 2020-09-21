import requests
from GrandPyBotApp.functions.Parse import Parser
from config import *
import json

# GOOGLE_MAP_API_KEY = app.config['GOOGLE_MAP_API_KEY']


class TheGoogleMapParseCom(Parser):
    """ This class parse message from front input from user and return it to the Google Map API"""

    @staticmethod
    def get_coordinates_from_api(title):
        """This function interrogate the API Wiki Media to obtain coordinate from a title from an another function"""
        the_url = "https://fr.wikipedia.org/w/api.php"
        the_titles = title
        the_params = {
            "action": "query",
            "prop": "coordinates",
            "titles": the_titles,
            "format": "json"
        }
        data_coordinates = requests.get(url=the_url, params=the_params)
        return data_coordinates

    @staticmethod
    def parse_coordinates_from_api(data_coordinates):
        """ Extract coordinate from Wiki Media API json and put it in a string"""
        data_coordinates = json.loads(data_coordinates.read().decode("utf8"))
        # Loop in Wiki media API json results from request for title.
        for json_content in data_coordinates["query"]['pages']:
            for json_content2 in data_coordinates["query"]['pages'][json_content]['coordinates'][0]:
                if json_content2 == 'lat':
                    string_coordinates_lat = data_coordinates["query"]['pages'][json_content]['coordinates'][0]['lat']
                if json_content2 == 'lat':
                    string_coordinates_lon = data_coordinates["query"]['pages'][json_content]['coordinates'][0]['lon']

        string_coordinates_lat = str(string_coordinates_lat)
        string_coordinates_lon = str(string_coordinates_lon)

        string_coordinates = string_coordinates_lat + ', ' + string_coordinates_lon

        return string_coordinates

    @staticmethod
    def get_image_from_api(coordinates):
        """ Function for interrogate Google Map API with coordinates to obtain a static map. """

        zoom = ["16", "10", "5"]
        img_url_list =[]

        for ZOOM in zoom:
            the_url = "https://maps.googleapis.com/maps/api/staticmap"
            the_coordinates = coordinates
            the_params = {
                "center": the_coordinates,
                "zoom": ZOOM,
                "size": "350x350",
                "key": GOOGLE_MAP_API_KEY
            }
            img = requests.get(url=the_url, params=the_params)

            img_url_list.append(img.url)

        return img_url_list
