from slackclient import SlackClient

slack_token = "xoxb-120639107217-U6ALke1l0dy0r9n1i4RZiPbM"
slack_client = SlackClient(slack_token)
api_call = slack_client.api_call("channels.list")

if slack_client.rtm_connect():	
	print "Successfully connected"
	for channel in api_call.get("channels"):
		print "channel yeah"
		if channel.get("name") == "slackbot_test":	
			print "user is right"
			response = "NOW it's time for STANDUP MEETING. YEAH"
			slack_client.api_call("chat.postMessage", channel="slackbot_test", text=response, as_user=True)
else:
	print "Connection failed"
