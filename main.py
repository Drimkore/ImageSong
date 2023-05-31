from flask import Flask, render_template, request


app = Flask(__name__)
text = ''

@app.route("/")
def main_page():
    return render_template('index.html')

