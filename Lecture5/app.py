from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta, datetime, timezone

app = Flask(__name__)
app.secret_key = "your_secure_random_key_here"  # Use a secure key in production
app.permanent_session_lifetime = timedelta(seconds=60)  # Session expires after 60 seconds

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if "user" in session:
        flash(f'You are already logged in as {session["user"]}!', 'info')
        return redirect(url_for('user'))
    
    if request.method == 'POST':
        session.permanent = True  # Extend session lifespan on login
        session['login_time'] = datetime.now(timezone.utc).isoformat()  # Store login time as a string
        user = request.form.get('username', '').strip()
        
        if user:
            session['user'] = user
            session.modified = True  # Ensure session updates
            flash(f'Login successful! Welcome, {user}.', 'success')
            return redirect(url_for('user'))
        
        flash('Error: Please enter a valid username!', 'danger')
    return render_template('login.html')

@app.route('/user')
def user():
    user = session.get('user')
    login_time = session.get('login_time')
    
    if user and login_time:
        # Convert stored login_time back to a datetime object
        login_time = datetime.fromisoformat(login_time).replace(tzinfo=None)  
        
        if (datetime.utcnow() - login_time).total_seconds() > 60:
            session.pop('user', None)
            session.pop('login_time', None)
            flash('Your session has expired. Please log in again.', 'warning')
            return redirect(url_for('login'))
        return render_template('user.html', username=user)
    
    flash('Your session has expired. Please log in again.', 'warning')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('login_time', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
