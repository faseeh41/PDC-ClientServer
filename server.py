import os
from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Serve the HTML file

@app.route('/api/message', methods=['POST'])
def get_message():
    if request.is_json:  # Check if the incoming request is JSON
        data = request.get_json()
        message = data.get('message', '')

        # Log the message in hacker style with a timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [HACKER LOG] Received message: {message}")

        # Craft a humorous and hacker-style response
        response = {
            'response': (
                f"HACKER RESPONSE: Your message \"{message}\" was received and logged. \n"
                "⚠️ Caution: Just between us, don’t go spilling the beans to anyone, \n"
                "or I might have to unleash the digital ninjas! 🥷💻\n\n"
                "P.S. Remember, in the world of hacking, the only thing more secure than a vault is a secret between friends! \n"
                "Keep it encrypted! 🔒"
            )
        }
        return jsonify(response)
    else:
        return jsonify({"error": "Unsupported Media Type, expected JSON"}), 415

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
