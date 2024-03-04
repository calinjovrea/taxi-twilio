from flask import Flask, request
from twilio.twiml.voice_response import Gather, VoiceResponse

app = Flask(__name__)

@app.route('/voice', methods=['POST'])
def voice():
    response = VoiceResponse()
    gather = Gather(num_digits=1, action='/menu', method='POST')
    gather.say("Welcome to the Robot Menu. Press 1 to activate, 2 to deactivate, 3 to move forward, 4 to move backward, 5 to turn left, 6 to turn right.", voice='alice', language='en-GB')
    response.append(gather)
    return str(response)

@app.route('/menu', methods=['POST'])
def menu():
    selected_option = request.form['Digits']
    response = VoiceResponse()

    if selected_option == '1':
        response.say("Robot activated.")
    elif selected_option == '2':
        response.say("Robot deactivated.")
    elif selected_option == '3':
        response.say("Robot moving forward.")
    elif selected_option == '4':
        response.say("Robot moving backward.")
    elif selected_option == '5':
        response.say("Robot turning left.")
    elif selected_option == '6':
        response.say("Robot turning right.")
    else:
        response.say("Invalid selection. Please try again.")

    response.redirect('/voice')
    return str(response)

if __name__ == '__main__':
    app.run(debug=True)
