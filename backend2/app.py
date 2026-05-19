from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return f"backend 2 - port5001\n"

if __name__ == "__main__":
    app.run(port=5001)
