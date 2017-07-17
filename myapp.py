from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html", to="cygarxtin")

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

