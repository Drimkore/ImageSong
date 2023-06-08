from flask import Flask, render_template, request
from gradio_client import Client
import json, random


app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template('index.html')


def get_song():
    r_id = random.randint(0, 10)
    song_data = json.load(open('song_list.json', 'rb'))
    song_title = song_data['songs'][r_id]['song_name']
    return song_title


def get_image(input_text):
    client = Client("https://dukujames-text-image.hf.space/")
    result = client.predict(
				input_text,	# str  in 'Input' Textbox component
				api_name="/predict"
    )
    return result