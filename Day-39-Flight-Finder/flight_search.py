import requests
import datetime as dt
from flight_data import FlightData

FLIGHT_ENDPOINT = "https://api.tequila.kiwi.com"
FLIGHT_API = "FLIGHT_API"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.current_date = dt.datetime.now()
        self.six_month_date = self.current_date + dt.timedelta(days=6 * 30)


    def get_iata(self, city):
        locations_endpoint = f"{FLIGHT_ENDPOINT}/locations/query"
        headers = {
            "apikey": FLIGHT_API,
            "accept": "application/json"
        }
        parameters = {
            "term": city,
            "locale": "en-US",
            "location_types": "city"

        }
        iata_reply = requests.get(url=locations_endpoint, params=parameters, headers=headers)
        iata_code = iata_reply.json()["locations"][0]["code"]
        return iata_code

    def find_flights(self, dest):
        find_flights_endpoint = f"{FLIGHT_ENDPOINT}/v2/search"
        headers = {"apikey": FLIGHT_API}
        parameters = {
            "fly_from": "LON",
            "fly_to": dest,
            "date_from": self.current_date.strftime("%d/%m/%Y"),
            "date_to": self.six_month_date.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "GBP",
            "max_stopovers": 0,
            "limit": 1
        }
        find_flight_reply = requests.get(url=find_flights_endpoint, params=parameters, headers=headers)
        try:
            flight_details = find_flight_reply.json()["data"][0]
        except IndexError:
            print(f"No flights found for {dest}")
            return None

        flight_data = FlightData(
            price=flight_details["price"],
            flyfrom=flight_details["flyFrom"],
            cityfrom=flight_details["cityFrom"],
            flyto=flight_details["flyTo"],
            cityto=flight_details["cityTo"],
            out_date=flight_details["route"][0]["local_departure"].split("T")[0],
            return_date=flight_details["route"][1]["local_departure"].split("T")[0]
        )

        print(f"{flight_data.arriving_city}: £{flight_data.price}")
        return flight_data

