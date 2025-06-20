from flask import Flask, session
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS

from models import db
from config import Config

# Ensure these are relative to the server directory (and that resources/__init__.py exists)
from resources.signup import Signup
from resources.login import Login
from resources.logout import Logout
from resources.check_session import CheckSession
from resources.recipe_index import RecipeIndex

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Enable CORS with credentials (cookies/session)
CORS(app, supports_credentials=True)

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

# Register API resource routes
api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(CheckSession, '/check_session')
api.add_resource(RecipeIndex, '/recipes')

# Root route
@app.route('/')
def index():
    return {'message': 'Flask API Running'}
