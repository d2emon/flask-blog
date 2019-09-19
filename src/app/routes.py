import uuid
from app import app, db
from app.forms import EditProfileForm, PostForm
from app.models import Post, User
from app.translate import translate
from datetime import datetime
from flask import flash, g, jsonify, render_template, redirect, request, url_for
from flask_babel import _, get_locale
from flask_login import current_user, login_user, logout_user, login_required
from flask_wtf.csrf import generate_csrf
from guess_language import guess_language


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

    g.locale = str(get_locale())


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():
        language = guess_language(form.post.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        post = Post(
            body=form.post.data,
            author=current_user,
            language=language,
        )
        db.session.add(post)
        db.session.commit()

        flash(_('Your post is now live!'))
        return redirect(url_for('index'))
    page = request.args.get('page', 1, type=int)
    posts = current_user.followed_posts().paginate(
        page,
        app.config['POSTS_PER_PAGE'],
        False,
    )
    prev_url = url_for('index', page=posts.prev_num) if posts.has_prev else None
    next_url = url_for('index', page=posts.next_num) if posts.has_next else None
    return render_template(
        'index.html',
        title="Home",
        form=form,
        posts=posts.items,
        prev_url=prev_url,
        next_url=next_url,
    )


@app.route('/user/<username>')
@login_required
def user_profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    posts = user.posts.order_by(
        Post.timestamp.desc(),
    ).paginate(
        page,
        app.config['POSTS_PER_PAGE'],
        False,
    )
    prev_url = url_for('user_profile', page=posts.prev_num) if posts.has_prev else None
    next_url = url_for('user_profile', page=posts.next_num) if posts.has_next else None
    return render_template(
        'user.html',
        user=user,
        posts=posts.items,
        prev_url=prev_url,
        next_url=next_url,
    )


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()

        flash(_('Your changes have been saved.'))
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me

    return render_template(
        'edit_profile.html',
        title="Edit Profile",
        form=form,
    )


@app.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()

    if user is None:
        flash(_('User %(username)s not found.', username=username))
        return redirect(url_for('index'))

    if user == current_user:
        flash(_('You cannot follow yourself!'))
        return redirect(url_for('user_profile', username=current_user.username))

    current_user.follow(user)
    db.session.commit()
    flash(_('You are following %(username)s!', username=username))
    return redirect(url_for('user_profile', username=username))


@app.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()

    if user is None:
        flash(_('User %(username)s not found.', username=username))
        return redirect(url_for('index'))

    if user == current_user:
        flash(_('You cannot unfollow yourself!'))
        return redirect(url_for('user_profile', username=current_user.username))

    current_user.unfollow(user)
    db.session.commit()
    flash(_('You are not following %(username)s!', username=username))
    return redirect(url_for('user_profile', username=username))


@app.route('/explore')
def explore():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(
        Post.timestamp.desc(),
    ).paginate(
        page,
        app.config['POSTS_PER_PAGE'],
        False,
    )
    prev_url = url_for('explore', page=posts.prev_num) if posts.has_prev else None
    next_url = url_for('explore', page=posts.next_num) if posts.has_next else None
    return render_template(
        'index.html',
        title="Explore",
        posts=posts.items,
        prev_url=prev_url,
        next_url=next_url,
    )


@app.route('/translate', methods=['POST'])
@login_required
def translate_text():
    return jsonify({'text': translate(
        request.form['text'],
        request.form['source_language'],
        request.form['dest_language'],
    )})


# API


@app.route('/api')
def api():
    return jsonify({
        'csrf_token': generate_csrf(),
    })


@app.route('/api/index')
@login_required
def api_index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!',
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!',
        },
        {
            'author': {'username': 'Hippolite'},
            'body': 'People=shit!',
        },
        {
            'id': uuid.uuid4(),
            'slug': 'post-1',
            'author': {
                'firstName': 'First',
                'lastName': 'Last',
            },
            'title': 'Post 1',
            'date': '01 May 2017',
            'summary': 'Post 1',
            'body': 'Post',
            'image': 'https://image.ibb.co/bF9iO5/1.jpg',
        },
        {
            'id': uuid.uuid4(),
            'slug': 'post-2',
            'author': {
                'firstName': 'First',
                'lastName': 'Last',
            },
            'title': 'Post 2',
            'date': '01 May 2017',
            'summary': 'Post 2',
            'body': 'Post',
            'image': 'https://image.ibb.co/bF9iO5/1.jpg',
        },
        {
            'id': uuid.uuid4(),
            'slug': 'post-3',
            'author': {
                'firstName': 'First',
                'lastName': 'Last',
            },
            'title': 'Post 3',
            'date': '01 May 2017',
            'summary': 'Post 3',
            'body': 'Post',
            'image': 'https://image.ibb.co/bF9iO5/1.jpg',
        },
    ]
    return jsonify({
        'csrf_token': generate_csrf(),
        'title': 'Home',
        'messages': [],
        'user': current_user,
        'posts': posts,
    })


@app.route('/api/login', methods=['GET', 'POST'])
def api_login():
    if current_user.is_authenticated:
        return jsonify({'authenticated': True})

    form = LoginForm()
    authenticated = form.validate_on_submit()
    messages = []
    errors = form.errors

    if authenticated:
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            errors['username'] = "Invalid username or password"
            errors['password'] = "Invalid username or password"
        else:
            login_user(user, remember=form.remember_me.data)
            messages.append(
                "Login requested for user {username}, remember_me={remember_me}".format(**form.data)
            )

    return jsonify({
        'authenticated': authenticated,
        'errors': errors,
        'messages': messages,
    })


@app.route('/api/logout')
def api_logout():
    logout_user()
    return jsonify({'authenticated': False})


@app.route('/api/register', methods=['GET', 'POST'])
def api_register():
    if current_user.is_authenticated:
        return jsonify({'registered': False})

    form = RegistrationForm()
    registered = form.validate_on_submit()
    messages = []
    if registered:
        user = User(
            username=form.username.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        messages.append("Congratulations, you are now a registered user!")

    return jsonify({
        'registered': registered,
        'errors': form.errors,
        'messages': messages,
    })
