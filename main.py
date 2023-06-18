import json
import os
import random
from flask import Flask, render_template, request
from gradio_client import Client

app = Flask(__name__)
app.debug = True

lives = 3
score = 0


@app.route("/")
def main_page():
    print('Hi', flush=True)
    return render_template('index.html', variable=correct_answer)


def change_path(path):
    if os.name == 'nt':  # for windows
        path_list = path.split('\\')
        file_name = path_list[-1]
        new_path = 'static\\tmp\\'+file_name  # по аналогии
        os.system(f'copy {path} {new_path}')
    else:  # for unix
        path_list = path.split('/')
        file_name = path_list[-1]
        new_path = 'static/tmp/'+file_name
        os.system(f'cp {path} {new_path}')
    return new_path


def get_song():
    r_id = random.randint(0, 10)
    song_data = json.load(open('song_list.json', 'rb'))
    song_title = song_data['songs'][r_id]['song_name']
    global help_list
    help_list = song_data['songs'][r_id]
    return song_title


correct_answer = ""
help_list = {}
count_help = 0


@app.route("/generate", methods=['GET'])
def get_image():
    global correct_answer
    correct_answer = get_song()
    client = Client("https://dukujames-text-image.hf.space/")
    result = client.predict(
        correct_answer,	 # str  in 'Input' Textbox component
        api_name="/predict"
    )
    return json.dumps({'result': change_path(result)})


@app.route("/answer", methods=['POST'])
def check_result():
    global lives
    global score
    res = False
    text = request.form['input_field']
    if text == correct_answer:
        res = True
        score += 10
    else:
        lives -= 1
    return json.dumps({'lives': lives, 'result': res, 'score': score})


@app.route("/help", methods=['GET'])
def get_help():
    global count_help
    count_help += 1
    if count_help == 1:
        return str(help_list['year'])
    elif count_help == 2:
        return help_list['genre']
    else:
        return help_list['artist']
