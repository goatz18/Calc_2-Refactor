from app.controllers.controller import ControllerBase
from flask import render_template

class IndexController(ControllerBase):
    @staticmethod
    def get():
        return render_template('index.html')

class BehindTheWebController(ControllerBase):
    @staticmethod
    def get():
        return render_template('behindtheweb.html')

class SearchEngineWarsController(ControllerBase):
    @staticmethod
    def get():
        return render_template('search.html')

class OopOopController(ControllerBase):
    @staticmethod
    def get():
        return render_template('oopoop.html')

class OopSelect(ControllerBase):
    @staticmethod
    def get():
        return render_template('oopselect.html')

class TestController(ControllerBase):
    @staticmethod
    def get():
        return render_template('test.html')