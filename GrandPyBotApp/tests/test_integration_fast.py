import pytest
from GrandPyBotApp.views import app
from GrandPyBotApp import conftest


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


class TestIntegration:
    """ Test get, post and route of application"""

    def setup_method(self):
        self.normal_to_post = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
        self.absurd_to_post = "dsqgrr(5éht"
        self.empty_to_post = ""
        self.json_from_normal_to_post = {
            "imgUrlList1": "https://maps.googleapis.com/maps/api/staticmap?center=48.8975156%2C+2.3833993&zoom=16&size=350x350&key=AIzaSyAkPL6F9QLiACGJT3ettWsKIX0OoZHlsQc",
            "imgUrlList2": "https://maps.googleapis.com/maps/api/staticmap?center=48.8975156%2C+2.3833993&zoom=10&size=350x350&key=AIzaSyAkPL6F9QLiACGJT3ettWsKIX0OoZHlsQc",
            "imgUrlList3": "https://maps.googleapis.com/maps/api/staticmap?center=48.8975156%2C+2.3833993&zoom=5&size=350x350&key=AIzaSyAkPL6F9QLiACGJT3ettWsKIX0OoZHlsQc",
            "question": "<br><p style=\"color:#04fc6d;\">Vous : Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?<p/><p style=\"color:#0417fc;\"> GrandPyBot : J’y suis déjà allé. C’était en 1963. Évidemment, depuis ça a changé !  Cette endroit se trouve à l'adresse : 10 Quai de la Charente, 75019 Paris, France<p/>OpenClassrooms est un site web de formation en ligne qui propose à ses membres des cours certifiants et des parcours débouchant sur des métiers en croissance. Ses contenus sont réalisés en interne, par des écoles, des universités, des entreprises partenaires comme Microsoft ou IBM, ou historiquement par des bénévoles. Jusqu'en 2018, n'importe quel membre du site pouvait être auteur, via un outil nommé « interface de rédaction » puis « Course Lab ». De nombreux cours sont issus de la communauté, mais ne sont plus mis en avant. Initialement orientée autour de la programmation informatique, la plate-forme couvre depuis 2013 des thématiques plus larges tels que le marketing, l'entrepreneuriat et les sciences.\nCréé en 1999 sous le nom de Site du Zéro, il se forme essentiellement sur la base de contributions de bénévoles proposant des tutoriels vulgarisés avec un ton léger portant sur des sujets informatiques divers. À la suite du succès et de la fin des études des gérants, l'entreprise Simple IT, renommée ensuite OpenClassrooms, est fondée dans le but de pérenniser le site. Celle-ci base son modèle économique sur la délivrance de certifications payantes et propose un abonnement pour être suivi par un mentor,. Suite à ces changements, des utilisateurs créent un site web aux buts similaires, dont les auteurs et l'association le gérant sont uniquement bénévoles et ne propose pas de certifications (Zeste de Savoir).\n\n\n== Fonctionnement ==\nLe site propose un catalogue de plus de 1 000 tutoriels accessibles en ligne.<br> "
        }

    @staticmethod
    def test_view_home(client):
        assert client.get('/').status_code == 200

    def test_view(self, client):
        message_to_post = self.normal_to_post
        assert client.post('/conversation', data=dict(question=message_to_post)).status_code == 200

    def test_view_absurd(self, client):
        message_to_post = self.absurd_to_post
        assert client.post('/conversation', data=dict(question=message_to_post)).status_code == 200

    def test_view_empty(self, client):
        message_to_post = self.empty_to_post
        assert client.post('/conversation', data=dict(question=message_to_post)).status_code == 200

