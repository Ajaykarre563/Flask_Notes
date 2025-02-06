from flask import Flask, render_template
# Importing Flask and the render_template function to handle HTML templates

app = Flask(__name__)
# Creating a Flask application instance

@app.route('/')
# Defining the route for the home page

@app.route('/')
def home():
    return render_template('home.html')
    # Renders and returns the 'home.html' template when the home route is accessed
@app.route('/index')
def index():
    return render_template('index.html')
    # Renders and returns the 'index.html' template when the index route is accessed

if __name__ == '__main__':
    app.run(debug=True)
    # Runs the Flask app in debug mode, allowing automatic reloading on changes
