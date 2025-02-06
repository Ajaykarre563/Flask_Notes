# Import necessary Flask-WTF and WTForms components
from flask_wtf import FlaskForm  # FlaskForm for handling forms
from wtforms import TextAreaField, IntegerField, SubmitField, RadioField, SelectField  # Input fields
from wtforms import validators, ValidationError  # Validators for input validation

#  Define ContactForm class
class ContactForm(FlaskForm):
    #  Name field (required)
    name = TextAreaField("Name Of Student", [validators.DataRequired("Please enter your name.")])

    # Gender selection (Radio buttons for Male/Female)
    Gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])

    #  Address field (optional)
    Address = TextAreaField("Address")

    #  Email field (required & must be valid email)
    email = TextAreaField("Email", [
        validators.DataRequired("Please enter your email address."),
        validators.Email("Please enter a valid email address.")
    ])

    #  Age field (integer input)
    Age = IntegerField("Age")

    #  Programming language selection (Dropdown menu)
    language = SelectField('Languages', choices=[('cpp', 'C++'), ('py', 'Python')])

    #  Submit button
    submit = SubmitField("Send")
