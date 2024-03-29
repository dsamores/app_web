"""Modulo de rutas de la app web."""
from flask import Flask, render_template, request

from process import text_analysis  # pylint: disable=import-error

app = Flask(__name__)


@app.route('/')
def hello():
    """Ruta de pagina de inicio."""
    return render_template("index.html")


@app.route('/analizar', methods=['GET', 'POST'])
def analizar():
    """Ruta para analizar texto."""
    text = request.form.get('text')
    results = text_analysis(text)
    return render_template("index.html", results=results)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
