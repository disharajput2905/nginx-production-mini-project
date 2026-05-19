from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return f"Hello from Backend 2 | host:{socket.gethostname()}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
