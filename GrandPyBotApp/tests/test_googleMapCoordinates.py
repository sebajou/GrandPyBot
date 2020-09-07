import pytest
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
        self.formated_address = '354-406 Avenue de Chasseforet, 73710 Pralognan-la-Vanoise, France'
        self.coordinates_api_json_results = {
   "results" : [
      {
         "address_components" : [
            {
               "long_name" : "354-406",
               "short_name" : "354-406",
               "types" : [ "street_number" ]
            },
            {
               "long_name" : "Avenue de Chasseforet",
               "short_name" : "Avenue de Chasseforet",
               "types" : [ "route" ]
            },
            {
               "long_name" : "Pralognan-la-Vanoise",
               "short_name" : "Pralognan-la-Vanoise",
               "types" : [ "locality", "political" ]
            },
            {
               "long_name" : "Savoie",
               "short_name" : "Savoie",
               "types" : [ "administrative_area_level_2", "political" ]
            },
            {
               "long_name" : "Auvergne-Rhône-Alpes",
               "short_name" : "Auvergne-Rhône-Alpes",
               "types" : [ "administrative_area_level_1", "political" ]
            },
            {
               "long_name" : "France",
               "short_name" : "FR",
               "types" : [ "country", "political" ]
            },
            {
               "long_name" : "73710",
               "short_name" : "73710",
               "types" : [ "postal_code" ]
            }
         ],
         "formatted_address" : "354-406 Avenue de Chasseforet, 73710 Pralognan-la-Vanoise, France",
         "geometry" : {
            "location" : {
               "lat" : 45.382175,
               "lng" : 6.720212999999999
            },
            "location_type" : "ROOFTOP",
            "viewport" : {
               "northeast" : {
                  "lat" : 45.38352398029149,
                  "lng" : 6.721561980291502
               },
               "southwest" : {
                  "lat" : 45.38082601970849,
                  "lng" : 6.718864019708497
               }
            }
         },
         "place_id" : "ChIJzRcOZjediUcRgLSJOfu0gIU",
         "plus_code" : {
            "compound_code" : "9PJC+V3 Pralognan-la-Vanoise, France",
            "global_code" : "8FQ89PJC+V3"
         },
         "types" : [ "bank", "establishment", "finance", "point_of_interest" ]
      }
   ],
   "status" : "OK"
}

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

    def test_get_formatted_address(self):

        # Attribute useful for the test
        data_coordinates =self.coordinates_api_json_results
        formated_address = self.formated_address


        # Call the class Coordinates
        getCoord = script.Coordinates()

        # Obtain results from tested function
        assert getCoord.get_formatted_address(data_coordinates) == formated_address

