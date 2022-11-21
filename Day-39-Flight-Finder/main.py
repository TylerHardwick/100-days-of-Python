from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_sheety_data()
for item in sheet_data:
    if item["iataCode"] == "":
        new_iata = flight_search.get_iata(item["city"])
        item["iataCode"] = new_iata
        data_manager.update_iata(row_id=item["id"], iata=new_iata)

    flight = flight_search.find_flights(item["iataCode"])
    if flight.price <= item["lowestPrice"]:
        message = f"Low price alert! Only £{flight.price} to fly from {flight.departure_city}-{flight.departure_airport_code} " \
                f"to {flight.arriving_city}-{flight.arriving_airport_code}, from {flight.out_date} to {flight.return_date}. "
        notification_manager.flight_found_sms(message=message)










#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.