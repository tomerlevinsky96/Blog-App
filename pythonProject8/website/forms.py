from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,DateField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):

    email = StringField('email',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class SignUpForm(FlaskForm):

    email = StringField('email',validators=[DataRequired()])
    FirstName=StringField('FirstName', validators=[DataRequired()])
    LastName = StringField('LastName', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    Birthday = DateField('Birthday', validators=[DataRequired()])

class PostForm(FlaskForm):
    category = StringField('category', validators=[DataRequired()])
    topic=StringField('topic',validators=[DataRequired()])
    text=StringField('text',validators=[DataRequired()])

class commentForm(FlaskForm):
    text=StringField('text',validators=[DataRequired()])
