import random
import os
import logging

from flask import Flask, jsonify, redirect, send_file
from flask_socketio import SocketIO, send, emit

BASE = os.getenv('BASE', '') # app/site1

logging.getLogger('socketio').setLevel(logging.INFO)
logging.getLogger('engineio').setLevel(logging.INFO)


app = Flask(__name__, static_url_path='/{}/static'.format(BASE), static_folder='mystatic')

@app.route('/{}/'.format(BASE))
def index():
    return send_file('mystatic/html/index.html')


app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# Flask bluepoint
app.url_map.strict_slashes = False



# socketio
socketio = SocketIO(app, path='/{}/socket.io'.format(BASE), logger=True)

@app.route('/healthz', methods=['GET'])
def healthz():
    return jsonify({'message': 'OK'}), 200

@app.route('/{}/v1/color'.format(BASE), methods=['GET'])
def color():
    r = lambda: random.randint(0,255)
    return jsonify({'message': '#%02X%02X%02X' % (r(),r(),r())}), 200

@socketio.on('connect')
def connect():
    print('socketio connect')

@socketio.on('disconnect')
def socket_disconnect():
    print('socketio disconnect')

@socketio.on('event')
def handle_event(event):
    send({'message': 'hi, there'})

if __name__ == '__main__':
    FLASK_HOST = '0.0.0.0'
    FLASK_PORT = 5000
    socketio.run(app,
                 host=FLASK_HOST,
                 port=FLASK_PORT)
