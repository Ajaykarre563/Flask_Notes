#  Import necessary libraries
from flask import Flask, render_template, request, flash  # Importing core Flask functions
from form import ContactForm  # Importing the ContactForm class from wtforms (you should have defined this class)

#  Initialize the Flask app
app = Flask(__name__)  # Initialize a new Flask application

# Set the secret key for sessions and form security (use a strong key in production)
app.config['SECRET_KEY'] = 'AK'  # This key is used for CSRF protection and sessions

#  Define the home route ("/") of the web app
@app.route('/')
def home():
    return "welcome to my life"  # Basic route that returns a welcome message

#  Define the contact route ("/contact") with GET and POST methods
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()  # Create an instance of the ContactForm

    #  Check if the request method is POST (form submission)
    if request.method == 'POST':
        #  Validate the form fields to ensure they are filled out correctly
        if form.validate() == False:
            flash('All fields are required.')  # If validation fails, flash an error message
            return render_template('contact.html', form=form)  # Re-render the form with the error message
        else:
            return 'Form posted successfully.'  # If validation is successful, return success message

    # If the request method is GET (initial form load), render the form
    elif request.method == 'GET':
        return render_template('contact.html', form=form)  # Render the contact form

#  Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode for development (auto reloads and detailed errors)
