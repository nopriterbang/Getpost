from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "admin" and password == "password":
            return redirect(url_for('welcome', username=username))
        else:
            return "Login Failed. Please try again."
    return render_template('login.html')

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return f"<h1>Welcome, {username}!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
