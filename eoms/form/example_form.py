from wtforms import Form, BooleanField, StringField, DateField, PasswordField, SelectField, validators, EmailField
from datetime import date, timedelta

class LoginForm(Form):
    username = StringField(
        'Username', 
        validators=[
            validators.DataRequired()
        ]
    )
    password = PasswordField(
        'Password', 
        validators=[
            validators.DataRequired()
        ]
    )

class RegistrationForm(Form):
    username = StringField(
        'Username', 
        validators=[
            validators.DataRequired(),
            validators.Length(min=4, max=25)
        ]
    )
    email = EmailField(
        'Email Address', 
        validators=[
            validators.DataRequired(),
            validators.Email()
        ]
    )
    password = PasswordField(
        'Password', 
        validators=[
            validators.DataRequired()
        ]
    )
    confirm = PasswordField(
        'Confirm Password',
        validators=[
            validators.DataRequired(),
            validators.EqualTo('password', message='Passwords must match')
        ]
    )
    title = SelectField(
        'Title', 
        validators=[
            validators.DataRequired()
        ],
        choices =[
            ('Mr', 'Mr'),
            ('Mrs', 'Mrs'),
            ('Ms', 'Ms'),
            ('Miss', 'Miss'),
            ('Dr', 'Dr')
        ]
    )
    first_name = StringField(
        'First name', 
        validators=[
            validators.DataRequired()
        ]
    )
    last_name = StringField(
        'Last name', 
        validators=[
            validators.DataRequired()
        ]
    )
    dob = DateField(
        'Date of birth', 
        validators=[
            validators.DataRequired()
        ]
    )
    accept_tos = BooleanField(
        'I accept the T&C', 
        validators=[
            validators.DataRequired()
        ]
    )

    def validate_dob(form, field):
        
        today = date.today()
        age = (today - field.data) // timedelta(days=365.2425)
        if age < 18:
            raise validators.ValidationError('You must be at least 18 years old to register.')