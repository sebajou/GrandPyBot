

class Coordinates:

    @staticmethod
    def get_coordinates(title):
        if title == "OpenClassrooms":
            return "48.8975156, 2.3833993"
        elif title == "Atlantide":
            return "45.9996836, -73.9187669"
        elif title == "Empty request"
            return "45.9996836, -73.9187669"
        else:
            return "45.9996836, -73.9187669"

    @staticmethod
    def get_formatted_address(data_coordinates):
        if data_coordinates == {'results': [{'address_components': [{'long_name': '10', 'short_name': '10', 'types': ['street_number']}, {'long_name': 'Quai de la Charente', 'short_name': 'Quai de la Charente', 'types': ['route']}, {'long_name': 'Paris', 'short_name': 'Paris', 'types': ['locality', 'political']}, {'long_name': 'Arrondissement de Paris', 'short_name': 'Arrondissement de Paris', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Île-de-France', 'short_name': 'IDF', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']}, {'long_name': '75019', 'short_name': '75019', 'types': ['postal_code']}], 'formatted_address': '10 Quai de la Charente, 75019 Paris, France', 'geometry': {'location': {'lat': 48.8975156, 'lng': 2.3833993}, 'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 48.8988645802915, 'lng': 2.384748280291502}, 'southwest': {'lat': 48.8961666197085, 'lng': 2.382050319708498}}}, 'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8', 'plus_code': {'compound_code': 'V9XM+29 Paris, France', 'global_code': '8FW4V9XM+29'}, 'types': ['establishment', 'point_of_interest']}, {'address_components': [{'long_name': '10', 'short_name': '10', 'types': ['street_number']}, {'long_name': 'Cité Paradis', 'short_name': 'Cité Paradis', 'types': ['route']}, {'long_name': 'Paris', 'short_name': 'Paris', 'types': ['locality', 'political']}, {'long_name': 'Arrondissement de Paris', 'short_name': 'Arrondissement de Paris', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Île-de-France', 'short_name': 'IDF', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']}, {'long_name': '75010', 'short_name': '75010', 'types': ['postal_code']}], 'formatted_address': '10 Cité Paradis, 75010 Paris, France', 'geometry': {'location': {'lat': 48.8750991, 'lng': 2.3489738}, 'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 48.8764480802915, 'lng': 2.350322780291502}, 'southwest': {'lat': 48.8737501197085, 'lng': 2.347624819708498}}}, 'place_id': 'ChIJLUzI3xRu5kcRX7qwoQiY5bM', 'plus_code': {'compound_code': 'V8GX+2H Paris, France', 'global_code': '8FW4V8GX+2H'}, 'types': ['electronics_store', 'establishment', 'home_goods_store', 'point_of_interest', 'store']}], 'status': 'OK'}:
            return "10 Quai de la Charente, 75019 Paris, France"
        elif data_coordinates == {'results': [{'address_components': [{'long_name': 'Atlantis Water Park', 'short_name': 'Atlantis Water Park', 'types': ['amusement_park', 'establishment', 'park', 'point_of_interest', 'tourist_attraction']}, {'long_name': '11155', 'short_name': '11155', 'types': ['street_number']}, {'long_name': 'Québec 335', 'short_name': 'QC-335', 'types': ['route']}, {'long_name': 'Saint-Calixte', 'short_name': 'Saint-Calixte', 'types': ['locality', 'political']}, {'long_name': 'Saint-Calixte', 'short_name': 'Saint-Calixte', 'types': ['administrative_area_level_3', 'political']}, {'long_name': 'Montcalm', 'short_name': 'Montcalm', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Québec', 'short_name': 'QC', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'Canada', 'short_name': 'CA', 'types': ['country', 'political']}, {'long_name': 'J0K 1Z0', 'short_name': 'J0K 1Z0', 'types': ['postal_code']}], 'formatted_address': 'Atlantis Water Park, 11155 QC-335, Saint-Calixte, QC J0K 1Z0, Canada', 'geometry': {'location': {'lat': 45.9996836, 'lng': -73.9187669}, 'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 46.0010325802915, 'lng': -73.91741791970848}, 'southwest': {'lat': 45.9983346197085, 'lng': -73.9201158802915}}}, 'place_id': 'ChIJY_H9kMTKyEwR16_4HyfYvY0', 'plus_code': {'compound_code': 'X3XJ+VF Saint-Calixte, QC, Canada', 'global_code': '87Q8X3XJ+VF'}, 'types': ['amusement_park', 'establishment', 'park', 'point_of_interest', 'tourist_attraction']}], 'status': 'OK'}:
            return "Atlantis Water Park, 11155 QC-335, Saint-Calixte, QC J0K 1Z0, Canada"
        elif data_coordinates == {'results': [], 'status': 'ZERO_RESULTS'}:
            return == "Quelques part sur terre"

