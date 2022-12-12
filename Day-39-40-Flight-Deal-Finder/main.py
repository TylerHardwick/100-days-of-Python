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

    flight = flight_search.find_flights(item["iataCode"], item["city"])
    try:
        if flight.price <= item["lowestPrice"]:
            message = f"Subject:New low price flight!\n\nLow price alert! Only £{flight.price} to fly from {flight.departure_city}-{flight.departure_airport_code} " \
                    f"to {flight.arriving_city}-{flight.arriving_airport_code}, from {flight.out_date} to {flight.return_date}."
            if flight.stop_overs > 0:
                message += f"\nFlight has 1 stop over, via {flight.via_city}."
            message += f"\n{flight.link}"

            email_list = data_manager.get_user_email()
            encoded_message = message.encode("utf-8")
            for email in email_list:
                notification_manager.send_emails(email, encoded_message)

            # notification_manager.flight_found_sms(message=message)
    except AttributeError:
        pass









#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.