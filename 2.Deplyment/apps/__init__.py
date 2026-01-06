from flask import Flask
from apps import routes

def create_app():
    app = Flask(__name__)