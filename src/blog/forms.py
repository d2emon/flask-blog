from flask_wtf import FlaskForm, RecaptchaField
from wtforms import SubmitField, TextField, TextAreaField
from wtforms.validators import InputRequired, Length
from wtforms_alchemy import model_form_factory


from .models import Post


from app import db


BaseModelForm = model_form_factory(FlaskForm)


class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session


class LoginForm(FlaskForm):
    username = TextField(
        "Username",
        validators=[
            InputRequired(message="Need an name"),
            Length(max=50)
        ]
    )
    password = TextField(
        "Password",
        validators=[
            InputRequired(message="Need a password"),
            Length(max=50)
        ]
    )
    recaptcha = RecaptchaField("Copy the words appearing below")
    submit = SubmitField("Login")


class PostForm(ModelForm):
    title = TextField("Title")
    postname = TextField("Postname")
    content = TextAreaField("Postname")
    tags = TextField("Tags")
    # {% for category in g.categories %}
    # {{ category.category_name }}<input type="radio" name="category" value="{{ category.id }}" />&nbsp;&nbsp;
    # {% endfor %}
    recaptcha = RecaptchaField("Copy the words appearing below")
    submit = SubmitField("Submit")

    class Meta:
        model = Post


class EForm(FlaskForm):
    postnumber = TextField("Postnumber")
    submit = SubmitField("Submit")
