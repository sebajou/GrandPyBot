import requests
from GrandPyBotApp.functions.Parse import Parser
from GrandPyBotApp import app
from PIL import Image
from io import BytesIO

GOOGLE_MAP_API_KEY = app.config['GOOGLE_MAP_API_KEY']


class TheGoogleMapParseCom(Parser):
    """ This class parse message from front input from user and return it to the Google Map API"""

    # 1 get title from WikiMedia in TheWikiMediaParseCom.get_title_from_api
    # => https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch=port+vieux+marseille&format=json
    # 2 get coordinates link to the title
    # => https://fr.wikipedia.org/w/api.php?action=query&prop=coordinates&titles=Vieux-Port_de_Marseille&format=json
    # 3 display map (or map at differente scale) link to this coordinates
    # => https://maps.googleapis.com/maps/api/staticmap?center=43.294, 5.37&zoom=12&size=400x400&key=GOOGLE_MAP_API_KEY

    def get_coordinates_from_api(self, title):
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

    def parse_coordinates_from_api(self, data_coordinates):
        pass

    def get_image_from_api(self, coordinates, title):
        URL = "https://maps.googleapis.com/maps/api/staticmap"
        COORDINATES = coordinates
        PARAMS = {
            "center": COORDINATES,
            "zoom": "16",
            "size": "400x400",
            "key": GOOGLE_MAP_API_KEY
        }
        img = requests.get(url=URL, params=PARAMS)
        i = Image.open(BytesIO(img.content))
        i.save('GrandPyBotApp/static/img/'+title, format='png')
