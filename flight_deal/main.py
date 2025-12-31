from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight,FlightData
import time
from datetime import datetime,timedelta
from notification_manager import NotificationManager

data_manager=DataManager()
sheet_data=data_manager.get_destination()
flightsearch = FlightSearch()
notification_manager=NotificationManager()

user_data =data_manager.get_customer_data()
user_email = [user['whatIsYourEmail?'] for user in user_data['users']]

departure_city_iata = "BOM"

if any(sheet_data[0]["iataCode"]=="" for row in sheet_data):
    for row in sheet_data:
        row["iataCode"]  = flightsearch.get_iata_code(row['city'])      
        time.sleep(2)
data_manager.destination_data =sheet_data
data_manager.update_destination()

tomorrow = datetime.now() + timedelta(days=1)
six_months = datetime.now() + timedelta(days=(6*30))

for destination in sheet_data :
    print(f"Getting flights for {destination['city']}...")
    flights = flightsearch.search_for_flight(
        departure=departure_city_iata,
        destination=destination["iataCode"],
        departure_date=tomorrow,
        return_date=six_months,
    )
    cheapest_flight = find_cheapest_flight(flights)

    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stopover_flights = flightsearch.search_for_flight(
        departure=departure_city_iata,
        destination=destination["iataCode"],
        departure_date=tomorrow,
        return_date=six_months,
        is_direct=False
        )

        cheapest_flight = find_cheapest_flight(stopover_flights)
    print(f"{destination['city']}: ₹{cheapest_flight.price}")
    time.sleep(2)

    
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        user_name =  [f"{user['whatIsYourFirstName?']} {user['whatIsYourLastName?']}" for user in user_data['users']]
        message_body=f"Low price alert!\n\n dear user Only Rs.{cheapest_flight.price} to fly from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport} with {cheapest_flight.stops} stop(s), on {cheapest_flight.out_date} until {cheapest_flight.return_date}.\nThank you"
        notification_manager.send_email(email_list=user_email,message=message_body)     