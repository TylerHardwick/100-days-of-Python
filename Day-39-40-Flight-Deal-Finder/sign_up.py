#Created and used separately on Replit

import requests

SHEETY_ENDPOINT = "Sheety_endpoint"
SHEETY_AUTH = {"Authorization": "Bearer auth_key"}

print("Bonjour, welcome to Tyler's flight club. \nWe find the best flight deals and email them to you ✈️")
forename = input("What is your first name?: ")
surname = input("What is your last name?: ")
email = input("What is your email address?: ").lower()
email2 = input("Please confirm your email address: ").lower()
if email == email2:
    print(f"Why hello {forename}, welcome to the club.")
    parameters = {
        "user": {
            "firstName": forename,
            "lastName": surname,
            "email": email
        }
    }
    sheety_post_reponse = requests.post(url=SHEETY_ENDPOINT, json=parameters, headers=SHEETY_AUTH)
