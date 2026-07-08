# Example for a simple Flask app
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from EKS!"

if __name__ == "__main__":
    # Crucial: Bind to 0.0.0.0, not 127.0.0.1
    app.run(host='0.0.0.0', port=8080)