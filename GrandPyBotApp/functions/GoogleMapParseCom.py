import requests
from GrandPyBotApp.functions.Parse import Parser
from config import *
# from GrandPyBotApp import app
from PIL import Image
from io import BytesIO
import json

# GOOGLE_MAP_API_KEY = app.config['GOOGLE_MAP_API_KEY']


class TheGoogleMapParseCom(Parser):
    """ This class parse message from front input from user and return it to the Google Map API"""

    # 1 get title from WikiMedia in TheWikiMediaParseCom.get_title_from_api
    # => https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch=port+vieux+marseille&format=json
    # 2 get coordinates link to the title
    # => https://fr.wikipedia.org/w/api.php?action=query&prop=coordinates&titles=Vieux-Port_de_Marseille&format=json
    # 3 display map (or map at differente scale) link to this coordinates
    # => https://maps.googleapis.com/maps/api/staticmap?center=43.294, 5.37&zoom=12&size=400x400&key=GOOGLE_MAP_API_KEY

    def get_coordinates_from_api(self, title):
        """This function interogate the API Wiki Media to obtain coordinate from a title from an another function"""
        URL = "https://fr.wikipedia.org/w/api.php"
        TITLES = title
        PARAMS = {
            "action": "query",
            "prop": "coordinates",
            "titles": TITLES,
            "format": "json"
        }
        data_coordinates = requests.get(url=URL, params=PARAMS)
        return data_coordinates

    @staticmethod
    def parse_coordinates_from_api(data_coordinates):
        """ Extract coordinate from Wiki Media API json and put it in a string"""
        # Loop in Wiki media API json results from request for obtain coordinates.
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

    def get_image_from_api(self, coordinates):
        """ Function for interogate Google Map API with coordinates to obtain a static map. """

        zoom = ["16", "10", "5"]
        imgUrlList =[]

        for ZOOM in zoom:
            URL = "https://maps.googleapis.com/maps/api/staticmap"
            COORDINATES = coordinates
            PARAMS = {
                "center": COORDINATES,
                "zoom": ZOOM,
                "size": "400x400",
                "key": GOOGLE_MAP_API_KEY
            }
            img = requests.get(url=URL, params=PARAMS)

            imgUrlList.append(img.url)

        return imgUrlList
