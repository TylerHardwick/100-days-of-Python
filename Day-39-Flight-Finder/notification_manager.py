from twilio.rest import Client

class NotificationManager:

    def flight_found_sms(self, message):
        account_sid = "accound SID here"
        auth_token = "auth token here"
        message_body = message

        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body = message_body,
            from_ = "send-num",
            to = "receive num"
        )
        print(message.status)
