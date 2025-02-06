from flask import Flask, render_template
from flask_wtf import FlaskForm  # Correct import
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Ak'  # Secret key for WTForms

# Define Form Class
class NameForm(FlaskForm):  # Use FlaskForm instead of Form
    name = StringField('What is your name?')
    submit = SubmitField('Submit')

# Define Route
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()  # Create an instance of the form
    name = None  # Initialize name variable

    if form.validate_on_submit():  # Check if form is submitted
        name = form.name.data  # Get name input
        form.name.data = ''  # Clear the form field

    return render_template('index.html', name=name, form=form)

# Run the Flask App
if __name__ == '__main__':
    app.run(debug=True)
