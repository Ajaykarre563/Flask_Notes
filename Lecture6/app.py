from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta, datetime, timezone

app = Flask(__name__)

# Secret key for session security (change this in production)
app.secret_key = "your_secure_random_key"

# Session timeout set to 60 seconds
app.permanent_session_lifetime = timedelta(seconds=60)

@app.route('/')
def home():
    """Render the home page"""
    return render_template('home.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    """Handle user login"""
    if "user" in session:
        flash(f'You are already logged in as {session["user"]}!', 'info')
        return redirect(url_for('user'))  # Redirect if already logged in

    if request.method == 'POST':
        session.permanent = True  # Extend session lifespan on login
        session['login_time'] = datetime.now(timezone.utc).isoformat()  # Store login time
        user = request.form.get('username', '').strip()

        if user:
            session['user'] = user  # Store user in session
            flash('You have successfully logged in!', 'success')  # Login success message
            return redirect(url_for('user'))

        flash('Error: Please enter a valid username!', 'danger')  # Empty username error
    
    return render_template('login.html')

@app.route('/user')
def user():
    """Display the user profile if logged in"""
    user = session.get('user')
    login_time = session.get('login_time')
    
    if user and login_time:
        login_time = datetime.fromisoformat(login_time)  # Convert string to datetime
        if (datetime.now(timezone.utc) - login_time).total_seconds() > 60:
            session.pop("user", None)  # Remove user only
            session.pop("login_time", None)  # Remove login time
            flash('Your session has expired. Please log in again.', 'warning')
            return redirect(url_for('login'))
        return render_template('user.html', username=user)
    
    flash('Your session has expired. Please log in again.', 'warning')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    """Log the user out and display a flash message"""
    if "user" in session:
        flash('You have successfully logged out!', 'success')  # Logout success message
        session.pop("user", None)  # Remove only the user from session
        session.pop("login_time", None)  # Remove login time
    else:
        flash('You are not logged in.', 'warning')  # If no session exists
    
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
