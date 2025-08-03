from flask import Flask, render_template, request, redirect, session, url_for
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'

users = {}
codes = ["21asa", "32hys"]

def get_current_code():
    now = datetime.utcnow()
    index = (now.minute // 20) % 2
    return codes[index]

@app.route('/')
def index():
    return redirect('/login')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users[username] = password
        return redirect('/login')
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users.get(username) == password:
            session['user'] = username
            return redirect('/code')
    return render_template('login.html')

@app.route('/code', methods=['GET', 'POST'])
def code_page():
    if 'user' not in session:
        return redirect('/login')

    if request.method == 'POST':
        entered_code = request.form['code']
        if entered_code == get_current_code():
            return redirect('/home')
    return render_template('code.html', current=get_current_code())

@app.route('/home', methods=['GET'])
def home():
    if 'user' not in session:
        return redirect('/login')
    return render_template('home.html')

@app.route('/predict')
def predict():
    x = round(random.uniform(1.0, 200.0), 2)
    return str(x)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
