from flask import request, session
from flask_restful import Resource
from models import db, User

class Signup(Resource):
    def post(self):
        data = request.get_json()

        try:
            user = User(
                username=data['username'],
                image_url=data['image_url'],
                bio=data['bio']
            )
            user.password_hash = data['password']
            db.session.add(user)
            db.session.commit()

            session['user_id'] = user.id

            return user.to_dict(), 201

        except Exception as e:
            return {'errors': [str(e)]}, 422
