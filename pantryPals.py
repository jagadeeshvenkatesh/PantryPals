from flask import Flask
from flask import render_template
from markupsafe import escape
app = Flask(__name__)

url_for('static', filename='/static/css/main.css')

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/home')
def home():
	return render_template('index.html')

#def hello(name=None):
#    return render_template('index.html', name=name)