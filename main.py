from flask import Flask, render_template, request
from gradio_client import Client
import json, random, os


app = Flask(__name__)
app.debug = True


@app.route("/")
def main_page():
    print('Hi', flush=True)
    return render_template('index.html')


def get_song():
    r_id = random.randint(0, 10)
    song_data = json.load(open('song_list.json', 'rb'))
    song_title = song_data['songs'][r_id]['song_name']
    return song_title


def change_path(path):
    path_list = path.split('/', '\\')
    file_name = path_list[-1]
    if os.name == 'nt':  # for windows
        new_path = '/static/tmp/'+file_name
        os.system(f'copy {path} {new_path}')
    else:
        new_path = ''+file_name
        os.system(f'cp {path} {new_path}')
    return new_path

@app.route("/", methods=['POST'])
def get_image():
    client = Client("https://dukujames-text-image.hf.space/")
    result = client.predict(
        get_song(),	 # str  in 'Input' Textbox component
        api_name="/predict"
    )
    print('check')
    return json.dumps({'result':change_path(result)})
