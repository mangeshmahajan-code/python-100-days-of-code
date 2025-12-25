import requests
from datetime import datetime
from dotenv import load_dotenv
import os
load_dotenv()

APP_ID = os.getenv("NIX_APP_ID")
APP_KEY = os.getenv("NIX_API_KEY")

TOKEN = os.getenv("TOKEN")

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

# API setup for 100daysofcodeapi which returns the json by converting simple english to it.
exercise_endpoint =os.getenv("exercise_endpoint")
exercise_input = input("Enter which exercise you have done :")
headers ={
    "Content-Type": "application/json",
  "x-app-id":APP_ID,
  "x-app-key":APP_KEY,
 }
data ={
    "query": exercise_input,
  "weight_kg": 70,                  
  "height_cm": 170,                 
  "age": 18,                        
  "gender": "male" ,                
}

response = requests.post(url=exercise_endpoint,json=data,headers=headers)
result = response.json()
print(response.status_code)
api_output = result["exercises"][0]

sheety_endpoint = os.getenv("sheety_endpoint")

sheety_data = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": api_output["name"].title(),
        "duration": api_output["duration_min"],
        "calories": api_output["nf_calories"]
    }
}

sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TOKEN}"
}

sheety_request = requests.post(url=sheety_endpoint,json=sheety_data,headers=sheety_headers)
print(sheety_request.status_code)
