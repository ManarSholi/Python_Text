from twilio.rest import Client

account_sid = "AC47dbca9c841b653f68f82b30e469e1e9"
auth_token = "c11842b5c1e2c9f262943ce7d22727c4"

client = Client(account_sid, auth_token)
call = client.messages.create(
    to="+97025632563",
    body="This is our first message",
    from="+13617923386",
)
