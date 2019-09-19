from flask_babel import lazy_gettext as _l
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    post = TextAreaField(_l('Say something'), validators=[
        DataRequired(),
        Length(min=1, max=140),
    ])
    submit = SubmitField(_l('Submit'))
