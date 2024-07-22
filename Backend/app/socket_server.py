from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    print(f"Received message: {message}")
    emit('response', {'data': 'Message received'}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
