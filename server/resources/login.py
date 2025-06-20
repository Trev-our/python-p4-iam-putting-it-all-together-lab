from flask import request, session
from flask_restful import Resource
from models import User

class Login(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()
        if user and user.authenticate(data['password']):
            session['user_id'] = user.id
            return user.to_dict(), 200
        return {'error': 'Invalid username or password'}, 401
