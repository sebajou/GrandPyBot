import GrandPyBotApp.functions.googleMapCoordinates as script
from GrandPyBotApp import app
import json


class TestCoordinates:

    def setup_method(self):
        # Values to test (Pralognan la Vanoise coordinates)
        self.coordinates = "45.382062, 6.721232"
        self.title ="Pralognan la Vanoise"

    def test_get_coordinates(self):

        # Attribute usefull for the test
        coord = self.coordinates
        titles = self.title

        # Call the class Coordinates
        getCoord = script.Coordinates()

        # Assert
        assert getCoord.get_coordinates(titles) == coord


