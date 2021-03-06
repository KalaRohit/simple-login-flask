from flask import Flask, url_for, request, render_template, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect
from sqlalchemy.exc import SQLAlchemyError
from functools import wraps
from passlib.hash import bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
app.secret_key = "test"

#User object that is pushed into database
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    pword = db.Column(db.String(100), nullable=False) #Stores a hashed password, thus it is 100 characters.
    def __init__(self, username, email, pword):
        self.username = username
        self.email = email
        self.pword = pword

#a decorator function that verifies that a user is logged in
def login_required(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if "user" not in session:
            return redirect(url_for('no_user_page'))
        return f(*args, **kwargs)
    return wrap

#guest page
@app.route("/", methods=['GET', 'POST'])
def no_user_page():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        userObject = Users.query.filter_by(username=user).first()
        if bcrypt.verify(password, userObject.pword):
            session['user'] = user
            return redirect(url_for('user_logged_in'))
    return render_template("userNotLoggedIn.html")

#signuppage
@app.route("/signUp", methods=['GET', 'POST'])
def sign_up_page():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['pword1']
        hashedPword = bcrypt.hash(password)
        email = request.form['email']
        new_user = Users(username=username, email=email,pword=hashedPword)
        try:
            db.session.add(new_user)
            db.session.commit()
            session["user"] = username
            return redirect(url_for('user_logged_in'))
        #CHANGE!
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            return error
    return render_template("signUp.html")

#After the user has logged in page
@app.route("/user", methods=['GET', 'POST'])
@login_required
def user_logged_in():
    if request.method == 'POST': #signout prompt
        session.clear()
        return redirect(url_for('no_user_page'))
    return render_template('userLoggedIn.html', user = session['user'])

if __name__ == "__main__":
    app.run(debug=True)
