import os
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Serve the HTML file

@app.route('/api/message', methods=['POST'])
def get_message():
    if request.is_json:  # Check if the incoming request is JSON
        data = request.get_json()
        print(f"Received data: {data}")
        message = data.get('message', '')
        response = {'response': f"You sent: {message}"}
        return jsonify(response)
    else:
        return jsonify({"error": "Unsupported Media Type, expected JSON"}), 415

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
