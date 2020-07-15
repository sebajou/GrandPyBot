from flask import Flask, request, render_template, url_for
from GrandPyBotApp.functions.Parse import Parser
from GrandPyBotApp.functions.WikiMediaParseCom import TheWikiMediaParseCom
from GrandPyBotApp.functions.googleMapCoordinates import Coordinates
import json

app = Flask(__name__)

# Config options 
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE'] ex app.config['SECRET_KEY']


"""@app.route("/")
def index():
    return render_template("home.html")


@app.route("/conversation", methods=["GET", "POST"])
def conversation():"""


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("home.html")

    if request.method == "POST":
        # Collect the question
        question = request.form["question"]
        print("La question : " + question)

        # Parse the question
        do_parser = Parser()
        parsed = do_parser.parse_message_from_front(question)
        parsed_requested_question = ""
        for element in parsed:
            parsed_requested_question = parsed_requested_question + element
            print(element)

        # Get coordinates from parsed_requested_question
        api_request_coord = Coordinates()
        request_coord = api_request_coord.get_coordinates(parsed_requested_question)
        print("Requested coordinates: ", request_coord)

        # Request the API Wiki Media with the parsed element
        api_request = TheWikiMediaParseCom()
        api_response_json = api_request.get_title_from_api(parsed_requested_question)
        print("api response json: ")
        print(api_response_json)
        # Get the title from json
        api_response_title = api_request.json_title(api_response_json)
        print("api response title: ")
        print(api_response_title)

        return render_template("home.html")


if __name__ == "__main__":
    app.run()
