from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello"
#route for web server
@app.route('/whereami')
def whereami():
	return "Kdua"

if __name__== '__main__':
	app.run(host="0.0.0.0")

