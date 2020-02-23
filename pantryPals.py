from flask import Flask, request
from flask import render_template
from markupsafe import escape
import requests 
import textAlerts

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('trial.html')



#background process happening without any refreshing
@app.route('/sendTexts')
def sendTexts():
    textAlerts.sendText(textAlerts.fromNumber, textAlerts.shreyaNumber, textAlerts.message)
    return("nothing")



