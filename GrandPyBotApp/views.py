from flask import Flask, request, render_template, url_for
from GrandPyBotApp.functions.Parse import Parser
from GrandPyBotApp.functions.WikiMediaParseCom import TheWikiMediaParseCom
import json

app = Flask(__name__)

# Config options 
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE'] ex app.config['SECRET_KEY']


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

        # Request the API Wiki Media
        api_request = TheWikiMediaParseCom()
        api_response_json = api_request.get_title_from_api(parsed_requested_question)
        print(api_response_json)
        results_string = json.dumps(api_response_json)
        results_bytes = results_string.encode()
        api_response_title = api_request.json_title(results_bytes)
        print(api_response_title)

        return render_template("home.html")


if __name__ == "__main__":
    app.run()
