import pytest
from GrandPyBotApp.views import app


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


class TestRoutes:
    """ Test get, post and route of application"""

    def setup_method(self):
        self.normal_to_post = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
        self.absurd_to_post = "dsqgrr(5éht"
        self.empty_to_post = ""
        self.coordinates_to_post = "45.393503599999995, 6.7251974"
        self.absurd_coordinates_to_post = "-96.393503599999995, 566.7251974"

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

    def test_view_coordinates(self, client):
        message_to_post = self.coordinates_to_post

        assert client.post('/conversation', data=dict(question=message_to_post)).status_code == 200

    def test_view_absurd_coordinates(self, client):
        message_to_post = self.absurd_coordinates_to_post

        assert client.post('/conversation', data=dict(question=message_to_post)).status_code == 200
