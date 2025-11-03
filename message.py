from twilio.rest import Client

account_sid = '******************************'
auth_token = '********************************'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+15076836292',
  body='Hey nigga good to meet you there is a elephant near the fence dont go near it ',
  to='+1***********'
)

print(message.sid)
