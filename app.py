from flask import Flask
from flask import render_template


app = Flask(__name__)

eventos = [
	{
		"title": "Evento random #1"
	},
	{
		"title": "Evento random #2"
	}
]


@app.route('/')
def index():
	return render_template('index.html', e=eventos)


if __name__ == "__main__":
	app.run(debug=True, port=5000)