from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object("config")
app.secret_key = '\xf0&#\xf2\xdb\xf2\x0b9\x10\x147\xce\xb2\xc2\x7fB\x13A>\xfdG\xaa\xca\xd3'

db = MongoEngine(app)

from app import views, models
