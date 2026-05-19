from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return f"Backend 1 - port 5000\n"

if __name__ == "__main__":
    app.run(port=5000)
