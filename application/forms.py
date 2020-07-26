from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError

#WTF validations
class ComposeEmailForm(FlaskForm):
    senderId  =  StringField("From:", validators=[DataRequired(),Length(min=5,max=20)])
    reciverId =  StringField("To:", validators=[DataRequired(),Length(min=5,max=20)])
    subject   =  StringField("Subject", validators=[DataRequired()])
    message   =  TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send")

    def validate_message(self, message):
        if len(message.data) > 50:
            raise ValidationError('Message must be less than 50 characters')

    def validate_subject(self, subject):
        if len(subject.data) > 20:
            raise ValidationError('Subject must be less than 20 characters')
