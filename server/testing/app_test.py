import json
from os import environ
from flask import request

from app import app
from models import db, Research, Author, ResearchAuthors

class TestApp:
    '''Flask application in app.py'''

    