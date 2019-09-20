from app import db
from app.models import Message, Notification, Post, User
from datetime import datetime
from flask import current_app, flash, g, jsonify, render_template, redirect, request, url_for
from flask_babel import _, get_locale
from flask_login import current_user, login_required
from guess_language import guess_language
from . import blueprint
from .forms import EditProfileForm, MessageForm, PostForm, SearchForm


@blueprint.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
        g.search_form = SearchForm()

    g.locale = str(get_locale())


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
        current_app.config['POSTS_PER_PAGE'],
        False,
    )
    prev_url = url_for('main.index', page=posts.prev_num) if posts.has_prev else None
    next_url = url_for('main.index', page=posts.next_num) if posts.has_next else None
    return render_template(
        'main/index.html',
        title=_("Home"),
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
        current_app.config['POSTS_PER_PAGE'],
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
        title=_("Edit Profile"),
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
        current_app.config['POSTS_PER_PAGE'],
        False,
    )
    prev_url = url_for('main.explore', page=posts.prev_num) if posts.has_prev else None
    next_url = url_for('main.explore', page=posts.next_num) if posts.has_next else None
    return render_template(
        'main/index.html',
        title=_("Explore"),
        posts=posts.items,
        prev_url=prev_url,
        next_url=next_url,
    )


@blueprint.route('/search')
@login_required
def search():
    if not g.search_form.validate():
        return redirect(url_for('main.explore'))

    page = request.args.get('page', 1, type=int)
    posts, total = Post.search(g.search_form.q.data, page, current_app.config['POSTS_PER_PAGE'])
    last_item = page * current_app.config['POSTS_PER_PAGE']
    prev_url = url_for('main.search', q=g.search_form.q.data, page=page - 1) if page > 1 else None
    next_url = url_for('main.search', q=g.search_form.q.data, page=page + 1) if total > last_item else None
    return render_template(
        'main/search.html',
        title=_("Search"),
        posts=posts,
        prev_url=prev_url,
        next_url=next_url,
    )


@blueprint.route('/user/<username>/popup')
@login_required
def user_popup(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template(
        'main/user_popup.html',
        user=user,
    )


@blueprint.route('/send_message/<receiver>', methods=['GET', 'POST'])
@login_required
def send_message(receiver):
    user = User.query.filter_by(username=receiver).first_or_404()
    form = MessageForm()
    if form.validate_on_submit():
        message = Message(
            author=current_user,
            receiver=user,
            body=form.message.data,
        )
        db.session.add(message)
        user.add_notification('unread_messages_count', user.new_messages())
        db.session.commit()

        flash(_('Your message has been sent.'))
        return redirect(url_for('main.user_profile', username=receiver))
    return render_template(
        'main/send_message.html',
        title=_("Send Message"),
        form=form,
        receiver=receiver,
    )


@blueprint.route('/messages')
@login_required
def messages():
    current_user.last_message_read_time = datetime.utcnow()
    current_user.add_notification('unread_message_count', 0)
    db.session.commit()

    page = request.args.get('page', 1, type=int)
    messages = current_user.messages_received.order_by(
        Message.timestamp.desc(),
    ).paginate(
        page,
        current_app.config['POSTS_PER_PAGE'],
        False,
    )
    prev_url = url_for('main.messages', page=messages.prev_num) if messages.has_prev else None
    next_url = url_for('main.messages', page=messages.next_num) if messages.has_next else None
    return render_template(
        'main/messages.html',
        title=_("Messages"),
        messages=messages.items,
        prev_url=prev_url,
        next_url=next_url,
    )


@blueprint.route('/notifications')
@login_required
def notifications():
    since = request.args.get('since', 0.0, type=float)
    items = current_user.notifications.filter(
        Notification.timestamp > since
    ).order_by(
        Notification.timestamp.asc(),
    )
    return jsonify([{
        'name': item.name,
        'data': item.get_data(),
        'timestamp': item.timestamp,
    } for item in items])
