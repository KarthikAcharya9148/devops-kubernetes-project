from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Hello from DevOps project!",
        "version": os.getenv("APP_VERSION", "1.0.0")
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/api/hello")
def hello():
    return jsonify({
        "message": "Hello Kubernetes!"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
