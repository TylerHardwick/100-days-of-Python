import requests
from datetime import datetime
import smtplib
import time


MY_LNG = -0.759417
MY_LAT = 52.040623

EMAIL_USER = "myemail@email.com"
EMAIL_PASS = "mypassword"


def check_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    sun_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    sun_response.raise_for_status()
    sun_data = sun_response.json()
    sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

    current_hour = datetime.now().hour
    if current_hour < sunrise or current_hour > sunset:
        return True
    else:
        return False

def check_iss_overhead():
    iss_repsponse = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_repsponse.raise_for_status()
    data = iss_repsponse.json()

    latitude = float(iss_repsponse.json()["iss_position"]["latitude"])
    longitude = float(iss_repsponse.json()["iss_position"]["longitude"])
    print(latitude, longitude)

    if MY_LAT -5 <= latitude <=MY_LAT+5 and MY_LNG-5 <= longitude <= MY_LNG+5:
        return True

while True:
    time.sleep(60)
    if check_iss_overhead() and check_night():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=EMAIL_USER, password=EMAIL_PASS)
            connection.sendmail(from_addr=EMAIL_USER, to_addrs="testemail@email.com",
                                msg=f"Subject:International Space Station currently above you.\n\n "
                                    f"Look up! The ISS is currently above you!")
            print("Email sent")


# TODO 1. If the iss is close to my position, +5 -5 Lat and Lng
# and it is currently dark
# then send me an email to look up
#repeat this every 60 seconds