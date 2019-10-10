from flask_wtf import FlaskForm, RecaptchaField
from wtforms import SubmitField, TextField
from wtforms.validators import InputRequired, Length
from wtforms_alchemy import model_form_factory


from app.models import Post


from app import db


BaseModelForm = model_form_factory(FlaskForm)


class ModelForm(BaseModelForm):
    @classmethod
    def get_session(cls):
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
    title = TextField("Title:")
    postname = TextField("Postname:")
    # content = TextAreaField("Content:")
    tags = TextField("Tags:")

    # {% for category in g.categories %}
    # {{ category.category_name }}<input type="radio" name="category" value="{{ category.id }}" />&nbsp;&nbsp;
    # {% endfor %}
    # recaptcha = RecaptchaField("Copy the words appearing below")
    submit = SubmitField("Submit")

    class Meta:
        model = Post
        exclude = ['views', 'comments_count', 'tags_name']


class EForm(FlaskForm):
    postnumber = TextField("Postnumber")
    submit = SubmitField("Submit")
