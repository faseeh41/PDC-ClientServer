import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    # Get the port number from the environment variable
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if not set
    app.run(host='0.0.0.0', port=port)  # Listen on all interfaces
