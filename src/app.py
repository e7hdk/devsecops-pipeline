"""Flask app for DevSecOps demo."""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    """Return a greeting."""
    return "Hello from DevSecOps!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    