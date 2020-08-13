from flask import Flask, request, render_template, jsonify, session
from GrandPyBotApp.functions.Parse import Parser
from GrandPyBotApp.functions.WikiMediaParseCom import TheWikiMediaParseCom
from GrandPyBotApp.functions.googleMapCoordinates import Coordinates
from GrandPyBotApp.functions.RandomMessage import TheRandomMessage
from GrandPyBotApp.functions.GoogleMapParseCom import TheGoogleMapParseCom
from config import *
import json

app = Flask(__name__)

# Config options 
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE'] ex app.config['SECRET_KEY']
app.secret_key = SECRET_KEY


@app.route("/")
def index():
    return render_template("home.html")


@app.route('/conversation', methods=['POST'])
def conversation():

    if request.method == "POST":

        # Log in session
        session['username'] = "userNameSession"

        # Collect the question
        question = request.form["question"]
        print("La question : " + question)

        # Parse the question
        do_parser = Parser()
        parsed = do_parser.parse_message_from_front(question)
        parsed_requested_question = ""
        for element in parsed:
            parsed_requested_question = parsed_requested_question + " " + element

        # Display a Random message
        random_class = TheRandomMessage()
        random_message = random_class.random_message()

        # Get coordinates from parsed_requested_question
        api_request_coord = Coordinates()
        request_coord = api_request_coord.get_coordinates(parsed_requested_question)
        print(parsed_requested_question)

        # Request the API Wiki Media with the parsed element
        api_request = TheWikiMediaParseCom()
        api_response_json = api_request.get_title_from_api(parsed_requested_question)

        # Get the title from json
        api_response_title = api_request.json_title(api_response_json)
        print("api response title: ")
        print(api_response_title)

        # Get the extract from API with title
        extract_json = api_request.get_extract_from_api(api_response_title)
        extract = api_request.json_extract(extract_json)

        # Get google map images from API with coordinates
        api_google_map = TheGoogleMapParseCom()
        imgUrlList = api_google_map.get_image_from_api(request_coord)

        imgUrlList1 = imgUrlList[0]
        imgUrlList2 = imgUrlList[1]
        imgUrlList3 = imgUrlList[2]


        # Print all message for the front
        final_message = "<p style=\"color:#04fc6d;\">Vous : " + question + "<p/>" \
            + "<p style=\"color:#0417fc;\"> GrandPyBot : " + random_message \
            + "<p/>" + extract + "<br>"


        # Memorise old message
        if 'memMessage' not in session:
            session['memMessage'] = []

        session['memMessage'].append(final_message)
        session['memMessage'].reverse()
        listMemMessage = session['memMessage']

        return jsonify({'question': listMemMessage[0], 'imgUrlList1': imgUrlList1,
                        'imgUrlList2': imgUrlList2, 'imgUrlList3': imgUrlList3,
                        'memResponse': str(listMemMessage[1:]).strip('[]').strip(', ')})


if __name__ == "__main__":
    app.run(debug=True)
