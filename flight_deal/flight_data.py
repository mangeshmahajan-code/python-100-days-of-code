class FlightData:
    
    def __init__(self,price,origin_airport,destination_airport,out_date,return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date


def find_cheapest_flight(data):
     
    if data is None or not data["data"]:
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")
     
    first_flight=data["data"][0]
    lowest_price =float(first_flight["price"]["grandTotal"])
    departure_airport = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    arrival_airport = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    departure_date=first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    arrival_date=first_flight["itineraries"][0]["segments"][0]["arrival"]["at"].split("T")[0]

    cheap_flight = FlightData(lowest_price,departure_airport,arrival_airport,departure_date,arrival_date)

    for flight in data["data"]:
        price_of_flight = float(flight["price"]["grandTotal"])
        if lowest_price > price_of_flight :
            lowest_price = price_of_flight
            departure_airport = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            arrival_airport = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            departure_date=flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            arrival_date=flight["itineraries"][0]["segments"][0]["arrival"]["at"].split("T")[0]
            cheap_flight = FlightData(lowest_price,departure_airport,arrival_airport,departure_date,arrival_date)
    
    return cheap_flight