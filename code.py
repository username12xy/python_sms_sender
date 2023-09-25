from twilio.rest import Client

# Your Twilio Account SID and Auth Token
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Get user input for the SMS message and recipient's phone number
sms_message = input("Enter the SMS message: ")
recipient_number = input("Enter the recipient's phone number (in the format +1234567890): ")

try:
    # Send the SMS
    message = client.messages.create(
        body=sms_message,
        from_='your_twilio_phone_number',  # Your Twilio phone number
        to=recipient_number
    )
    print(f"SMS sent successfully with SID: {message.sid}")
except Exception as e:
    print(f"An error occurred: {str(e)}")

#Sign up for a Twilio account at https://www.twilio.com/ if you haven't already.
#After signing up, you'll get yourn Twilio Phone Number, Twilio Account SID and Auth Token from the Twilio dashboard.
#Install the Twilio Python library if you haven't already: pip install twilio
