import os
from flask import Flask, request, jsonify, render_template
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Serve the HTML file

@app.route('/api/message', methods=['POST'])
def get_message():
    if request.is_json:  # Check if the incoming request is JSON
        data = request.get_json()
        message = data.get('message', '')

        # Get the user agent from the request headers
        user_agent = request.headers.get('User-Agent', 'Unknown Device')

        # Log the message in hacker style with a timestamp and device info
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [HACKER LOG] Received message: \"{message}\" from {user_agent}")

        # Generate a shocking response
        shocking_responses = [
            f"HACKER RESPONSE: Your message \"{message}\" was received and logged. \n"
            f"🔍 HACKER ALERT: I see you're using {user_agent}! That's a nice device. \n"
            "But remember, every keystroke is being monitored! 👀💻",

            f"HACKER RESPONSE: Whoa! You just sent \"{message}\" from {user_agent}. \n"
            "I hope you know what you're getting into... \n"
            "The digital shadows are always watching! 🕵️‍♂️",

            f"HACKER RESPONSE: Your message \"{message}\" has been logged. \n"
            f"📱 Device Detected: {user_agent}. \n"
            "Consider this a friendly warning: nothing on the internet is truly private! 🔒",
            
            f"HACKER RESPONSE: Message \"{message}\" received. \n"
            f"🛡️ Your device: {user_agent}. Hope you're ready for the consequences! \n"
            "Don't forget: hackers have all the time in the world...⌛",
        ]

        # Randomly select a response to keep it dynamic
        response_message = random.choice(shocking_responses)

        response = {
            'response': response_message
        }
        return jsonify(response)
    else:
        return jsonify({"error": "Unsupported Media Type, expected JSON"}), 415

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
