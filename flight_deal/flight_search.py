import os
from dotenv import load_dotenv
import requests
load_dotenv()
class FlightSearch:
    """
    Handles flight-related search operations using the Amadeus API.

    This class is responsible for:
    - Authenticating with the Amadeus OAuth2 service
    - Retrieving IATA codes for cities
    """

    def __init__(self):
        """
        Initializes the FlightSearch client with API credentials and
        retrieves an access token for subsequent API calls.
        """
        self.api_key = os.getenv("API_KEY")
        self.api_secret= os.getenv("API_SECRET")
        self._token = self._get_new_token()
        self.token_endpoint = os.getenv("Amadeus_endpoint")
        self.amadeus_iata_endpoint = os.getenv("IATA_ENDPOINT")
        self.flight_offer_endpoint=os.getenv("FLIGHT_OFFERS_ENDPOINT")
        

    def get_iata_code(self,city_name):
        """
        Retrieves the IATA code for a given city.
        required city_name as string and 
        Returns:
        str: The IATA city code if found, otherwise 'N/A'.
        """
        params ={
            "keyword":city_name,
            "subType": "CITY"
        }
        headers= {
            "Authorization": f"Bearer {self._token}"
        }
        iata_data= requests.get(url=self.amadeus_iata_endpoint,headers=headers,params=params)
        
        
        try:
            code = iata_data.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return code

    def _get_new_token(self):
        """
        Requests a new OAuth2 access token from the Amadeus API.

        Returns:
            str: Access token for authenticated API requests.
        """

        header = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
        'grant_type': 'client_credentials',
        'client_id': self.api_key,
        'client_secret': self.api_secret
        }
        url ="https://test.api.amadeus.com/v1/security/oauth2/token"
        response= requests.post(url=url,headers=header,data=body)
        response.raise_for_status()
        return response.json()["access_token"]

    def search_for_flight(
        self,
        departure,
        destination,
        departure_date,
        return_date,
        adults=1,
        max_results=10,
        currency="INR",
        is_direct = True,   
    ):
        headers = {
            "Authorization": f"Bearer {self._token}"
        }
        
        params={
            "originLocationCode": departure,
            "destinationLocationCode": destination,
            "departureDate": departure_date.strftime("%Y-%m-%d"),
            "returnDate": return_date.strftime("%Y-%m-%d"),
            "adults": adults,
            "currencyCode": currency,
            "max": max_results,
            "nonStop":"true" if is_direct else "false",
        }
        response = requests.get(url=self.flight_offer_endpoint, headers=headers, params=params)
        data= response.json()["data"]
        if response.status_code != 200:
                    print(f"check_flights() response code: {response.status_code}")
                    print("There was a problem with the flight search.\n"
                        "For details on status codes, check the API documentation:\n"
                        "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                        "-reference")
                    print("Response body:", response.text)
                    return None
        if not data :
            is_direct = False
            print("No direct flight.\nSearching for connected flights.")
            response = requests.get(url=self.flight_offer_endpoint,headers=headers, params=params)
               

        return response.json()
    


