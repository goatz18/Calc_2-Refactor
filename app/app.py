"""A simple flask web app"""
from flask import Flask, flash, render_template, request
from app.controllers.index_controller import IndexController
from app.controllers.index_controller import BehindTheWebController
from app.controllers.index_controller import SearchEngineWarsController
from app.controllers.index_controller import OopOopController
from app.controllers.index_controller import OopSelect
from app.controllers.index_controller import TestController
from app.controllers.calculator_controller import CalculatorController
from werkzeug.debug import DebuggedApplication

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

if __name__ == '__maain__':
    app.run(debug=True)

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()

@app.route("/behindtheweb", methods=['GET'])
def behind_the_web_get():
    return BehindTheWebController.get()

@app.route("/search", methods=['GET'])
def search_get():
    return SearchEngineWarsController.get()

@app.route("/oopoop", methods=['GET'])
def oopoop_get():
    return OopOopController.get()

@app.route("/oopselect", methods=['GET'])
def oopselect_get():
    return OopSelect.get()

@app.route("/test", methods=['GET'])
def test_get():
    return TestController.get()

#@app.route("/calculator")
#def divide_by_zero():

#    flash("flash test!!!!")
#    return render_template("index.html")
