from app import app, db
from app.models import Post, User
from flask import flash, jsonify, render_template, redirect, request, url_for
from flask_babel import _
from flask_login import current_user, login_required
from guess_language import guess_language
from . import blueprint
from .forms import EditProfileForm, PostForm
from .translate import translate


@blueprint.route('/', methods=['GET', 'POST'])
@blueprint.route('/index', methods=['GET', 'POST'])
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
        return redirect(url_for('main.index'))
    page = request.args.get('page', 1, type=int)
    posts = current_user.followed_posts().paginate(
        page,
        app.config['POSTS_PER_PAGE'],
        False,
    )
    prev_url = url_for('main.index', page=posts.prev_num) if posts.has_prev else None
    next_url = url_for('main.index', page=posts.next_num) if posts.has_next else None
    return render_template(
        'main/index.html',
        title="Home",
        form=form,
        posts=posts.items,
        prev_url=prev_url,
        next_url=next_url,
    )


@blueprint.route('/user/<username>')
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
    prev_url = url_for('main.user_profile', page=posts.prev_num) if posts.has_prev else None
    next_url = url_for('main.user_profile', page=posts.next_num) if posts.has_next else None
    return render_template(
        'main/user.html',
        user=user,
        posts=posts.items,
        prev_url=prev_url,
        next_url=next_url,
    )


@blueprint.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()

        flash(_('Your changes have been saved.'))
        return redirect(url_for('main.edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me

    return render_template(
        'main/edit_profile.html',
        title="Edit Profile",
        form=form,
    )


@blueprint.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()

    if user is None:
        flash(_('User %(username)s not found.', username=username))
        return redirect(url_for('main.index'))

    if user == current_user:
        flash(_('You cannot follow yourself!'))
        return redirect(url_for('main.user_profile', username=current_user.username))

    current_user.follow(user)
    db.session.commit()
    flash(_('You are following %(username)s!', username=username))
    return redirect(url_for('main.user_profile', username=username))


@blueprint.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()

    if user is None:
        flash(_('User %(username)s not found.', username=username))
        return redirect(url_for('main.index'))

    if user == current_user:
        flash(_('You cannot unfollow yourself!'))
        return redirect(url_for('main.user_profile', username=current_user.username))

    current_user.unfollow(user)
    db.session.commit()
    flash(_('You are not following %(username)s!', username=username))
    return redirect(url_for('main.user_profile', username=username))


@blueprint.route('/explore')
def explore():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(
        Post.timestamp.desc(),
    ).paginate(
        page,
        app.config['POSTS_PER_PAGE'],
        False,
    )
    prev_url = url_for('main.explore', page=posts.prev_num) if posts.has_prev else None
    next_url = url_for('main.explore', page=posts.next_num) if posts.has_next else None
    return render_template(
        'main/index.html',
        title="Explore",
        posts=posts.items,
        prev_url=prev_url,
        next_url=next_url,
    )


@blueprint.route('/translate', methods=['POST'])
@login_required
def translate_text():
    return jsonify({'text': translate(
        request.form['text'],
        request.form['source_language'],
        request.form['dest_language'],
    )})