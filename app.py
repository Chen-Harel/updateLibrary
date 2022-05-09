import enum
from msilib.schema import Class
from flask import Flask, render_template
from enum import Enum, auto

app = Flask(__name__)

class Books(Enum):
    HARRY_POTTER_AND_THE_SORCERERS_STONE = auto()
    HARRY_POTTER_AND_THE_CHAMBER_OF_SECRETS = auto()
    THE_HUNGER_GAMES = auto()
    THE_LORD_OF_THE_RINGS_THE_FELLOWSHIP_OF_THE_RING = auto()

class Customers(Enum):
    John = auto()
    Becky = auto()
    Jane = auto()
    Michael = auto()
    Jason = auto()



book = Books
customer = Customers

@app.route("/")
def index():
    return render_template("index.html", book=book, customer=customer)


if __name__ == "__main__": 
    app.run(debug=True)