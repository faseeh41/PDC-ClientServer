import os
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Serve the HTML file

# New route to handle POST requests
@app.route('/api/message', methods=['POST'])
def get_message():
    data = request.get_json()  # Get JSON data from the request
    message = data.get('message', '')  # Extract 'message' from the data
    response = {'response': f"You sent: {message}"}  # Create a response
    return jsonify(response)  # Return response as JSON

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Get the port
    app.run(host='0.0.0.0', port=port)  # Run the app
