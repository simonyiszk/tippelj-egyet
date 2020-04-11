#!/usr/bin/python3
from flask import Flask
from flask import render_template, escape, send_from_directory
import uuid

host='tippelj.sch.bme.hu'
wsuri='ws://' + host + '/ws' #Change to ws://localhost:8765 when using in test environment

app = Flask(__name__, static_url_path='', static_folder='assets/')

@app.route('/start_game/<token>')
def servegame(token):
    return render_template('game.html', session_id=escape(token), wsuri=wsuri)

@app.route('/new_game')
def newgame():
    return render_template('create_game.html', url='http://' + host + '/start_game/' + str(uuid.uuid1()))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
