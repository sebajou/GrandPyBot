from GrandPyBotApp.tests.test_integration_functions.Parse import Parser


class TheGoogleMapParseCom(Parser):

    @staticmethod
    def get_image_from_api(coordinates):
        if coordinates == "48.8975156, 2.3833993":
            return ['https://maps.googleapis.com/maps/api/staticmap?center=48.8975156%2C+2.3833993&zoom=16&size=350x350&key=AIzaSyAkPL6F9QLiACGJT3ettWsKIX0OoZHlsQc', 'https://maps.googleapis.com/maps/api/staticmap?center=48.8975156%2C+2.3833993&zoom=10&size=350x350&key=AIzaSyAkPL6F9QLiACGJT3ettWsKIX0OoZHlsQc', 'https://maps.googleapis.com/maps/api/staticmap?center=48.8975156%2C+2.3833993&zoom=5&size=350x350&key=AIzaSyAkPL6F9QLiACGJT3ettWsKIX0OoZHlsQc']
        elif coordinates == "37.5398268, -107.777521":
            return ['https://maps.googleapis.com/maps/api/staticmap?center=37.5398268%2C+-107.777521&zoom=16&size=350x350&key=AIzaSyAkPL6F9QLiACGJT3ettWsKIX0OoZHlsQc', 'https://maps.googleapis.com/maps/api/staticmap?center=37.5398268%2C+-107.777521&zoom=10&size=350x350&key=AIzaSyAkPL6F9QLiACGJT3ettWsKIX0OoZHlsQc', 'https://maps.googleapis.com/maps/api/staticmap?center=37.5398268%2C+-107.777521&zoom=5&size=350x350&key=AIzaSyAkPL6F9QLiACGJT3ettWsKIX0OoZHlsQc']
        elif coordinates == "45.9996836, -73.9187669":
            return ['https://maps.googleapis.com/maps/api/staticmap?center=45.9996836%2C+-73.9187669&zoom=16&size=350x350&key=AIzaSyAkPL6F9QLiACGJT3ettWsKIX0OoZHlsQc', 'https://maps.googleapis.com/maps/api/staticmap?center=45.9996836%2C+-73.9187669&zoom=10&size=350x350&key=AIzaSyAkPL6F9QLiACGJT3ettWsKIX0OoZHlsQc', 'https://maps.googleapis.com/maps/api/staticmap?center=45.9996836%2C+-73.9187669&zoom=5&size=350x350&key=AIzaSyAkPL6F9QLiACGJT3ettWsKIX0OoZHlsQc']

