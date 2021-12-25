from flask import Flask, url_for, request, render_template

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        print(user, password)
    return render_template("userNotLoggedIn.html")