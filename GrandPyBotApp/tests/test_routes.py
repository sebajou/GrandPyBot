import pytest
from GrandPyBotApp.views import app

app.testing = True
client = app.test_client()


class TestRoutes:
    """ Test get, post and route of application"""

    def setup_method(self):
        self.normal_to_post = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
        self.absurd_to_post = "dsqgrr(5éht"
        self.empty_to_post = ""

    @staticmethod
    def test_view_home():
        with app.test_client() as c:
            assert c.get('/').status_code == 200

    def test_view(self):
        to_post = self.normal_to_post
        with app.test_client() as c:
            assert c.post('/conversation', data=dict(question=to_post)).status_code == 200

    def test_view_absurd(self):
        to_post = self.absurd_to_post
        with app.test_client() as c:
            assert c.post('/conversation', data=dict(question=to_post)).status_code == 200

    def test_view_empty(self):
        to_post = self.empty_to_post
        with app.test_client() as c:
            assert c.post('/conversation', data=dict(question=to_post)).status_code == 200

