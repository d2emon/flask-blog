from app import db
from app.models import User
from flask import flash, jsonify, render_template, redirect, request, url_for
from flask_babel import _
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse
from . import blueprint
from .forms import LoginForm, RegistrationForm, ResetPasswordForm, ResetPasswordRequestForm
from .mail import send_password_reset_email


def do_register(form):
    messages = []
    success = current_user.is_authenticated
    user = current_user if current_user.is_authenticated else None

    if not success and form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        success = True
        messages.append(_('Congratulations, you are now a registered user!'))

    return {
        'errors': form.errors,
        'messages': messages,
        'success': success,
        'user': user and user.get_token(),
    }


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(_('Invalid username or password'))
            return redirect(url_for('auth.login'))

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)

    return render_template(
        'auth/login.html',
        title="Sign In",
        form=form,
    )


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST' and request.json.get('api'):
        return jsonify(do_register(RegistrationForm(csrf_enabled=False)))

    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = RegistrationForm()
    data = do_register(form)
    if data.get('success'):
        for message in data.get('messages', []):
            flash(message)
        return redirect(url_for('auth.login'))

    return render_template(
        'auth/register.html',
        title="Register",
        form=form,
    )


@blueprint.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)

        flash(_('Check your email for the instructions to reset your password'))
        return redirect(url_for('auth.login'))

    return render_template(
        'auth/reset_password_request.html',
        title="Reset Password",
        form=form,
    )


@blueprint.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('auth.login'))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()

        flash(_('Your password has been reset.'))
        return redirect(url_for('auth.login'))

    return render_template(
        'auth/reset_password.html',
        form=form,
    )


@blueprint.route('/api-login', methods=['GET', 'POST'])
def api_login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(_('Invalid username or password'))
            return redirect(url_for('auth.login'))

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)

    return render_template(
        'auth/login.html',
        title="Sign In",
        form=form,
    )


@blueprint.route('/api-logout')
def api_logout():
    logout_user()
    return redirect(url_for('main.index'))


@blueprint.route('/api-register', methods=['GET', 'POST'])
def api_register():
    return jsonify(do_register(RegistrationForm(csrf_enabled=False)))


@blueprint.route('/api-reset_password_request', methods=['GET', 'POST'])
def api_reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)

        flash(_('Check your email for the instructions to reset your password'))
        return redirect(url_for('auth.login'))

    return render_template(
        'auth/reset_password_request.html',
        title="Reset Password",
        form=form,
    )


@blueprint.route('/api-reset_password/<token>', methods=['GET', 'POST'])
def api_reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('auth.login'))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()

        flash(_('Your password has been reset.'))
        return redirect(url_for('auth.login'))

    return render_template(
        'auth/reset_password.html',
        form=form,
    )
