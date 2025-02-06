# Importing necessary modules from the Flask framework
from flask import Flask, render_template, request, redirect, url_for  

# Creating an instance of the Flask application
app = Flask(__name__)

# Defining the route for the home page ('/')
@app.route('/')
def home():
    return render_template('home.html')

# Defining the route for the login page with allowed methods (POST and GET)
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # Safely getting the 'username' from the form data
        user = request.form.get('username')  # Using .get() prevents KeyError

        if user:  # Check if username exists
            return redirect(url_for('user', usr=user))  
        else:
            return "Error: Please enter a username!"  # Handle empty input case

    return render_template('login.html')  # Render login page for GET request

# Defining a dynamic route for user greeting
@app.route('/user/<usr>')  
def user(usr):
    return f"Hello, {usr}!"  # Returning a greeting message with the username

# Running the Flask application
if __name__ == '__main__':
    app.run(debug=True)
