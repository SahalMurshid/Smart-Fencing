from twilio.rest import Client

account_sid = 'ACc4b1fc1af33d85a0b87d95d5fe7ee4a0'
auth_token = 'dd35b00d7280a26b1deace4bf006d4d2'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+15076836292',
  body='Hey nigga good to meet you there is a elephant near the fence dont go near it ',
  to='+918606496666'
)

print(message.sid)