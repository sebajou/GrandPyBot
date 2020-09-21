import pytest
from GrandPyBotApp.views import app


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    """Remove requests.sessions.Session.request for all tests."""
    monkeypatch.delattr("requests.sessions.Session.request")


class TestIntegration:
    """ Test get, post and route of application"""

    def setup_method(self):
        self.normal_to_post = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
        self.absurd_to_post = "dsqgrr(5éht"
        self.empty_to_post = ""
        self.coordinates_to_post = "45.393503599999995, 6.7251974"
        self.absurd_coordinates_to_post = "-96.393503599999995, 566.7251974"
        self.json_from_normal_to_post = {
            "imgUrlList1": "https://maps.googleapis.com/maps/api/staticmap?"
                           "center=48.8975156%2C+2.3833993&zoom=16&size=350x350&"
                           "key=AIzaSyAkPL6F9QLiACGJT3ettWsKIX0OoZHlsQc",
            "imgUrlList2": "https://maps.googleapis.com/maps/api/staticmap?"
                           "center=48.8975156%2C+2.3833993&zoom=10&size=350x350&"
                           "key=AIzaSyAkPL6F9QLiACGJT3ettWsKIX0OoZHlsQc",
            "imgUrlList3": "https://maps.googleapis.com/maps/api/staticmap?"
                           "center=48.8975156%2C+2.3833993&zoom=5&size=350x350&"
                           "key=AIzaSyAkPL6F9QLiACGJT3ettWsKIX0OoZHlsQc",
            "question": "<br><p style=\"color:#04fc6d;\">Vous : "
                        "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
                        "<p/><p style=\"color:#0417fc;\"> "
                        "GrandPyBot : J’y suis déjà allé. C’était en 1963. "
                        "Évidemment, depuis ça a changé !  "
                        "Cette endroit se trouve à l'adresse : 10 Quai de la Charente, 75019 Paris, France"
                        "<p/>OpenClassrooms est un site web de formation en ligne qui propose à ses membres des cours "
                        "certifiants et des parcours débouchant sur des métiers en croissance. Ses contenus sont "
                        "réalisés en interne, par des écoles, des universités, des entreprises partenaires comme "
                        "Microsoft ou IBM, ou historiquement par des bénévoles. Jusqu'en 2018, n'importe quel membre "
                        "du site pouvait être auteur, via un outil nommé « interface de rédaction » puis « Course Lab "
                        "». De nombreux cours sont issus de la communauté, mais ne sont plus mis en avant. "
                        "Initialement orientée autour de la programmation informatique, la plate-forme couvre depuis "
                        "2013 des thématiques plus larges tels que le marketing, l'entrepreneuriat et les "
                        "sciences.\nCréé en 1999 sous le nom de Site du Zéro, il se forme essentiellement sur la base "
                        "de contributions de bénévoles proposant des tutoriels vulgarisés avec un ton léger portant "
                        "sur des sujets informatiques divers. À la suite du succès et de la fin des études des "
                        "gérants, l'entreprise Simple IT, renommée ensuite OpenClassrooms, est fondée dans le but de "
                        "pérenniser le site. Celle-ci base son modèle économique sur la délivrance de certifications "
                        "payantes et propose un abonnement pour être suivi par un mentor,. Suite à ces changements, "
                        "des utilisateurs créent un site web aux buts similaires, dont les auteurs et l'association "
                        "le gérant sont uniquement bénévoles et ne propose pas de certifications (Zeste de "
                        "Savoir).\n\n\n== Fonctionnement ==\nLe site propose un catalogue de plus de 1 000 tutoriels "
                        "accessibles en ligne.<br> "
        }

    @staticmethod
    def test_view_home(client):
        assert client.get('/').status_code == 200

    def test_view(self, client, monkeypatch):
        message_to_post = self.normal_to_post

        def mock_parse_message_from_front(self, message_from_front):
            return 'openclassrooms'
        monkeypatch.setattr('GrandPyBotApp.functions.Parse.Parser.parse_message_from_front',
                            mock_parse_message_from_front)

        def mock_get_coordinates(self, title):
            return '48.8975156, 2.3833993'
        monkeypatch.setattr('GrandPyBotApp.functions.googleMapCoordinates.Coordinates.get_coordinates',
                            mock_get_coordinates)

        def mock_get_coordinates_from_api(self, title):
            return {'results': [{'address_components': [{'long_name': '10', 'short_name': '10', 'types': ['street_number']}, {'long_name': 'Quai de la Charente', 'short_name': 'Quai de la Charente', 'types': ['route']}, {'long_name': 'Paris', 'short_name': 'Paris', 'types': ['locality', 'political']}, {'long_name': 'Arrondissement de Paris', 'short_name': 'Arrondissement de Paris', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Île-de-France', 'short_name': 'IDF', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']}, {'long_name': '75019', 'short_name': '75019', 'types': ['postal_code']}], 'formatted_address': '10 Quai de la Charente, 75019 Paris, France', 'geometry': {'location': {'lat': 48.8975156, 'lng': 2.3833993}, 'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 48.8988645802915, 'lng': 2.384748280291502}, 'southwest': {'lat': 48.8961666197085, 'lng': 2.382050319708498}}}, 'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8', 'plus_code': {'compound_code': 'V9XM+29 Paris, France', 'global_code': '8FW4V9XM+29'}, 'types': ['establishment', 'point_of_interest']}, {'address_components': [{'long_name': '10', 'short_name': '10', 'types': ['street_number']}, {'long_name': 'Cité Paradis', 'short_name': 'Cité Paradis', 'types': ['route']}, {'long_name': 'Paris', 'short_name': 'Paris', 'types': ['locality', 'political']}, {'long_name': 'Arrondissement de Paris', 'short_name': 'Arrondissement de Paris', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Île-de-France', 'short_name': 'IDF', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']}, {'long_name': '75010', 'short_name': '75010', 'types': ['postal_code']}], 'formatted_address': '10 Cité Paradis, 75010 Paris, France', 'geometry': {'location': {'lat': 48.8750991, 'lng': 2.3489738}, 'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 48.8764480802915, 'lng': 2.350322780291502}, 'southwest': {'lat': 48.8737501197085, 'lng': 2.347624819708498}}}, 'place_id': 'ChIJLUzI3xRu5kcRX7qwoQiY5bM', 'plus_code': {'compound_code': 'V8GX+2H Paris, France', 'global_code': '8FW4V8GX+2H'}, 'types': ['electronics_store', 'establishment', 'home_goods_store', 'point_of_interest', 'store']}], 'status': 'OK'}
        monkeypatch.setattr('GrandPyBotApp.functions.googleMapCoordinates.Coordinates.get_coordinates_from_api',
                            mock_get_coordinates_from_api)

        def mock_get_formatted_address(self, data_coordinates):
            return '10 Quai de la Charente, 75019 Paris, France'
        monkeypatch.setattr('GrandPyBotApp.functions.googleMapCoordinates.Coordinates.get_formatted_address',
                            mock_get_formatted_address)

        def mock_get_image_from_api(self, coordinates):
            return ['https://maps.googleapis.com/maps/api/staticmap?center=48.8975156%2C+2.3833993&zoom=16&size'
                    '=350x350&key=AIzaSyAkPL6F9QLiACGJT3ettWsKIX0OoZHlsQc',
                    'https://maps.googleapis.com/maps/api/staticmap?center=48.8975156%2C+2.3833993&zoom=10&size'
                    '=350x350&key=AIzaSyAkPL6F9QLiACGJT3ettWsKIX0OoZHlsQc',
                    'https://maps.googleapis.com/maps/api/staticmap?center=48.8975156%2C+2.3833993&zoom=5&size'
                    '=350x350&key=AIzaSyAkPL6F9QLiACGJT3ettWsKIX0OoZHlsQc']
        monkeypatch.setattr('GrandPyBotApp.functions.GoogleMapParseCom.TheGoogleMapParseCom.get_image_from_api',
                            mock_get_image_from_api)

        monkeypatch.setattr('GrandPyBotApp.functions.RandomMessage.TheRandomMessage', lambda: 'J’y suis déjà allé. '
                                                                                              'C’était en 1963. '
                                                                                              'Évidemment, '
                                                                                              'depuis ça a changé ! ')

        def mock_get_title_from_api(self, message_to_api):
            return {'batchcomplete': '', 'continue': {'sroffset': 10, 'continue': '-||'}, 'query': {'searchinfo': {'totalhits': 41}, 'search': [{'ns': 0, 'title': 'OpenClassrooms', 'pageid': 4338589, 'size': 30770, 'wordcount': 3143, 'snippet': 'chez <span class="searchmatch">OpenClassrooms</span>\xa0», <span class="searchmatch">OpenClassrooms</span>\xa0: le blog,\u200e 17 avril 2018 (lire en ligne, consulté le 11 juillet 2018) «\xa0<span class="searchmatch">OpenClassrooms</span>\xa0», sur <span class="searchmatch">openclassrooms</span>.com', 'timestamp': '2020-08-03T11:29:42Z'}, {'ns': 0, 'title': 'Massive Open Online Course', 'pageid': 6436398, 'size': 55242, 'wordcount': 5707, 'snippet': 'sur <span class="searchmatch">openclassrooms</span>.com (consulté le 22 septembre 2015) «\xa0Google\xa0», sur <span class="searchmatch">openclassrooms</span>.com (consulté le 22 septembre 2015) «\xa0IBM\xa0», sur <span class="searchmatch">openclassrooms</span>.com', 'timestamp': '2020-08-07T14:04:41Z'}, {'ns': 0, 'title': 'Compilateur', 'pageid': 635, 'size': 23027, 'wordcount': 2776, 'snippet': '«\xa0Découvrez le cours &quot;Compilation à la volée avec libtcc&quot; sur @<span class="searchmatch">OpenClassrooms</span>\xa0», sur <span class="searchmatch">OpenClassrooms</span> (consulté le 21 novembre 2016). «\xa0tranpiler\xa0», sur wiktionary', 'timestamp': '2020-08-15T12:49:38Z'}, {'ns': 0, 'title': 'Unix', 'pageid': 3081, 'size': 43396, 'wordcount': 4675, 'snippet': '(consulté le 2 juillet 2017). «\xa0Mais c\'est quoi, Linux\xa0? @<span class="searchmatch">OpenClassrooms</span>\xa0», sur <span class="searchmatch">OpenClassrooms</span> (consulté le 3 juillet 2017). (en) Andrew Tanenbaum, «\xa0Some', 'timestamp': '2020-08-30T17:41:13Z'}, {'ns': 0, 'title': 'Zeste de Savoir', 'pageid': 12431773, 'size': 4665, 'wordcount': 344, 'snippet': 'fondée le 1er avril 2014, à la suite de changements de politique d\'\'<span class="searchmatch">OpenClassrooms</span>. Celle-ci promeut le partage de connaissances et l\'auto-formation, participe', 'timestamp': '2020-07-05T10:10:30Z'}, {'ns': 0, 'title': 'Percolation', 'pageid': 84364, 'size': 7795, 'wordcount': 875, 'snippet': 'Hoshen-Kopelman Théorie de la percolation La percolation sur le site <span class="searchmatch">OpenClassrooms</span> Article La percolation, un jeu de pavages aléatoires de Hugo Duminil-Copin', 'timestamp': '2020-09-08T03:02:50Z'}, {'ns': 0, 'title': 'Sudo', 'pageid': 869228, 'size': 4707, 'wordcount': 571, 'snippet': '(consulté le 2 novembre 2019) «\xa0Les utilisateurs et les droits\xa0», sur <span class="searchmatch">OpenClassrooms</span> (consulté le 1er septembre 2015). su sudosh Role-Based Access Control', 'timestamp': '2020-07-01T10:27:03Z'}, {'ns': 0, 'title': 'Programmation dynamique', 'pageid': 128278, 'size': 18992, 'wordcount': 2707, 'snippet': '«\xa0Introduction à la programmation dynamique\xa0», sur http://<span class="searchmatch">openclassrooms</span>.com/, <span class="searchmatch">OpenClassrooms</span> (consulté le 21 février 2015) Robert Cori, «\xa0Principe de', 'timestamp': '2019-12-27T22:12:13Z'}, {'ns': 0, 'title': 'Broadcast (informatique)', 'pageid': 3363958, 'size': 3825, 'wordcount': 551, 'snippet': 'Anycast Géocast Voir Broadcast address (en) Calculer ses plages d\'adresses sur <span class="searchmatch">OpenClassrooms</span> Portail de l’informatique Portail des télécommunications', 'timestamp': '2019-05-02T12:12:24Z'}, {'ns': 0, 'title': 'PHP', 'pageid': 2350, 'size': 67571, 'wordcount': 5039, 'snippet': 'Foundation\xa0» (consulté le 7 novembre 2007) «\xa0Introduction à PHP\xa0», sur <span class="searchmatch">openclassrooms</span>.com (consulté le 14 juillet 2015). «\xa0PHP is dead…Viva le PHP! – Hacker', 'timestamp': '2020-08-17T20:24:58Z'}]}}
        monkeypatch.setattr('GrandPyBotApp.functions.WikiMediaParseCom.TheWikiMediaParseCom.get_title_from_api',
                            mock_get_title_from_api)

        def mock_json_title(self, media_wiki_request_search_result):
            return 'OpenClassrooms'
        monkeypatch.setattr('GrandPyBotApp.functions.WikiMediaParseCom.TheWikiMediaParseCom.json_title', mock_json_title)

        def mock_json_extract(self, media_wiki_request_extract_result):
            return 'OpenClassrooms est un site web de formation en ligne qui propose à ses membres des cours ' \
                   'certifiants et des parcours débouchant sur des métiers en croissance. Ses contenus sont réalisés ' \
                   'en interne, par des écoles, des universités, des entreprises partenaires comme Microsoft ou IBM, ' \
                   'ou historiquement par des bénévoles. Jusqu\'en 2018, n\'importe quel membre du site pouvait être ' \
                   'auteur, via un outil nommé « interface de rédaction » puis « Course Lab ». De nombreux cours sont ' \
                   'issus de la communauté, mais ne sont plus mis en avant. Initialement orientée autour de la ' \
                   'programmation informatique, la plate-forme couvre depuis 2013 des thématiques plus larges tels ' \
                   'que le marketing, l\'entrepreneuriat et les sciences.\nCréé en 1999 sous le nom de Site du Zéro, ' \
                   'il se forme essentiellement sur la base de contributions de bénévoles proposant des tutoriels ' \
                   'vulgarisés avec un ton léger portant sur des sujets informatiques divers. À la suite du succès et ' \
                   'de la fin des études des gérants, l\'entreprise Simple IT, renommée ensuite OpenClassrooms, ' \
                   'est fondée dans le but de pérenniser le site. Celle-ci base son modèle économique sur la ' \
                   'délivrance de certifications payantes et propose un abonnement pour être suivi par un mentor,' \
                   '. Suite à ces changements, des utilisateurs créent un site web aux buts similaires, ' \
                   'dont les auteurs et l\'association le gérant sont uniquement bénévoles et ne propose pas de ' \
                   'certifications (Zeste de Savoir).\n\n\n== Fonctionnement ==\nLe site propose un catalogue de plus ' \
                   'de 1 000 tutoriels accessibles en ligne. '
        monkeypatch.setattr('GrandPyBotApp.functions.WikiMediaParseCom.TheWikiMediaParseCom.json_extract',
                            mock_json_extract)

        def mock_get_extract_from_api(self, title):
            return {'batchcomplete': '', 'query': {'pages': {'4338589': {'pageid': 4338589, 'ns': 0, 'title': 'OpenClassrooms', 'extract': "OpenClassrooms est un site web de formation en ligne qui propose à ses membres des cours certifiants et des parcours débouchant sur des métiers en croissance. Ses contenus sont réalisés en interne, par des écoles, des universités, des entreprises partenaires comme Microsoft ou IBM, ou historiquement par des bénévoles. Jusqu'en 2018, n'importe quel membre du site pouvait être auteur, via un outil nommé « interface de rédaction » puis « Course Lab ». De nombreux cours sont issus de la communauté, mais ne sont plus mis en avant. Initialement orientée autour de la programmation informatique, la plate-forme couvre depuis 2013 des thématiques plus larges tels que le marketing, l'entrepreneuriat et les sciences.\nCréé en 1999 sous le nom de Site du Zéro, il se forme essentiellement sur la base de contributions de bénévoles proposant des tutoriels vulgarisés avec un ton léger portant sur des sujets informatiques divers. À la suite du succès et de la fin des études des gérants, l'entreprise Simple IT, renommée ensuite OpenClassrooms, est fondée dans le but de pérenniser le site. Celle-ci base son modèle économique sur la délivrance de certifications payantes et propose un abonnement pour être suivi par un mentor,. Suite à ces changements, des utilisateurs créent un site web aux buts similaires, dont les auteurs et l'association le gérant sont uniquement bénévoles et ne propose pas de certifications (Zeste de Savoir).\n\n\n== Fonctionnement ==\nLe site propose un catalogue de plus de 1 000 tutoriels accessibles en ligne."}}}}
        monkeypatch.setattr('GrandPyBotApp.functions.WikiMediaParseCom.TheWikiMediaParseCom.get_extract_from_api',
                            mock_get_extract_from_api)

        assert client.post('/conversation', data=dict(question=message_to_post)).status_code == 200

    def test_view_absurd(self, client, monkeypatch):
        message_to_post = self.absurd_to_post

        def mock_parse_message_from_front(self, message_from_front):
            return 'dsqgrr(5éht'
        monkeypatch.setattr('GrandPyBotApp.functions.Parse.Parser.parse_message_from_front',
                            mock_parse_message_from_front)

        def mock_get_coordinates(self, title):
            return '45.9996836, -73.9187669'
        monkeypatch.setattr('GrandPyBotApp.functions.googleMapCoordinates.Coordinates.get_coordinates',
                            mock_get_coordinates)

        def mock_get_coordinates_from_api(self, title):
            return {'results': [{'address_components': [{'long_name': 'Atlantis Water Park', 'short_name': 'Atlantis '
                                                                                                           'Water '
                                                                                                           'Park',
                                                         'types': ['amusement_park', 'establishment', 'park',
                                                                   'point_of_interest', 'tourist_attraction']},
                                                        {'long_name': '11155', 'short_name': '11155',
                                                         'types': ['street_number']}, {'long_name': 'Québec 335',
                                                                                       'short_name': 'QC-335',
                                                                                       'types': ['route']},
                                                        {'long_name': 'Saint-Calixte', 'short_name': 'Saint-Calixte',
                                                         'types': ['locality', 'political']},
                                                        {'long_name': 'Saint-Calixte', 'short_name': 'Saint-Calixte',
                                                         'types': ['administrative_area_level_3', 'political']},
                                                        {'long_name': 'Montcalm', 'short_name': 'Montcalm',
                                                         'types': ['administrative_area_level_2', 'political']},
                                                        {'long_name': 'Québec', 'short_name': 'QC', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'Canada', 'short_name': 'CA', 'types': ['country', 'political']}, {'long_name': 'J0K 1Z0', 'short_name': 'J0K 1Z0', 'types': ['postal_code']}], 'formatted_address': 'Atlantis Water Park, 11155 QC-335, Saint-Calixte, QC J0K 1Z0, Canada', 'geometry': {'location': {'lat': 45.9996836, 'lng': -73.9187669}, 'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 46.0010325802915, 'lng': -73.91741791970848}, 'southwest': {'lat': 45.9983346197085, 'lng': -73.9201158802915}}}, 'place_id': 'ChIJY_H9kMTKyEwR16_4HyfYvY0', 'plus_code': {'compound_code': 'X3XJ+VF Saint-Calixte, QC, Canada', 'global_code': '87Q8X3XJ+VF'}, 'types': ['amusement_park', 'establishment', 'park', 'point_of_interest', 'tourist_attraction']}], 'status': 'OK'}
        monkeypatch.setattr('GrandPyBotApp.functions.googleMapCoordinates.Coordinates.get_coordinates_from_api',
                            mock_get_coordinates_from_api)

        def mock_get_formatted_address(self, data_coordinates):
            return 'Atlantis Water Park, 11155 QC-335, Saint-Calixte, QC J0K 1Z0, Canada'
        monkeypatch.setattr('GrandPyBotApp.functions.googleMapCoordinates.Coordinates.get_formatted_address',
                            mock_get_formatted_address)

        def mock_get_image_from_api(self, coordinates):
            return ['https://maps.googleapis.com/maps/api/staticmap?center=37.5398268%2C+-107.777521&zoom=16&size'
                    '=350x350&key=AIzaSyAkPL6F9QLiACGJT3ettWsKIX0OoZHlsQc',
                    'https://maps.googleapis.com/maps/api/staticmap?center=37.5398268%2C+-107.777521&zoom=10&size'
                    '=350x350&key=AIzaSyAkPL6F9QLiACGJT3ettWsKIX0OoZHlsQc',
                    'https://maps.googleapis.com/maps/api/staticmap?center=37.5398268%2C+-107.777521&zoom=5&size'
                    '=350x350&key=AIzaSyAkPL6F9QLiACGJT3ettWsKIX0OoZHlsQc']
        monkeypatch.setattr('GrandPyBotApp.functions.GoogleMapParseCom.TheGoogleMapParseCom.get_image_from_api',
                            mock_get_image_from_api)

        monkeypatch.setattr('GrandPyBotApp.functions.RandomMessage.TheRandomMessage', lambda: 'J’y suis déjà allé. '
                                                                                              'C’était en 1963. '
                                                                                              'Évidemment, '
                                                                                              'depuis ça a changé ! ')

        def mock_get_title_from_api(self, message_to_api):
            return {'batchcomplete': '', 'query': {'searchinfo': {'totalhits': 0}, 'search': []}}
        monkeypatch.setattr('GrandPyBotApp.functions.WikiMediaParseCom.TheWikiMediaParseCom.get_title_from_api',
                            mock_get_title_from_api)

        def mock_json_title(self, media_wiki_request_search_result):
            return 'Atlantide'
        monkeypatch.setattr('GrandPyBotApp.functions.WikiMediaParseCom.TheWikiMediaParseCom.json_title', mock_json_title)

        def mock_json_extract(self, media_wiki_request_extract_result):
            return 'L’Atlantide (du grec ancien Ἀτλαντίς / Atlantís) est une île mythique évoquée par Platon dans ' \
                   'deux de ses Dialogues, le Timée puis le Critias. Cette île, qu’il situe au-delà des Colonnes ' \
                   'd\'Hercule, est dédiée à Poséidon et, après avoir connu un âge d\'or pacifique, ' \
                   'évolue progressivement vers une thalassocratie conquérante dont l\'expansion est arrêtée par ' \
                   'Athènes, avant que l\'île ne soit engloutie par les flots dans un cataclysme provoqué à ' \
                   'l\'instigation de Zeus.  \nSi le mythe a été peu commenté et a eu peu d\'influence durant ' \
                   'l\'Antiquité, il a suscité un intérêt croissant à partir de la Renaissance. Au-delà de sa portée ' \
                   'philosophique et politique, il a depuis donné naissance à de nombreuses hypothèses. Certains ' \
                   'auteurs affirment que l\'Atlantide est un lieu qui aurait réellement existé et qu\'il serait ' \
                   'possible de localiser. Dans le même temps, l\'Atlantide inspire de nombreuses interprétations ' \
                   'ésotériques, allégoriques ou encore patriotiques qui ont donné lieu à une abondante ' \
                   'littérature.\nAu début du XXIe siècle, les chercheurs restent partagés, entre les partisans ' \
                   'd\'une Atlantide de pure fiction (majoritaires dans la recherche scientifique) et ceux d\'une ' \
                   'lecture du récit de Platon basée sur des événements réels. \nL\'Atlantide demeure un thème ' \
                   'fertile dans l\'art et la littérature, en particulier de nos jours, dans les genres liés au ' \
                   'merveilleux et au fantastique, comme la fantasy, le péplum ou la science-fiction.\n\n\n== Sources ' \
                   '==\n\n\n=== Prise de vue ===\n\nL\'histoire de l\'Atlantide puise son origine dans deux des ' \
                   'Dialogues du philosophe athénien Platon (428 — 348 avant J.-C.), le Timée et le Critias, ' \
                   'qui sont présentés comme une suite de La République et ont pour objet d\'illustrer, à travers ce ' \
                   'récit,  les vertus des citoyens idéaux suivant Socrate, montrant comment une Athènes vertueuse ' \
                   'est venue à bout d\'un ennemi malfaisant.   \nPlaton, « inventeur » de l\'Atlantide, y confronte ' \
                   'deux images de la Cité au travers de l\'affrontement de deux d\'entre elles, en des temps ' \
                   'immémoriaux. '
        monkeypatch.setattr('GrandPyBotApp.functions.WikiMediaParseCom.TheWikiMediaParseCom.json_extract',
                            mock_json_extract)

        def mock_get_extract_from_api(self, title):
            return {'batchcomplete': '', 'query': {'pages': {'20852': {'pageid': 20852, 'ns': 0, 'title': 'Atlantide', 'extract': "L’Atlantide (du grec ancien Ἀτλαντίς / Atlantís) est une île mythique évoquée par Platon dans deux de ses Dialogues, le Timée puis le Critias. Cette île, qu’il situe au-delà des Colonnes d'Hercule, est dédiée à Poséidon et, après avoir connu un âge d'or pacifique, évolue progressivement vers une thalassocratie conquérante dont l'expansion est arrêtée par Athènes, avant que l'île ne soit engloutie par les flots dans un cataclysme provoqué à l'instigation de Zeus.  \nSi le mythe a été peu commenté et a eu peu d'influence durant l'Antiquité, il a suscité un intérêt croissant à partir de la Renaissance. Au-delà de sa portée philosophique et politique, il a depuis donné naissance à de nombreuses hypothèses. Certains auteurs affirment que l'Atlantide est un lieu qui aurait réellement existé et qu'il serait possible de localiser. Dans le même temps, l'Atlantide inspire de nombreuses interprétations ésotériques, allégoriques ou encore patriotiques qui ont donné lieu à une abondante littérature.\nAu début du XXIe siècle, les chercheurs restent partagés, entre les partisans d'une Atlantide de pure fiction (majoritaires dans la recherche scientifique) et ceux d'une lecture du récit de Platon basée sur des événements réels. \nL'Atlantide demeure un thème fertile dans l'art et la littérature, en particulier de nos jours, dans les genres liés au merveilleux et au fantastique, comme la fantasy, le péplum ou la science-fiction.\n\n\n== Sources ==\n\n\n=== Prise de vue ===\n\nL'histoire de l'Atlantide puise son origine dans deux des Dialogues du philosophe athénien Platon (428 — 348 avant J.-C.), le Timée et le Critias, qui sont présentés comme une suite de La République et ont pour objet d'illustrer, à travers ce récit,  les vertus des citoyens idéaux suivant Socrate, montrant comment une Athènes vertueuse est venue à bout d'un ennemi malfaisant.   \nPlaton, « inventeur » de l'Atlantide, y confronte deux images de la Cité au travers de l'affrontement de deux d'entre elles, en des temps immémoriaux."}}}}
        monkeypatch.setattr('GrandPyBotApp.functions.WikiMediaParseCom.TheWikiMediaParseCom.get_extract_from_api',
                            mock_get_extract_from_api)

        assert client.post('/conversation', data=dict(question=message_to_post)).status_code == 200

    def test_view_empty(self, client, monkeypatch):
        message_to_post = self.empty_to_post

        def mock_parse_message_from_front(self, message_from_front):
            return ''
        monkeypatch.setattr('GrandPyBotApp.functions.Parse.Parser.parse_message_from_front',
                            mock_parse_message_from_front)

        def mock_get_coordinates(self, title):
            return '45.9996836, -73.9187669'
        monkeypatch.setattr('GrandPyBotApp.functions.googleMapCoordinates.Coordinates.get_coordinates',
                            mock_get_coordinates)

        def mock_get_coordinates_from_api(self, title):
            return {'results': [], 'status': 'ZERO_RESULTS'}
        monkeypatch.setattr('GrandPyBotApp.functions.googleMapCoordinates.Coordinates.get_coordinates_from_api',
                            mock_get_coordinates_from_api)

        def mock_get_formatted_address(self, data_coordinates):
            return 'Quelques part sur terre'
        monkeypatch.setattr('GrandPyBotApp.functions.googleMapCoordinates.Coordinates.get_formatted_address', mock_get_formatted_address)

        def mock_get_image_from_api(self, coordinates):
            return ['https://maps.googleapis.com/maps/api/staticmap?center=45.9996836%2C+-73.9187669&zoom=16&size'
                    '=350x350&key=AIzaSyAkPL6F9QLiACGJT3ettWsKIX0OoZHlsQc',
                    'https://maps.googleapis.com/maps/api/staticmap?center=45.9996836%2C+-73.9187669&zoom=10&size'
                    '=350x350&key=AIzaSyAkPL6F9QLiACGJT3ettWsKIX0OoZHlsQc',
                    'https://maps.googleapis.com/maps/api/staticmap?center=45.9996836%2C+-73.9187669&zoom=5&size'
                    '=350x350&key=AIzaSyAkPL6F9QLiACGJT3ettWsKIX0OoZHlsQc']
        monkeypatch.setattr('GrandPyBotApp.functions.GoogleMapParseCom.TheGoogleMapParseCom.get_image_from_api',
                            mock_get_image_from_api)

        monkeypatch.setattr('GrandPyBotApp.functions.RandomMessage.TheRandomMessage', lambda: 'J’y suis déjà allé. '
                                                                                              'C’était en 1963. '
                                                                                              'Évidemment, '
                                                                                              'depuis ça a changé ! ')

        def mock_get_title_from_api(self, message_to_api):
            return {'error': {'code': 'missingparam', 'info': 'The "srsearch" parameter must be set.', '*': 'See https://fr.wikipedia.org/w/api.php for API usage. Subscribe to the mediawiki-api-announce mailing list at &lt;https://lists.wikimedia.org/mailman/listinfo/mediawiki-api-announce&gt; for notice of API deprecations and breaking changes.'}, 'servedby': 'mw2366'}
        monkeypatch.setattr('GrandPyBotApp.functions.WikiMediaParseCom.TheWikiMediaParseCom.get_title_from_api',
                            mock_get_title_from_api)

        def mock_json_title(self, media_wiki_request_search_result):
            return "Empty request"
        monkeypatch.setattr('GrandPyBotApp.functions.WikiMediaParseCom.TheWikiMediaParseCom.json_title',
                            mock_json_title)

        def mock_json_extract(self, media_wiki_request_extract_result):
            return ''
        monkeypatch.setattr('GrandPyBotApp.functions.WikiMediaParseCom.TheWikiMediaParseCom.json_extract',
                            mock_json_extract)

        def mock_get_extract_from_api(self, title):
            return {'batchcomplete': '', 'query': {'pages': {'-1': {'ns': 0, 'title': 'Empty request', 'missing': ''}}}}
        monkeypatch.setattr('GrandPyBotApp.functions.WikiMediaParseCom.TheWikiMediaParseCom.get_extract_from_api',
                            mock_get_extract_from_api)

        assert client.post('/conversation', data=dict(question=message_to_post)).status_code == 200

    def test_view_coordinates(self, client, monkeypatch):
        message_to_post = self.coordinates_to_post

        def mock_get_parsed_requested_question_from_coordinates(self, requested_coord):
            return 'Pralognan-la-Vanoise'
        monkeypatch.setattr('GrandPyBotApp.functions.parsedRequestedQuestionFromCoordinates'
                            '.ParsedRequestedQuestionFromCoordinates.get_parsed_requested_question_from_coordinates',
                            mock_get_parsed_requested_question_from_coordinates)

        def mock_parse_message_from_front(self, message_from_front):
            return 'Pralognan-la-Vanoise'
        monkeypatch.setattr('GrandPyBotApp.functions.Parse.Parser.parse_message_from_front',
                            mock_parse_message_from_front)

        def mock_get_coordinates_from_api(self, title):
            return {'results': [{'address_components': [{'long_name': 'Pralognan-la-Vanoise',
                                                         'short_name': 'Pralognan-la-Vanoise',
                                                         'types': ['locality', 'political']},
                                                        {'long_name': 'Savoie', 'short_name': 'Savoie',
                                                         'types': ['administrative_area_level_2', 'political']},
                                                        {'long_name': 'Auvergne-Rhône-Alpes',
                                                         'short_name': 'Auvergne-Rhône-Alpes',
                                                         'types': ['administrative_area_level_1', 'political']},
                                                        {'long_name': 'France', 'short_name': 'FR',
                                                         'types': ['country', 'political']},
                                                        {'long_name': '73710', 'short_name': '73710',
                                                         'types': ['postal_code']}],
                                 'formatted_address': '73710 Pralognan-la-Vanoise, France',
                                 'geometry': {'bounds': {'northeast': {'lat': 45.4171931, 'lng': 6.827487},
                                                         'southwest': {'lat': 45.2687369, 'lng': 6.6337528}},
                                              'location': {'lat': 45.382062, 'lng': 6.721232},
                                              'location_type': 'APPROXIMATE', 'viewport':
                                                  {'northeast': {'lat': 45.4171931, 'lng': 6.827487},
                                                   'southwest': {'lat': 45.2687369, 'lng': 6.6337528}}}, 'place_id': 'ChIJ0cdEvZOciUcRAK665CqrCAQ', 'types': ['locality', 'political']}], 'status': 'OK'}
        monkeypatch.setattr('GrandPyBotApp.functions.googleMapCoordinates.Coordinates.get_coordinates_from_api',
                            mock_get_coordinates_from_api)

        def mock_get_formatted_address(self, data_coordinates):
            return '73710 Pralognan-la-Vanoise, France'
        monkeypatch.setattr('GrandPyBotApp.functions.googleMapCoordinates.Coordinates.get_formatted_address',
                            mock_get_formatted_address)

        def mock_get_image_from_api(self, coordinates):
            return ['https://maps.googleapis.com/maps/api/staticmap?center=45.393503599999995%2C+6.7251974&zoom=16'
                    '&size=350x350&key=AIzaSyAkPL6F9QLiACGJT3ettWsKIX0OoZHlsQc',
                    'https://maps.googleapis.com/maps/api/staticmap?center=45.393503599999995%2C+6.7251974&zoom=10'
                    '&size=350x350&key=AIzaSyAkPL6F9QLiACGJT3ettWsKIX0OoZHlsQc',
                    'https://maps.googleapis.com/maps/api/staticmap?center=45.393503599999995%2C+6.7251974&zoom=5'
                    '&size=350x350&key=AIzaSyAkPL6F9QLiACGJT3ettWsKIX0OoZHlsQc']
        monkeypatch.setattr('GrandPyBotApp.functions.GoogleMapParseCom.TheGoogleMapParseCom.get_image_from_api',
                            mock_get_image_from_api)

        monkeypatch.setattr('GrandPyBotApp.functions.RandomMessage.TheRandomMessage',
                            lambda: 'J’y suis déjà allé. C’était en 1963. Évidemment, depuis ça a changé ! ')

        def mock_get_title_from_api(self, message_to_api):
            return {'batchcomplete': '', 'continue': {'sroffset': 10, 'continue': '-||'}, 'query': {'searchinfo': {'totalhits': 128}, 'search': [{'ns': 0, 'title': 'Pralognan-la-Vanoise', 'pageid': 586449, 'size': 45723, 'wordcount': 4640, 'snippet': 'Pour les articles homonymes, voir <span class="searchmatch">Vanoise</span>. <span class="searchmatch">Pralognan</span>-<span class="searchmatch">la</span>-<span class="searchmatch">Vanoise</span> est une commune française située dans le département de <span class="searchmatch">la</span> Savoie, en région Auvergne-Rhône-Alpes', 'timestamp': '2020-09-15T02:02:21Z'}, {'ns': 0, 'title': 'Col de la Vanoise', 'pageid': 928898, 'size': 10187, 'wordcount': 1295, 'snippet': 'homonymes, voir <span class="searchmatch">Vanoise</span>. Le col de <span class="searchmatch">la</span> <span class="searchmatch">Vanoise</span> est un col des Alpes françaises culminant à 2\xa0517\xa0mètres dans le parc national de <span class="searchmatch">la</span> <span class="searchmatch">Vanoise</span>. Il permet l\'accès', 'timestamp': '2020-06-30T13:49:01Z'}, {'ns': 0, 'title': 'Massif de la Vanoise', 'pageid': 99158, 'size': 15514, 'wordcount': 1908, 'snippet': 'Pour les articles homonymes, voir <span class="searchmatch">Vanoise</span>. Le massif de <span class="searchmatch">la</span> <span class="searchmatch">Vanoise</span> est un massif montagneux des Alpes françaises, intégralement situé en Savoie. Il abrite', 'timestamp': '2020-09-16T16:55:15Z'}, {'ns': 0, 'title': 'Champagny-en-Vanoise', 'pageid': 677471, 'size': 12417, 'wordcount': 1341, 'snippet': 'Champagny et <span class="searchmatch">Vanoise</span>. Champagny-en-<span class="searchmatch">Vanoise</span> est une commune française située dans le département de <span class="searchmatch">la</span> Savoie, en région Auvergne-Rhône-Alpes. <span class="searchmatch">La</span> commune compte', 'timestamp': '2020-09-17T20:55:57Z'}, {'ns': 0, 'title': 'Parc national de la Vanoise', 'pageid': 69436, 'size': 29348, 'wordcount': 2386, 'snippet': 'voir <span class="searchmatch">Vanoise</span>. Parc national de <span class="searchmatch">la</span> <span class="searchmatch">Vanoise</span> Les glaciers de <span class="searchmatch">la</span> <span class="searchmatch">Vanoise</span>. modifier - modifier le code - modifier Wikidata Le parc national de <span class="searchmatch">la</span> <span class="searchmatch">Vanoise</span> est', 'timestamp': '2020-09-16T11:29:51Z'}, {'ns': 0, 'title': 'Hockey Courchevel Méribel Pralognan', 'pageid': 2991927, 'size': 7450, 'wordcount': 379, 'snippet': 'Pralognan-la-<span class="searchmatch">Vanoise</span>. Il évolue au troisième niveau national (Division 2) depuis <span class="searchmatch">la</span> saison 2018-2019. En 1964, le club de <span class="searchmatch">Pralognan</span>-<span class="searchmatch">la</span>-<span class="searchmatch">Vanoise</span> est fondé', 'timestamp': '2020-04-15T07:33:34Z'}, {'ns': 0, 'title': 'Vanoise', 'pageid': 96536, 'size': 1062, 'wordcount': 147, 'snippet': ' <span class="searchmatch">La</span> <span class="searchmatch">Vanoise</span> est un lieu des Alpes au sud de <span class="searchmatch">Pralognan</span> ayant donné son nom à plusieurs entités géographiques\xa0: Aiguille de <span class="searchmatch">la</span> <span class="searchmatch">Vanoise</span>, sommet de <span class="searchmatch">la</span> vallée', 'timestamp': '2020-08-24T13:34:32Z'}, {'ns': 0, 'title': 'Aiguille de la Vanoise', 'pageid': 1048095, 'size': 4465, 'wordcount': 404, 'snippet': '<span class="searchmatch">la</span> <span class="searchmatch">Vanoise</span> est un sommet du massif de <span class="searchmatch">la</span> <span class="searchmatch">Vanoise</span> dominant <span class="searchmatch">Pralognan</span>-<span class="searchmatch">la</span>-<span class="searchmatch">Vanoise</span>. Elle est réputée pour sa grande face nord de 300 à 400 m de haut. <span class="searchmatch">La</span> première', 'timestamp': '2020-04-19T16:28:46Z'}, {'ns': 0, 'title': 'Communauté de communes Val Vanoise', 'pageid': 7724796, 'size': 10665, 'wordcount': 497, 'snippet': 'communes de Champagny-en-<span class="searchmatch">Vanoise</span> et de <span class="searchmatch">Pralognan</span>-<span class="searchmatch">la</span>-<span class="searchmatch">Vanoise</span>. Depuis le 1er janvier 2014, <span class="searchmatch">la</span> communauté de communes Val <span class="searchmatch">Vanoise</span> Tarentaise remplace l\'ancien', 'timestamp': '2020-08-10T12:04:10Z'}, {'ns': 0, 'title': 'Lac des Vaches', 'pageid': 10416661, 'size': 5808, 'wordcount': 546, 'snippet': '1974, p.\xa0291 Rando <span class="searchmatch">Vanoise</span>, «\xa0Tour de l\'aiguille de <span class="searchmatch">la</span> <span class="searchmatch">Vanoise</span> et col de <span class="searchmatch">la</span> <span class="searchmatch">Vanoise</span> depuis <span class="searchmatch">Pralognan</span>-<span class="searchmatch">la</span>-<span class="searchmatch">Vanoise</span>\xa0», sur rando.<span class="searchmatch">vanoise</span>.com (consulté le 6', 'timestamp': '2019-06-23T08:02:38Z'}]}}
        monkeypatch.setattr('GrandPyBotApp.functions.WikiMediaParseCom.TheWikiMediaParseCom.get_title_from_api',
                            mock_get_title_from_api)

        def mock_json_title(self, media_wiki_request_search_result):
            return 'Pralognan-la-Vanoise'
        monkeypatch.setattr('GrandPyBotApp.functions.WikiMediaParseCom.TheWikiMediaParseCom.json_title', mock_json_title)

        def mock_json_extract(self, media_wiki_request_extract_result):
            return 'Pralognan-la-Vanoise  est une commune française située dans le département de la Savoie, ' \
                   'en région Auvergne-Rhône-Alpes. Village de montagne du massif de la Vanoise, en Tarentaise, ' \
                   'il comptait 724 habitants en 2017.\nLe village est une station touristique d\'été et de sports ' \
                   'd\'hiver installée au cœur du parc national de la Vanoise, proposant de nombreuses activités ' \
                   'sportives de montagne, telles que la randonnée (les sentiers de grande randonnée GR 5 et GR 55 y ' \
                   'passent) ou des via ferrata.\n\n\n== Géographie ==\n\n\n=== Situation ===\nPralognan-la-Vanoise ' \
                   'est la dernière commune de la vallée de Bozel (Tarentaise). Le centre du village, situé à environ ' \
                   '1 400 mètres d\'altitude, s\'établit au confluent des vallées glaciaires de la Glière et de ' \
                   'Chavière. Toutes deux constituent des points de passage vers la vallée de la Maurienne par le col ' \
                   'de la Vanoise (2 517 mètres) ou le col de Chavière (2 796 mètres).\n\n\n=== Communes limitrophes ' \
                   '===\n\n\n=== Géologie et relief, hydrographie ===\n\nLe Doron de Pralognan — formé en amont de ' \
                   'différents cours d\'eau (torrent de la Glière, du Dard et nant de la Crépéna, puis du ruisseau ' \
                   'd\'Isertan) — et le Doron de Chavière se rejoignent dans la commune. En aval, il conflue avec le ' \
                   'Doron de Champagny pour former le Doron de Bozel.\n\n\n=== Climat ===\nLa situation de ' \
                   'Pralognan-la-Vanoise, d\'une altitude d\'environ 1 400 m, la place dans un milieu continental ' \
                   'montagnard caractérisé par une humidité marquée. Les hivers sont plus froids et neigeux, ' \
                   'et la saison estivale douce avec parfois des épisodes orageux. '
        monkeypatch.setattr('GrandPyBotApp.functions.WikiMediaParseCom.TheWikiMediaParseCom.json_extract',
                            mock_json_extract)

        def mock_get_extract_from_api(self, title):
            return {'batchcomplete': '', 'query': {'pages': {'586449': {'pageid': 586449, 'ns': 0, 'title': 'Pralognan-la-Vanoise', 'extract': "Pralognan-la-Vanoise  est une commune française située dans le département de la Savoie, en région Auvergne-Rhône-Alpes. Village de montagne du massif de la Vanoise, en Tarentaise, il comptait 724 habitants en 2017.\nLe village est une station touristique d'été et de sports d'hiver installée au cœur du parc national de la Vanoise, proposant de nombreuses activités sportives de montagne, telles que la randonnée (les sentiers de grande randonnée GR 5 et GR 55 y passent) ou des via ferrata.\n\n\n== Géographie ==\n\n\n=== Situation ===\nPralognan-la-Vanoise est la dernière commune de la vallée de Bozel (Tarentaise). Le centre du village, situé à environ 1 400 mètres d'altitude, s'établit au confluent des vallées glaciaires de la Glière et de Chavière. Toutes deux constituent des points de passage vers la vallée de la Maurienne par le col de la Vanoise (2 517 mètres) ou le col de Chavière (2 796 mètres).\n\n\n=== Communes limitrophes ===\n\n\n=== Géologie et relief, hydrographie ===\n\nLe Doron de Pralognan — formé en amont de différents cours d'eau (torrent de la Glière, du Dard et nant de la Crépéna, puis du ruisseau d'Isertan) — et le Doron de Chavière se rejoignent dans la commune. En aval, il conflue avec le Doron de Champagny pour former le Doron de Bozel.\n\n\n=== Climat ===\nLa situation de Pralognan-la-Vanoise, d'une altitude d'environ 1 400 m, la place dans un milieu continental montagnard caractérisé par une humidité marquée. Les hivers sont plus froids et neigeux, et la saison estivale douce avec parfois des épisodes orageux."}}}}
        monkeypatch.setattr('GrandPyBotApp.functions.WikiMediaParseCom.TheWikiMediaParseCom.get_extract_from_api',
                            mock_get_extract_from_api)

        assert client.post('/conversation', data=dict(question=message_to_post)).status_code == 200

    def test_view_absurd_coordinates(self, client, monkeypatch):
        message_to_post = self.absurd_coordinates_to_post

        def mock_get_parsed_requested_question_from_coordinates(self, requested_coord):
            return 'Quelques part sur terre'
        monkeypatch.setattr('GrandPyBotApp.functions.parsedRequestedQuestionFromCoordinates'
                            '.ParsedRequestedQuestionFromCoordinates.get_parsed_requested_question_from_coordinates',
                            mock_get_parsed_requested_question_from_coordinates)

        def mock_parse_message_from_front(self, message_from_front):
            return 'Quelques part sur terre'
        monkeypatch.setattr('GrandPyBotApp.functions.Parse.Parser.parse_message_from_front',
                            mock_parse_message_from_front)

        def mock_get_coordinates_from_api(self, title):
            return {'results': [{'address_components': [{'long_name': 'Pralognan-la-Vanoise', 'short_name': 'Pralognan-la-Vanoise', 'types': ['locality', 'political']}, {'long_name': 'Savoie', 'short_name': 'Savoie', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Auvergne-Rhône-Alpes', 'short_name': 'Auvergne-Rhône-Alpes', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']}, {'long_name': '73710', 'short_name': '73710', 'types': ['postal_code']}], 'formatted_address': '73710 Pralognan-la-Vanoise, France', 'geometry': {'bounds': {'northeast': {'lat': 45.4171931, 'lng': 6.827487}, 'southwest': {'lat': 45.2687369, 'lng': 6.6337528}}, 'location': {'lat': 45.382062, 'lng': 6.721232}, 'location_type': 'APPROXIMATE', 'viewport': {'northeast': {'lat': 45.4171931, 'lng': 6.827487}, 'southwest': {'lat': 45.2687369, 'lng': 6.6337528}}}, 'place_id': 'ChIJ0cdEvZOciUcRAK665CqrCAQ', 'types': ['locality', 'political']}], 'status': 'OK'}
        monkeypatch.setattr('GrandPyBotApp.functions.googleMapCoordinates.Coordinates.get_coordinates_from_api',
                            mock_get_coordinates_from_api)

        def mock_get_formatted_address(self, data_coordinates):
            return 'Quelques part sur terre'
        monkeypatch.setattr('GrandPyBotApp.functions.googleMapCoordinates.Coordinates.get_formatted_address',
                            mock_get_formatted_address)

        def mock_get_image_from_api(self, coordinates):
            return ['https://maps.googleapis.com/maps/api/staticmap?center=45.393503599999995%2C+6.7251974&zoom=16'
                    '&size=350x350&key=AIzaSyAkPL6F9QLiACGJT3ettWsKIX0OoZHlsQc',
                    'https://maps.googleapis.com/maps/api/staticmap?center=45.393503599999995%2C+6.7251974&zoom=10'
                    '&size=350x350&key=AIzaSyAkPL6F9QLiACGJT3ettWsKIX0OoZHlsQc',
                    'https://maps.googleapis.com/maps/api/staticmap?center=45.393503599999995%2C+6.7251974&zoom=5'
                    '&size=350x350&key=AIzaSyAkPL6F9QLiACGJT3ettWsKIX0OoZHlsQc']
        monkeypatch.setattr('GrandPyBotApp.functions.GoogleMapParseCom.TheGoogleMapParseCom.get_image_from_api',
                            mock_get_image_from_api)

        monkeypatch.setattr('GrandPyBotApp.functions.RandomMessage.TheRandomMessage', lambda: 'J’y suis déjà allé. '
                                                                                              'C’était en 1963. '
                                                                                              'Évidemment, '
                                                                                              'depuis ça a changé ! ')

        def mock_get_title_from_api(self, message_to_api):
            return {'batchcomplete': '', 'continue': {'sroffset': 10, 'continue': '-||'}, 'query': {'searchinfo': {'totalhits': 128}, 'search': [{'ns': 0, 'title': 'Pralognan-la-Vanoise', 'pageid': 586449, 'size': 45723, 'wordcount': 4640, 'snippet': 'Pour les articles homonymes, voir <span class="searchmatch">Vanoise</span>. <span class="searchmatch">Pralognan</span>-<span class="searchmatch">la</span>-<span class="searchmatch">Vanoise</span> est une commune française située dans le département de <span class="searchmatch">la</span> Savoie, en région Auvergne-Rhône-Alpes', 'timestamp': '2020-09-15T02:02:21Z'}, {'ns': 0, 'title': 'Col de la Vanoise', 'pageid': 928898, 'size': 10187, 'wordcount': 1295, 'snippet': 'homonymes, voir <span class="searchmatch">Vanoise</span>. Le col de <span class="searchmatch">la</span> <span class="searchmatch">Vanoise</span> est un col des Alpes françaises culminant à 2\xa0517\xa0mètres dans le parc national de <span class="searchmatch">la</span> <span class="searchmatch">Vanoise</span>. Il permet l\'accès', 'timestamp': '2020-06-30T13:49:01Z'}, {'ns': 0, 'title': 'Massif de la Vanoise', 'pageid': 99158, 'size': 15514, 'wordcount': 1908, 'snippet': 'Pour les articles homonymes, voir <span class="searchmatch">Vanoise</span>. Le massif de <span class="searchmatch">la</span> <span class="searchmatch">Vanoise</span> est un massif montagneux des Alpes françaises, intégralement situé en Savoie. Il abrite', 'timestamp': '2020-09-16T16:55:15Z'}, {'ns': 0, 'title': 'Champagny-en-Vanoise', 'pageid': 677471, 'size': 12417, 'wordcount': 1341, 'snippet': 'Champagny et <span class="searchmatch">Vanoise</span>. Champagny-en-<span class="searchmatch">Vanoise</span> est une commune française située dans le département de <span class="searchmatch">la</span> Savoie, en région Auvergne-Rhône-Alpes. <span class="searchmatch">La</span> commune compte', 'timestamp': '2020-09-17T20:55:57Z'}, {'ns': 0, 'title': 'Parc national de la Vanoise', 'pageid': 69436, 'size': 29348, 'wordcount': 2386, 'snippet': 'voir <span class="searchmatch">Vanoise</span>. Parc national de <span class="searchmatch">la</span> <span class="searchmatch">Vanoise</span> Les glaciers de <span class="searchmatch">la</span> <span class="searchmatch">Vanoise</span>. modifier - modifier le code - modifier Wikidata Le parc national de <span class="searchmatch">la</span> <span class="searchmatch">Vanoise</span> est', 'timestamp': '2020-09-16T11:29:51Z'}, {'ns': 0, 'title': 'Hockey Courchevel Méribel Pralognan', 'pageid': 2991927, 'size': 7450, 'wordcount': 379, 'snippet': 'Pralognan-la-<span class="searchmatch">Vanoise</span>. Il évolue au troisième niveau national (Division 2) depuis <span class="searchmatch">la</span> saison 2018-2019. En 1964, le club de <span class="searchmatch">Pralognan</span>-<span class="searchmatch">la</span>-<span class="searchmatch">Vanoise</span> est fondé', 'timestamp': '2020-04-15T07:33:34Z'}, {'ns': 0, 'title': 'Vanoise', 'pageid': 96536, 'size': 1062, 'wordcount': 147, 'snippet': ' <span class="searchmatch">La</span> <span class="searchmatch">Vanoise</span> est un lieu des Alpes au sud de <span class="searchmatch">Pralognan</span> ayant donné son nom à plusieurs entités géographiques\xa0: Aiguille de <span class="searchmatch">la</span> <span class="searchmatch">Vanoise</span>, sommet de <span class="searchmatch">la</span> vallée', 'timestamp': '2020-08-24T13:34:32Z'}, {'ns': 0, 'title': 'Aiguille de la Vanoise', 'pageid': 1048095, 'size': 4465, 'wordcount': 404, 'snippet': '<span class="searchmatch">la</span> <span class="searchmatch">Vanoise</span> est un sommet du massif de <span class="searchmatch">la</span> <span class="searchmatch">Vanoise</span> dominant <span class="searchmatch">Pralognan</span>-<span class="searchmatch">la</span>-<span class="searchmatch">Vanoise</span>. Elle est réputée pour sa grande face nord de 300 à 400 m de haut. <span class="searchmatch">La</span> première', 'timestamp': '2020-04-19T16:28:46Z'}, {'ns': 0, 'title': 'Communauté de communes Val Vanoise', 'pageid': 7724796, 'size': 10665, 'wordcount': 497, 'snippet': 'communes de Champagny-en-<span class="searchmatch">Vanoise</span> et de <span class="searchmatch">Pralognan</span>-<span class="searchmatch">la</span>-<span class="searchmatch">Vanoise</span>. Depuis le 1er janvier 2014, <span class="searchmatch">la</span> communauté de communes Val <span class="searchmatch">Vanoise</span> Tarentaise remplace l\'ancien', 'timestamp': '2020-08-10T12:04:10Z'}, {'ns': 0, 'title': 'Lac des Vaches', 'pageid': 10416661, 'size': 5808, 'wordcount': 546, 'snippet': '1974, p.\xa0291 Rando <span class="searchmatch">Vanoise</span>, «\xa0Tour de l\'aiguille de <span class="searchmatch">la</span> <span class="searchmatch">Vanoise</span> et col de <span class="searchmatch">la</span> <span class="searchmatch">Vanoise</span> depuis <span class="searchmatch">Pralognan</span>-<span class="searchmatch">la</span>-<span class="searchmatch">Vanoise</span>\xa0», sur rando.<span class="searchmatch">vanoise</span>.com (consulté le 6', 'timestamp': '2019-06-23T08:02:38Z'}]}}
        monkeypatch.setattr('GrandPyBotApp.functions.WikiMediaParseCom.TheWikiMediaParseCom.get_title_from_api',
                            mock_get_title_from_api)

        def mock_json_title(self, media_wiki_request_search_result):
            return 'PQuelques part sur terre'
        monkeypatch.setattr('GrandPyBotApp.functions.WikiMediaParseCom.TheWikiMediaParseCom.json_title', mock_json_title)

        def mock_json_extract(self, media_wiki_request_extract_result):
            return 'Pralognan-la-Vanoise  est une commune française située dans le département de la Savoie, ' \
                   'en région Auvergne-Rhône-Alpes. Village de montagne du massif de la Vanoise, en Tarentaise, ' \
                   'il comptait 724 habitants en 2017.\nLe village est une station touristique d\'été et de sports ' \
                   'd\'hiver installée au cœur du parc national de la Vanoise, proposant de nombreuses activités ' \
                   'sportives de montagne, telles que la randonnée (les sentiers de grande randonnée GR 5 et GR 55 y ' \
                   'passent) ou des via ferrata.\n\n\n== Géographie ==\n\n\n=== Situation ===\nPralognan-la-Vanoise ' \
                   'est la dernière commune de la vallée de Bozel (Tarentaise). Le centre du village, situé à environ ' \
                   '1 400 mètres d\'altitude, s\'établit au confluent des vallées glaciaires de la Glière et de ' \
                   'Chavière. Toutes deux constituent des points de passage vers la vallée de la Maurienne par le col ' \
                   'de la Vanoise (2 517 mètres) ou le col de Chavière (2 796 mètres).\n\n\n=== Communes limitrophes ' \
                   '===\n\n\n=== Géologie et relief, hydrographie ===\n\nLe Doron de Pralognan — formé en amont de ' \
                   'différents cours d\'eau (torrent de la Glière, du Dard et nant de la Crépéna, puis du ruisseau ' \
                   'd\'Isertan) — et le Doron de Chavière se rejoignent dans la commune. En aval, il conflue avec le ' \
                   'Doron de Champagny pour former le Doron de Bozel.\n\n\n=== Climat ===\nLa situation de ' \
                   'Pralognan-la-Vanoise, d\'une altitude d\'environ 1 400 m, la place dans un milieu continental ' \
                   'montagnard caractérisé par une humidité marquée. Les hivers sont plus froids et neigeux, ' \
                   'et la saison estivale douce avec parfois des épisodes orageux. '
        monkeypatch.setattr('GrandPyBotApp.functions.WikiMediaParseCom.TheWikiMediaParseCom.json_extract', mock_json_extract)

        def mock_get_extract_from_api(self, title):
            return {'batchcomplete': '', 'query': {'pages': {'586449': {'pageid': 586449, 'ns': 0, 'title':
                'Pralognan-la-Vanoise', 'extract': "Pralognan-la-Vanoise  est une commune française située dans le "
                                                   "département de la Savoie, en région Auvergne-Rhône-Alpes. Village "
                                                   "de montagne du massif de la Vanoise, en Tarentaise, il comptait "
                                                   "724 habitants en 2017.\nLe village est une station touristique "
                                                   "d'été et de sports d'hiver installée au cœur du parc national de "
                                                   "la Vanoise, proposant de nombreuses activités sportives de "
                                                   "montagne, telles que la randonnée (les sentiers de grande "
                                                   "randonnée GR 5 et GR 55 y passent) ou des via ferrata.\n\n\n== "
                                                   "Géographie ==\n\n\n=== Situation ===\nPralognan-la-Vanoise est la "
                                                   "dernière commune de la vallée de Bozel (Tarentaise). Le centre du "
                                                   "village, situé à environ 1 400 mètres d'altitude, s'établit au "
                                                   "confluent des vallées glaciaires de la Glière et de Chavière. "
                                                   "Toutes deux constituent des points de passage vers la vallée de "
                                                   "la Maurienne par le col de la Vanoise (2 517 mètres) ou le col de "
                                                   "Chavière (2 796 mètres).\n\n\n=== Communes limitrophes "
                                                   "===\n\n\n=== Géologie et relief, hydrographie ===\n\nLe Doron de "
                                                   "Pralognan — formé en amont de différents cours d'eau (torrent de "
                                                   "la Glière, du Dard et nant de la Crépéna, puis du ruisseau "
                                                   "d'Isertan) — et le Doron de Chavière se rejoignent dans la "
                                                   "commune. En aval, il conflue avec le Doron de Champagny pour "
                                                   "former le Doron de Bozel.\n\n\n=== Climat ===\nLa situation de "
                                                   "Pralognan-la-Vanoise, d'une altitude d'environ 1 400 m, "
                                                   "la place dans un milieu continental montagnard caractérisé par "
                                                   "une humidité marquée. Les hivers sont plus froids et neigeux, "
                                                   "et la saison estivale douce avec parfois des épisodes orageux."}}}}
        monkeypatch.setattr('GrandPyBotApp.functions.WikiMediaParseCom.TheWikiMediaParseCom.get_extract_from_api',
                            mock_get_extract_from_api)

        assert client.post('/conversation', data=dict(question=message_to_post)).status_code == 200
