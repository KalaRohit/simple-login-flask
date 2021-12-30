from flask import Flask, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

    

@app.route("/", methods=['GET', 'POST'])
def no_user_page():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        print(user, password)
    return render_template("userNotLoggedIn.html")

@app.route("/signUp", methods=['GET', 'POST'])
def sign_up_page():
    if request.method == 'POST':
        pass
    return render_template("signUp.html")

@app.route("/user/<username>")
def user_logged_in():
    return "HelloWorld"

if __name__ == "__main__":
    app.run(debug=True)