import GrandPyBotApp.functions.googleMapCoordinates as script
from GrandPyBotApp import app
import json


class TestCoordinates:

    def setup_method(self):
        # Values to test (Pralognan la Vanoise coordinates)
        self.coordinates = "45.382062, 6.721232"
        self.title ="Pralognan la Vanoise"
        self.absurd_title = "DdgDarghh"
        self.atlandide_coord = "45.9996836, -73.9187669"

    def test_get_coordinates(self):

        # Attribute useful for the test
        coord = self.coordinates
        titles = self.title

        # Call the class Coordinates
        getCoord = script.Coordinates()

        # Assert
        assert getCoord.get_coordinates(titles) == coord

    def test_get_coordinates_from_absurd_tittle(self):

        # Attribute useful for the test
        atlandide_coord = self.atlandide_coord
        absurd_title = self.absurd_title

        # Call the class Coordinates
        getCoord = script.Coordinates()

        assert getCoord.get_coordinates(absurd_title) == atlandide_coord


