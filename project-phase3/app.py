from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/health/live')
def liveness():
    return "I am alive", 200

@app.route('/health/ready')
def readiness():
    return "I am ready", 200

if __name__ == '__main__':
    if os.getenv('CI') == '1':
        print("Running in CI mode: not starting Flask server")
    else:
        app.run(host='0.0.0.0', port=5000, debug=True)

