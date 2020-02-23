from flask import Flask
from flask import render_template
from markupsafe import escape

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/home')
def home():
	return render_template('index.html')

#def hello(name=None):
#    return render_template('index.html', name=name)