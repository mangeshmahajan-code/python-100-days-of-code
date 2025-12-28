import os
from pprint import pprint
from dotenv import load_dotenv
import requests
load_dotenv()


class DataManager:
    """
    Responsible for managing flight destination data stored in Google Sheets.

    This class interacts with the Sheety API to:
    - Retrieve destination data from a Google Sheet
    - Update existing rows (e.g., IATA codes, prices)
    - Keep the local data structure in sync with the sheet

    The Google Sheet acts as the single source of truth for all destination data.
    """
    def __init__(self):
        self.sheety_endpoint=os.getenv("sheety_endpoint")
        self.sheety_token=os.getenv("TOKEN")
        self.sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {self.sheety_token}"
    }
        self.destination_data={}



    def get_destination(self):
        '''Get the data in the google sheet with get request and store it in self.destination_data also returen the data 
        '''
    
        sheet_request=requests.get(url=self.sheety_endpoint,headers=self.sheety_headers)
        # sheet_request.raise_for_status()
        data=sheet_request.json()
        self.destination_data=data["prices"]
        return data["prices"]
    
    def update_destination (self):
        '''Update the data in the google sheet with put request  '''
        for row in self.destination_data:
            new_data={
                "price":{
                    "iataCode":row["iataCode"]
                }
            }
            responce =requests.put(
                url=f"{self.sheety_endpoint}/{row['id']}",
                json=new_data,
                headers=self.sheety_headers
            )
            # responce.raise_for_status()