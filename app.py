from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
SocketIO = SocketIO(app)
@app.route("/")
def index():
    return render_template("index.html")

@SocketIO.on('Mensaje')
def handle_mensaje(msg):
    print(msg)
    SocketIO.emit('Mensaje', msg)

if __name__ == "__main__":
    SocketIO.run(app, debug=True)