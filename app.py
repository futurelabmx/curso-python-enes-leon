from flask import Flask
from flask import render_template


app = Flask(__name__)

eventos = [
	{
		"title": "Evento random #1",
		"desc": "Descripción random sobre mi evento favorito #1."
	},
	{
		"title": "Evento random #2",
		"desc": "Descripción random sobre mi evento favorito #2."
	},
	{
		"title": "Evento random #3",
		"desc": "Descripción random sobre mi evento favorito #3."
	}
]


@app.route('/')
def index():
	return render_template('index.html', e=eventos)


@app.route('/acerca-de')
def about():
	return render_template('about.html')


if __name__ == "__main__":
	app.run(debug=True, port=5000)