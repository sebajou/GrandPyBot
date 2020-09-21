from GrandPyBotApp.functions.parsedRequestedQuestionFromCoordinates import ParsedRequestedQuestionFromCoordinates


class TestParsedRequestedQuestionFromCoordinates:

    def setup_method(self):
        self.coordinates = "45.382062, 6.721232"
        self.parsed_requested_question = "Pralognan-la-Vanoise"
        self.coordinates_api_json_results = {'plus_code': {'compound_code': '9PJC+RF Pralognan-la-Vanoise, France', 'global_code': '8FQ89PJC+RF'}, 'results': [{'address_components': [{'long_name': '306', 'short_name': '306', 'types': ['street_number']}, {'long_name': 'Avenue de Chasseforet', 'short_name': 'Avenue de Chasseforet', 'types': ['route']}, {'long_name': 'Pralognan-la-Vanoise', 'short_name': 'Pralognan-la-Vanoise', 'types': ['locality', 'political']}, {'long_name': 'Savoie', 'short_name': 'Savoie', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Auvergne-Rhône-Alpes', 'short_name': 'Auvergne-Rhône-Alpes', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']}, {'long_name': '73710', 'short_name': '73710', 'types': ['postal_code']}], 'formatted_address': '306 Avenue de Chasseforet, 73710 Pralognan-la-Vanoise, France', 'geometry': {'location': {'lat': 45.3820427, 'lng': 6.721212299999999}, 'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 45.3833916802915, 'lng': 6.722561280291502}, 'southwest': {'lat': 45.3806937197085, 'lng': 6.719863319708497}}}, 'place_id': 'ChIJ_YCknzediUcRdUIO4GEzTDA', 'plus_code': {'compound_code': '9PJC+RF Pralognan-la-Vanoise, France', 'global_code': '8FQ89PJC+RF'}, 'types': ['street_address']}, {'address_components': [{'long_name': '306', 'short_name': '306', 'types': ['street_number']}, {'long_name': 'Avenue de Chasseforet', 'short_name': 'Avenue de Chasseforet', 'types': ['route']}, {'long_name': 'Pralognan-la-Vanoise', 'short_name': 'Pralognan-la-Vanoise', 'types': ['locality', 'political']}, {'long_name': 'Savoie', 'short_name': 'Savoie', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Auvergne-Rhône-Alpes', 'short_name': 'Auvergne-Rhône-Alpes', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']}, {'long_name': '73710', 'short_name': '73710', 'types': ['postal_code']}], 'formatted_address': '306 Avenue de Chasseforet, 73710 Pralognan-la-Vanoise, France', 'geometry': {'location': {'lat': 45.3820427, 'lng': 6.721212299999999}, 'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 45.3833916802915, 'lng': 6.722561280291502}, 'southwest': {'lat': 45.3806937197085, 'lng': 6.719863319708497}}}, 'place_id': 'ChIJW73yZTediUcRE3ydXWMbEow', 'plus_code': {'compound_code': '9PJC+RF Pralognan-la-Vanoise, France', 'global_code': '8FQ89PJC+RF'}, 'types': ['city_hall', 'establishment', 'local_government_office', 'point_of_interest']}, {'address_components': [{'long_name': '203', 'short_name': '203', 'types': ['street_number']}, {'long_name': 'Avenue de Chasseforet', 'short_name': 'Avenue de Chasseforet', 'types': ['route']}, {'long_name': 'Pralognan-la-Vanoise', 'short_name': 'Pralognan-la-Vanoise', 'types': ['locality', 'political']}, {'long_name': 'Savoie', 'short_name': 'Savoie', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Auvergne-Rhône-Alpes', 'short_name': 'Auvergne-Rhône-Alpes', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']}, {'long_name': '73710', 'short_name': '73710', 'types': ['postal_code']}], 'formatted_address': '203 Avenue de Chasseforet, 73710 Pralognan-la-Vanoise, France', 'geometry': {'bounds': {'northeast': {'lat': 45.3817171, 'lng': 6.7216117}, 'southwest': {'lat': 45.3815761, 'lng': 6.7214366}}, 'location': {'lat': 45.381666, 'lng': 6.721510899999999}, 'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 45.38299558029149, 'lng': 6.722873130291502}, 'southwest': {'lat': 45.3802976197085, 'lng': 6.720175169708497}}}, 'place_id': 'ChIJF_bXdjediUcRRp_n8uLfHv4', 'types': ['premise']}, {'address_components': [{'long_name': '305', 'short_name': '305', 'types': ['street_number']}, {'long_name': 'Avenue de Chasseforet', 'short_name': 'Avenue de Chasseforet', 'types': ['route']}, {'long_name': 'Pralognan-la-Vanoise', 'short_name': 'Pralognan-la-Vanoise', 'types': ['locality', 'political']}, {'long_name': 'Savoie', 'short_name': 'Savoie', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Auvergne-Rhône-Alpes', 'short_name': 'Auvergne-Rhône-Alpes', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']}, {'long_name': '73710', 'short_name': '73710', 'types': ['postal_code']}], 'formatted_address': '305 Avenue de Chasseforet, 73710 Pralognan-la-Vanoise, France', 'geometry': {'location': {'lat': 45.3818344, 'lng': 6.720905399999999}, 'location_type': 'RANGE_INTERPOLATED', 'viewport': {'northeast': {'lat': 45.38318338029149, 'lng': 6.722254380291502}, 'southwest': {'lat': 45.38048541970849, 'lng': 6.719556419708498}}}, 'place_id': 'Ej0zMDUgQXZlbnVlIGRlIENoYXNzZWZvcmV0LCA3MzcxMCBQcmFsb2duYW4tbGEtVmFub2lzZSwgRnJhbmNlIhsSGQoUChIJvT2WdDediUcRh0Qblz1LSjQQsQI', 'types': ['street_address']}, {'address_components': [{'long_name': '236-318', 'short_name': '236-318', 'types': ['street_number']}, {'long_name': 'Avenue de Chasseforet', 'short_name': 'D915', 'types': ['route']}, {'long_name': 'Pralognan-la-Vanoise', 'short_name': 'Pralognan-la-Vanoise', 'types': ['locality', 'political']}, {'long_name': 'Savoie', 'short_name': 'Savoie', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Auvergne-Rhône-Alpes', 'short_name': 'Auvergne-Rhône-Alpes', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']}, {'long_name': '73710', 'short_name': '73710', 'types': ['postal_code']}], 'formatted_address': '236-318 D915, 73710 Pralognan-la-Vanoise, France', 'geometry': {'bounds': {'northeast': {'lat': 45.381925, 'lng': 6.7214393}, 'southwest': {'lat': 45.3813615, 'lng': 6.720778999999999}}, 'location': {'lat': 45.3816573, 'lng': 6.7211338}, 'location_type': 'GEOMETRIC_CENTER', 'viewport': {'northeast': {'lat': 45.3829922302915, 'lng': 6.722458130291502}, 'southwest': {'lat': 45.3802942697085, 'lng': 6.719760169708497}}}, 'place_id': 'ChIJvT2WdDediUcRhkQblz1LSjQ', 'types': ['route']}, {'address_components': [{'long_name': '73710', 'short_name': '73710', 'types': ['postal_code']}, {'long_name': 'Pralognan-la-Vanoise', 'short_name': 'Pralognan-la-Vanoise', 'types': ['locality', 'political']}, {'long_name': 'Savoie', 'short_name': 'Savoie', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Auvergne-Rhône-Alpes', 'short_name': 'Auvergne-Rhône-Alpes', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']}], 'formatted_address': '73710 Pralognan-la-Vanoise, France', 'geometry': {'bounds': {'northeast': {'lat': 45.4173985, 'lng': 6.828684300000001}, 'southwest': {'lat': 45.2684687, 'lng': 6.6337927}}, 'location': {'lat': 45.3562442, 'lng': 6.7164044}, 'location_type': 'APPROXIMATE', 'viewport': {'northeast': {'lat': 45.4173985, 'lng': 6.828684300000001}, 'southwest': {'lat': 45.2684687, 'lng': 6.6337927}}}, 'place_id': 'ChIJ0cdEvZOciUcRMIXkQS6rCBw', 'types': ['postal_code']}, {'address_components': [{'long_name': 'Pralognan-la-Vanoise', 'short_name': 'Pralognan-la-Vanoise', 'types': ['locality', 'political']}, {'long_name': 'Savoie', 'short_name': 'Savoie', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Auvergne-Rhône-Alpes', 'short_name': 'Auvergne-Rhône-Alpes', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']}, {'long_name': '73710', 'short_name': '73710', 'types': ['postal_code']}], 'formatted_address': '73710 Pralognan-la-Vanoise, France', 'geometry': {'bounds': {'northeast': {'lat': 45.4171931, 'lng': 6.827487}, 'southwest': {'lat': 45.2687369, 'lng': 6.6337528}}, 'location': {'lat': 45.382062, 'lng': 6.721232}, 'location_type': 'APPROXIMATE', 'viewport': {'northeast': {'lat': 45.4171931, 'lng': 6.827487}, 'southwest': {'lat': 45.2687369, 'lng': 6.6337528}}}, 'place_id': 'ChIJ0cdEvZOciUcRAK665CqrCAQ', 'types': ['locality', 'political']}, {'address_components': [{'long_name': 'Savoie', 'short_name': 'Savoie', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Auvergne-Rhône-Alpes', 'short_name': 'Auvergne-Rhône-Alpes', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']}], 'formatted_address': 'Savoie, France', 'geometry': {'bounds': {'northeast': {'lat': 45.9385369, 'lng': 7.1855661}, 'southwest': {'lat': 45.0516891, 'lng': 5.621902}}, 'location': {'lat': 45.4932045, 'lng': 6.472399999999999}, 'location_type': 'APPROXIMATE', 'viewport': {'northeast': {'lat': 45.9385369, 'lng': 7.1855661}, 'southwest': {'lat': 45.0516891, 'lng': 5.621902}}}, 'place_id': 'ChIJ01Qj_B7Si0cRECq55CqrCAM', 'types': ['administrative_area_level_2', 'political']}, {'address_components': [{'long_name': 'Auvergne-Rhône-Alpes', 'short_name': 'Auvergne-Rhône-Alpes', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']}], 'formatted_address': 'Auvergne-Rhône-Alpes, France', 'geometry': {'bounds': {'northeast': {'lat': 46.804293, 'lng': 7.1855661}, 'southwest': {'lat': 44.115493, 'lng': 2.062882}}, 'location': {'lat': 45.4471431, 'lng': 4.385250699999999}, 'location_type': 'APPROXIMATE', 'viewport': {'northeast': {'lat': 46.804293, 'lng': 7.1855661}, 'southwest': {'lat': 44.115493, 'lng': 2.062882}}}, 'place_id': 'ChIJ_fju9ukE9UcROuOAIn5wRjk', 'types': ['administrative_area_level_1', 'political']}, {'address_components': [{'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']}], 'formatted_address': 'France', 'geometry': {'bounds': {'northeast': {'lat': 51.1241999, 'lng': 9.6624999}, 'southwest': {'lat': 41.31433, 'lng': -5.5591}}, 'location': {'lat': 46.227638, 'lng': 2.213749}, 'location_type': 'APPROXIMATE', 'viewport': {'northeast': {'lat': 51.1241999, 'lng': 9.6624999}, 'southwest': {'lat': 41.31433, 'lng': -5.5591}}}, 'place_id': 'ChIJMVd4MymgVA0R99lHx5Y__Ws', 'types': ['country', 'political']}], 'status': 'OK'}

    def test_get_parsed_requested_question_from_coordinates(self, monkeypatch):
        coord = self.coordinates
        parsed_req_question = self.parsed_requested_question

        # Mock the class Coordinates
        def mock_get_parsed_requested_question_from_coordinates(coord):
            return "Pralognan-la-Vanoise"
        monkeypatch.setattr('GrandPyBotApp.functions.parsedRequestedQuestionFromCoordinates'
                            '.ParsedRequestedQuestionFromCoordinates.get_parsed_requested_question_from_coordinates',
                            mock_get_parsed_requested_question_from_coordinates)

        assert ParsedRequestedQuestionFromCoordinates.get_parsed_requested_question_from_coordinates(coord) == \
               parsed_req_question