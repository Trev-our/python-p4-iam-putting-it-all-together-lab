from flask import session
from flask_restful import Resource
from models import User

class CheckSession(Resource):
    def get(self):
        user_id = session.get('user_id')
        if user_id:
            user = User.query.get(user_id)
            return user.to_dict(), 200
        return {'error': 'Unauthorized'}, 401
