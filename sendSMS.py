import sys
try:
	from twilio.rest import TwilioRestClient
except ImportError:
	print "Unfortunately, twilio package was not installed. Please try to execute 'pip install twilio' for install required package"

account_sid = ""
auth_token = ""

try:
	file = open("credentials.txt","r")
	credentials = file.read()
	account_sid, auth_token = credentials.split(",")
except IOError:
	file = open("credentials.txt","w")
	account_sid = raw_input("Please insert your Sid: ")
	auth_token = raw_input("Please insert your Auth Token: ")
	file.write(account_sid + "," + auth_token)
file.close()

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello World, @metoinside" ,to="toPhoneNumber",from_="yourTwilioPhoneNumber")
print message.sid
