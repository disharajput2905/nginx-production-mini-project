from flask import Flask
import socket
import sys

app = Flask(__name__)

@app.route("/")
def home():
    return f"Hello from {socket.gethostname()}"

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    app.run(host="0.0.0.0", port=port)
