from flask import Flask

app = Flask(__name__)

# Config options 
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE'] ex app.config['SECRET_KEY']

@app.route('/')
def index():
    return "Hello world !"

if __name__ == "__main__":
    app.run()
