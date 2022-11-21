import requests

SHEETY_ENDPOINT = "https://api.sheety.co/USER_HERE/flightDeals/prices"
SHEETY_HEADER = {"AUTHORISATION HERE"}

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



