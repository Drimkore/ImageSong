from flask import Flask, render_template, request
from gradio_client import Client


app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template('index.html')


def get_image(input_text):
    client = Client("https://dukujames-text-image.hf.space/")
    result = client.predict(
				input_text,	# str  in 'Input' Textbox component
				api_name="/predict"
    )
    return result