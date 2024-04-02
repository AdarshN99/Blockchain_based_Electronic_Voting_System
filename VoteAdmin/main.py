from flask import Flask, jsonify, request, render_template, redirect, url_for, session
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__)

app.secret_key = 'your_secret_key'

app.config["MONGO_DBNAME"] = "voting_system"
app.config["MONGO_URI"] = "mongodb://localhost:27017/voting_system"

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register_user', methods=['POST'])
def register_user():
    users = mongo.db.users
    # Assuming you are sending data as JSON
    name = request.json['name']
    address = request.json['address']
    password = request.json['password']
    existing_user = users.find_one({'name': name})

    if existing_user is None:
        hashpass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        users.insert_one({'name': name, 'address': address, 'password': hashpass})
        return jsonify({"message": "User registered successfully"}), 200

    return jsonify({"message": "That username already exists!"}), 409

@app.route('/register_admin', methods=['POST'])
def register_admin():
    admins = mongo.db.admins
    name = request.json['name']
    address = request.json['address']
    password = request.json['password']
    existing_admin = admins.find_one({'name': name})

    if existing_admin is None:
        hashpass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        admins.insert_one({'name': name, 'address': address, 'password': hashpass, 'is_admin': True})
        return jsonify({"message": "Admin registered successfully"}), 200

    return jsonify({"message": "That admin username already exists!"}), 409

"""@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login_page():
    if request.method == 'POST':
        admins = mongo.db.admins
        admin_user = admins.find_one({'name': request.form['username']})

        if admin_user and bcrypt.checkpw(request.form['pass'].encode('utf-8'), admin_user['password']):
            session['username'] = request.form['username']
            # Redirect to an admin dashboard page if exists
            return redirect(url_for('admin_dashboard'))

        return 'Invalid username/password combination'
    
    return render_template('adminlog.html')  # Renamed to match your HTML file
"""
@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login_page():
    if request.method == 'POST':
        admins = mongo.db.admins
        admin_user = admins.find_one({'name': request.form['adminUsername']})

        if admin_user and bcrypt.checkpw(request.form['adminPassword'].encode('utf-8'), admin_user['password']):
            session['username'] = request.form['adminUsername']
            return redirect(url_for('admin_dashboard'))

        return 'Invalid username/password combination'
    
    return render_template('adminlog.html')

"""@app.route('/user_login', methods=['GET', 'POST'])
def user_login_page():
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'name': request.form['username']})

        if login_user and bcrypt.checkpw(request.form['pass'].encode('utf-8'), login_user['password']):
            session['username'] = request.form['username']
            # Redirect to a user dashboard page if exists
            return redirect(url_for('user_dashboard'))

        return 'Invalid username/password combination'
    
    return render_template('userlog.html')  # Assuming you have this HTML file"""

@app.route('/user_login', methods=['GET', 'POST'])
def user_login_page():
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'name': request.form['username']})

        if login_user and bcrypt.checkpw(request.form['userPassword'].encode('utf-8'), login_user['password']):
            session['username'] = request.form['username']
            return redirect(url_for('user_dashboard'))

        return 'Invalid username/password combination'
    
    return render_template('userlog.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    # Check to see if an admin is logged in
    if 'username' not in session:
        # Not logged in, redirect to login page
        return redirect(url_for('admin_login_page'))

    # Proceed if admin is logged in
    return render_template('admin.html')  # Assuming you have this HTML file

@app.route('/user_dashboard')
def user_dashboard():
    # Check to see if a user is logged in
    if 'username' not in session:
        # Not logged in, redirect to login page
        return redirect(url_for('user_login_page'))

    # Proceed if user is logged in
    return render_template('user.html')  # Assuming you have this HTML file

if __name__ == '__main__':
    app.run(debug=True)