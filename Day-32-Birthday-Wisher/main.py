import smtplib
import datetime as dt
import random
import pandas

MY_EMAIL = "email@email.com"
MY_PASSWORD = "password"

now = dt.datetime.now()
month = now.month
day = now.day

birthday_df = pandas.read_csv("birthdays.csv")
birthday_dict = birthday_df.to_dict(orient="records")

for item in birthday_dict:
    if month == item["month"] and day == item["day"]:
        birthday_person = item["name"]
        birthday_email = item["email"]

        with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as letter:
            letter_contents = letter.read()
            new_letter = letter_contents.replace("[NAME]", birthday_person)

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_email,
                                msg=f"Subject:Happy Birthday {birthday_person}!\n\n {new_letter}")

        print("Msg sent")




