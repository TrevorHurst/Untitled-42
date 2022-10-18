import os
from flask import Flask, send_from_directory
from flask import request
from flask import redirect
from flask import render_template
from flask_socketio import SocketIO, send

messages = []

app = Flask(__name__)
app.config['SECRET'] = "Secret123"
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/troll.ico')
def icon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'troll.ico', mimetype='image/vnd.microsoft.ico')

@app.route('/css/styles.css')
def styles():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'css/styles.css')

@app.route('/js/app.js')
def js():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'js/app.js')

@socketio.on('message')
def handle_message(message):
    print(f"Recieved: {message}")
    send(message, broadcast=True)

@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    socketio.run(app, host='localhost')
