from flask import Flask, render_template, send_from_directory
import os
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("moorhouseassociates.com", 1883, 60)

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html", to="cygarxtin")

@app.route('/btn')
def btn():
	print("button clicked")
	client.publish("test/all", " Hey Gomah, watzup?")
	return ""

@app.route('/css/<path:path>')
def send_css(path):
	return send_from_directory('css', path)

@app.route('/img/<path:path>')
def send_img(path):
        return send_from_directory('img', path)

@app.route('/whereami')
def whereami():
	return "Kdua"

@app.route('/hello/<name>')
def foo(name):
        return render_template('index.html', to=path)

@app.route('/python')
def mypython():
	return render_template("webpage2.html")

@app.route('/linux')
def mylinux():
	return render_template("webpage3.html")

