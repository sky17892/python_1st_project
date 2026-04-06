from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class RegisterForm(FlaskForm):
    mem_name = StringField('이름', validators=[DataRequired()])
    mem_email = StringField('이메일', validators=[DataRequired(), Email()])
    mem_password = PasswordField('비밀번호', validators=[DataRequired()])
    mem_password2 = PasswordField('비밀번호 확인',
        validators=[DataRequired(), EqualTo('mem_password')])
    mem_phone = StringField('휴대폰')
    submit = SubmitField('회원가입')

class LoginForm(FlaskForm):
    mem_email = StringField('이메일', validators=[DataRequired(), Email()])
    mem_password = PasswordField('비밀번호', validators=[DataRequired()])
