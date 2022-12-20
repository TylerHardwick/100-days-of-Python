from flask import Flask
from random import randint


RANDOM_NUMBER = randint(1, 10)


app = Flask(__name__)


@app.route("/")
def homepage():
    return "<h1 style='text-align: center'>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route("/<number>")
def check_number(number):
    try:
        if int(number) == RANDOM_NUMBER:
            return "<h1 style='color:green'>You found me!</h1>" \
                   "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
        elif int(number) < RANDOM_NUMBER:
            return "<h1 style='color:red'>Too low, try again!</h1>" \
                   "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
        elif int(number) > RANDOM_NUMBER:
            return "<h1 style='color:purple'>Too high, try again!</h1>" \
                   "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    except ValueError:
        return "<h1 style='color:orange'>That's not a number between 1-9! What are you doing?</h1>" \
               "<img src='https://media.giphy.com/media/fQfS2YYFQgvQACkRPV/giphy-downsized-large.gif'>"





if __name__ == "__main__":
    app.run(debug=True)