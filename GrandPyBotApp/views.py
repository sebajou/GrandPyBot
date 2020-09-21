from flask import Flask, request, render_template, jsonify
from GrandPyBotApp.functions.Parse import Parser
from GrandPyBotApp.functions.WikiMediaParseCom import TheWikiMediaParseCom
from GrandPyBotApp.functions.googleMapCoordinates import Coordinates
from GrandPyBotApp.functions.RandomMessage import TheRandomMessage
from GrandPyBotApp.functions.GoogleMapParseCom import TheGoogleMapParseCom
from GrandPyBotApp.functions.parsedRequestedQuestionFromCoordinates import ParsedRequestedQuestionFromCoordinates
from config import *
import re

app = Flask(__name__)

# Config options 
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE'] ex app.config['SECRET_KEY']
app.secret_key = SECRET_KEY


@app.route("/")
def index():
    """Root routes"""
    return render_template("home.html")


@app.route('/conversation', methods=['POST'])
def conversation():
    """Main URL. Allow AJAX data exchange with front"""

    if request.method == "POST":

        # Collect the question
        question = request.form["question"]
        print("La question : " + question)

        # Control if question content coordinates
        regexp = re.compile(r'^(-?\d+(\.\d+)?),\s*(-?\d+(\.\d+)?)$')
        request_coord = ""
        parsed_requested_question = ""
        regex_not_catch = True
        if regexp.search(question):
            # Allow to obtain map from shared location
            request_coord = question
            # Give to parsed_requested_question variable a title from share location
            par_req_qu = ParsedRequestedQuestionFromCoordinates()
            parsed_requested_question = par_req_qu.get_parsed_requested_question_from_coordinates(request_coord)
            regex_not_catch = False

        # Parse the question if regex is not catch
        if regex_not_catch:
            do_parser = Parser()
            parsed = do_parser.parse_message_from_front(question)
            for element in parsed:
                parsed_requested_question = parsed_requested_question + " " + element

        # Display a Random message
        random_class = TheRandomMessage()
        random_message = random_class.random_message()

        # Get coordinates from parsed_requested_question
        api_request_coord = Coordinates()
        if regex_not_catch:
            request_coord = api_request_coord.get_coordinates(parsed_requested_question)

        # Request the API Wiki Media with the parsed element
        api_request = TheWikiMediaParseCom()
        api_response_json = api_request.get_title_from_api(parsed_requested_question)

        # Get the title from json
        api_response_title = api_request.json_title(api_response_json)

        # Extract formatted address from requested coordinates
        coord = api_request_coord.get_coordinates_from_api(api_response_title)
        formatted_address = api_request_coord.get_formatted_address(coord)

        # Get the extract from API with title
        extract_json = api_request.get_extract_from_api(api_response_title)
        extract = api_request.json_extract(extract_json)

        # Get google map images from API with coordinates
        api_google_map = TheGoogleMapParseCom()
        img_url_list = api_google_map.get_image_from_api(request_coord)

        img_url_list1 = img_url_list[0]
        img_url_list2 = img_url_list[1]
        img_url_list3 = img_url_list[2]

        # Message in case of empty request
        if api_response_title == "Empty request":
            final_message = "<br><ul><p style=\"color:#04fc6d;\">Vous : " + question + "<p/>" \
                            + "<p style=\"color:#0417fc;\"> GrandPyBot : " \
                            + "Je n'ai pas bien entendu ta question. Tu as dit quelque chose ? " \
                            + "<p/>"
        # If the request is bad, the api response titile is Atlantide
        elif api_response_title == "Atlantide":
            final_message = "<br><ul><p style=\"color:#04fc6d;\">Vous : " + question + "<p/>" \
                            + "<p style=\"color:#0417fc;\"> GrandPyBot : " \
                              " Je n'ai pas bien entendu ta question. " \
                              "Tu veux parler de l'île cachée de l'Atlantide ? " \
                            + random_message \
                            + " J'ai l'adresse. Garde-la pour toi, elle est secrète : " + formatted_address + "<p/>" \
                            + "<p style=\"color:#0417fc;\">" + extract + "<p/><ul/>"

        # Print all message for the front is case of satisfactory question
        else:
            final_message = "<br><ul><p style=\"color:#04fc6d;\">Vous : " + question + "<p/>" \
                            + "<p style=\"color:#0417fc;\">GrandPyBot : " + random_message \
                            + "Cet endroit se trouve à l'adresse : " + formatted_address + "<p/>" \
                            + "<p style=\"color:#0417fc;\">" + extract + "<p/><ul/>"

        # Json return to front with AJAX
        return jsonify({'question': final_message, 'imgUrlList1': img_url_list1,
                        'imgUrlList2': img_url_list2, 'imgUrlList3': img_url_list3})
