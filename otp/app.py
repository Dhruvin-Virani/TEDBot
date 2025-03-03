from flask import Flask, render_template, request, jsonify
from twilio.rest import Client
import os

app = Flask(__name__)

# Your Twilio Account SID and Auth Token
account_sid = 'AC9864f080d07646638148bcdd288d9e3d'
auth_token = 'af95e62e642ef879b00ba5ced1fd58e2'
client = Client(account_sid, auth_token)

# Your Twilio phone number
from_number = '+17406192673'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_otp', methods=['POST'])
def send_otp():
    phone_number = request.json.get('phone_number')
    otp = '123456'  # Replace with generated OTP
    try:
        message = client.messages.create(
            body=f'Your OTP is: {otp}',
            from_=from_number,
            to=phone_number
        )
        return jsonify(message="OTP sent")
    except Exception as e:
        return jsonify(message=f"Failed to send OTP: {str(e)}")

@app.route('/verify_otp', methods=['POST'])
def verify_otp():
    entered_otp = request.json.get('otp')
    # Here, you can compare the entered OTP with the expected OTP
    if entered_otp == '123456':  # Replace '123456' with the expected OTP
        return jsonify(message="OTP verified")
    else:
        return jsonify(message="Invalid OTP")

if __name__ == '__main__':
    app.run(debug=True)
