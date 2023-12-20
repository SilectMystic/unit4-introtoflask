from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user_name = 'Mystic'
    return render_template('home.html.jinja', user_name=user_name)

@app.route('/ping')
def ping():
    return '<h1>pong<h1>'

@app.route('/hello/<name>')
def hello(name):
    return f'<h1>Hello {name}!<h1>'