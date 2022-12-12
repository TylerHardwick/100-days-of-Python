import requests

SHEETY_ENDPOINT = "sheet_endpoint"
SHEETY_HEADER = {"Authorization": "bearer KEY"}

class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_sheety_data(self):
        sheety_response = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADER)
        sheety_data = sheety_response.json()
        self.destination_data = sheety_data["prices"]
        return self.destination_data

    def update_iata(self, row_id, iata):
        parameters = {
            "price": {
                "iataCode": iata
            }
        }
        sheety_update_endpoint = f"{SHEETY_ENDPOINT}/{row_id}"
        sheety_update = requests.put(url=sheety_update_endpoint, json=parameters, headers=SHEETY_HEADER)

    def get_user_email(self):
        user_endpoint = "sheety_endpoint"
        user_response = requests.get(url=user_endpoint, headers=SHEETY_HEADER)
        user_list = user_response.json()["users"]
        email_list = [user_list[num]["email"] for num in range(len(user_list))]
        return email_list




