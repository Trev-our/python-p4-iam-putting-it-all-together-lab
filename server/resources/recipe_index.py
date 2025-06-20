from flask import request, session
from flask_restful import Resource
from models import db, Recipe, User

class RecipeIndex(Resource):
    def get(self):
        if not session.get('user_id'):
            return {'error': 'Unauthorized'}, 401
        recipes = Recipe.query.all()
        return [r.to_dict() for r in recipes], 200

    def post(self):
        if not session.get('user_id'):
            return {'error': 'Unauthorized'}, 401

        data = request.get_json()
        try:
            recipe = Recipe(
                title=data['title'],
                instructions=data['instructions'],
                minutes_to_complete=data['minutes_to_complete'],
                user_id=session['user_id']
            )
            db.session.add(recipe)
            db.session.commit()
            return recipe.to_dict(), 201
        except Exception as e:
            return {'errors': [str(e)]}, 422
