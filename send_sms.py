from twilio.rest import TwilioRestClient

account_sid = "AC2358390dedfd541fd727c893703eccfc" # Your Account SID from www.twilio.com/console
auth_token  = "fab9c2b6bb5b19930d1cac25ebfb6c9f"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
body="Hello from the othersideeee",
to="+66909747123",    # Replace with your phone number
from_="+1201-591-4204 ") # Replace with your Twilio number

print(message.sid)
