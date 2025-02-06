from flask import Flask,redirect,url_for  # Importing the Flask class from the flask module

app = Flask(__name__)  # Creating an instance of the Flask class

@app.route("/")  # Defining a route for the root URL "/"
def home():  
    return "Hello, World!"  # Function returns "Hello, World!" when accessed

@app.route("/about")  # Defining a route for the "/about" URL
def about():
    return "I am a software engineer"  # Function returns "I am a software engineer" when accessed

@app.route("/<name>")  # Defining a dynamic route for the "/name" URL means you can pass any name in the URL b/w '<name>'.
def name(name):
    return f"Hi this is {name}!"  # Function returns My name

@app.route("/admin")  # Defining a route for the "/admin" URL
#def admin():
#   return redirect(url_for("home"))  # Redirecting to the root URL ("/")

def admin():
    return redirect("/")

if __name__ == "__main__":  # Ensures the script runs only if executed directly
    app.run(debug=True)  # Starts the Flask web server with debugging enabled mean it will reload the server when you make changes to the code.
