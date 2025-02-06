from flask import Flask, render_template  # Import necessary modules from Flask
import os  # Import the os module to work with the operating system

app = Flask(__name__)  # Create an instance of the Flask class

@app.route("/")  # Define a route for the root URL "/"
def home():  # Define a function named home that returns "home.html" 
   #return render_template("home.html", content="Flask tutorial")  # Return the "home.html" template with the content "Flask tutorial"
   return render_template("home.html", content=["ML", "DL", "AI", "DS"]) # Return the "home.html" template with the content "Flask tutorial"
@app.route("/index")  # Define a route for the "/about" URL
def index():
    return render_template("index.html")

if __name__ == "__main__":  # Ensure the script runs only if executed directly
    app.run(debug=True)  # Start the Flask web server with debugging enabled
