from app import db
from app.models import User
from flask import jsonify, request, url_for
from . import blueprint
from .errors import bad_request


@blueprint.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify(User.query.get_or_404(user_id).to_dict())


@blueprint.route('/users', methods=['GET'])
def get_users():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = User.to_collection_dict(User.query, page, per_page, 'api.get_users')
    return jsonify(data)


@blueprint.route('/users/<user_id>/followers', methods=['GET'])
def get_followers(user_id):
    user = User.query.get_or_404(user_id)
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = User.to_collection_dict(user.followers, page, per_page, 'api.get_followers', user_id=user_id)
    return jsonify(data)


@blueprint.route('/users/<user_id>/followed', methods=['GET'])
def get_followed(user_id):
    user = User.query.get_or_404(user_id)
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = User.to_collection_dict(user.followed, page, per_page, 'api.get_followed', user_id=user_id)
    return jsonify(data)


@blueprint.route('/users', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    required = ('username', 'email', 'password')
    if any(field not in data for field in required):
        return bad_request('must include username, email and password fields')
    if User.query.filter_by(username=data['username']).first():
        return bad_request('please use a different username')
    if User.query.filter_by(email=data['email']).first():
        return bad_request('please use a different email address')
    user = User()
    user.from_dict(data, new_user=True)
    db.session.add(user)
    db.session.commit()
    response = jsonify(user.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.get_user', user_id=user.user_id)
    return response


@blueprint.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id=None):
    user = User.query.get_or_404(user_id)
    data = request.get_json() or {}
    username_changed = 'username' in data and data['username'] != user.username
    if username_changed and User.query.filter_by(username=data['username']).first():
        return bad_request('please use a different username')
    email_changed = 'email' in data and data['email'] != user.email
    if username_changed and User.query.filter_by(email=data['email']).first():
        return bad_request('please use a different email address')
    user.from_dict(data, new_user=False)
    db.session.commit()
    return jsonify(user.to_dict())
