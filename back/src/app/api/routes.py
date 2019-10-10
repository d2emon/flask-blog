import random
from app import db
from app.models import User
from app.auth.forms import LoginForm
from flask import current_app, jsonify, request, url_for
from flask_login import current_user, login_user
from . import blueprint
from .auth import token_auth
from .errors import bad_request
from .articles import articles_data
from .check import check_all


def enter_blog(user):
    current_app.logger.info(
        "Blog entry by {} : UID {}".format(
            user.username,
            user.user_id,
        ),
    )


@blueprint.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    # TODO: Find by Username
    # TODO: Validate Username
    return jsonify(User.query.get_or_404(user_id).to_dict())


@blueprint.route('/users', methods=['GET'])
@token_auth.login_required
def get_users():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = User.to_collection_dict(User.query, page, per_page, 'api.get_users')
    return jsonify(data)


@blueprint.route('/users/<user_id>/followers', methods=['GET'])
@token_auth.login_required
def get_followers(user_id):
    user = User.query.get_or_404(user_id)
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = User.to_collection_dict(user.followers, page, per_page, 'api.get_followers', user_id=user_id)
    return jsonify(data)


@blueprint.route('/users/<user_id>/followed', methods=['GET'])
@token_auth.login_required
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
    # TODO: Enter system on registration
    return response


@blueprint.route('/users/<user_id>', methods=['PUT'])
@token_auth.login_required
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


@blueprint.route('/articles', methods=['GET'])
def get_articles():
    start = request.args.get('start', 0, type=int)
    count = request.args.get('count', 10, type=int)
    articles = articles_data[start:start + count]
    return jsonify({
        'articles': articles,
        'total': len(articles_data),
    })


@blueprint.route('/categories', methods=['GET'])
def get_categories():
    count = request.args.get('count', 10, type=int)
    categories = []
    for article in articles_data:
        text = article.get('category')
        if not text:
            continue

        category = next((category for category in categories if category.get('text') == text), None)
        if category:
            category['postsCount'] = category.get('postsCount', 0) + 1
            continue
        categories.append({
            'categoryId': len(categories) + 1,
            'text': text,
            'to': "/category/{}".format(text),
            'postsCount': 1,
        })
    categories.sort(key=lambda c: c.get('text', ''))
    return jsonify({
        'categories': categories[0:count],
        'total': len(categories),
    })


@blueprint.route('/instagram', methods=['GET'])
def instagram():
    return jsonify([
        {'src': src}
        for src in [
            'adventurealtitude.jpg',
            'garden.jpg',
            'pigduck.jpg',
            'rain.jpg',
            'spices.jpg',
            'sunset.jpg',
        ]
    ])


@blueprint.route('/tags', methods=['GET'])
def tags():
    return jsonify([
        {'tagId': tag_id + 1, 'name': "Tag {}".format(tag_id + 1)}
        for tag_id in range(35)
    ])


@blueprint.route('/notifications', methods=['GET'])
def notifications():
    return jsonify([
        "Message {}".format(message_id)
        for message_id in range(random.randrange(5))
    ] if random.randrange(10) > 8 else [])


@blueprint.route('/login', methods=['POST'])
def login():
    if current_user.is_authenticated:
        return jsonify({'errors': False})

    form = LoginForm(csrf_enabled=False)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            return jsonify({'errors': ['Invalid username or password']})

        login_user(user, remember=form.remember_me.data)
        return jsonify({
            'errors': False,
            'token': current_user.get_token() if current_user.is_authenticated else None,
        })

    return jsonify({'errors': form.errors})


# TODO: Add api to password change


@blueprint.route('/check', methods=['GET'])
def check():
    user_id = request.args.get('userId')
    hostname = request.args.get('hostname')

    try:
        return jsonify({
            'success': check_all(user_id, hostname),
            'createdAt': None,
            'startedAt': None,
        })
    except Exception as e:
        return jsonify({
            'error':  str(e)
        })
