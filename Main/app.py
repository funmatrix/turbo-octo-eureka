from flask import Flask, render_template, jsonify
from jinja2 import TemplateNotFound

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("home.html")


@app.route('/<string:filename>')
def getUser(filename):
    return render_template("aboutus.html")


@app.route('/number/<string:id>')
def praseNumber(page):
    try:
        return render_template(page)
    except TemplateNotFound:
        return render_template("404.html")


if __name__ == "__main__":
    app.run()
