from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the Flask App!"


@app.route("/api/data")
def get_data():
    data = {"message": "Hello, World!", "status": "success"}
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
