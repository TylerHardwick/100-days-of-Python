from twilio.rest import Client
import smtplib

class NotificationManager:

    def flight_found_sms(self, message):
        account_sid = "twilio_sid"
        auth_token = "twilio_auth"
        message_body = message

        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body = message_body,
            from_ = "+13854752557",
            to = "+447588253281"
        )
        print(message.status)

    def send_emails(self, email, message):
        my_email = "my_email"
        my_password = "my_password"

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=email, msg=message)

            print("Msg sent")
