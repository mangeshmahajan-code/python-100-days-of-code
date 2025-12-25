import requests
# Use open trivia questions api to import question in json format 
parameters = {
    "amount":10,
    "type":"boolean",
}
responce = requests.get(url="opentdb api endpoint",params=parameters)
responce.raise_for_status()
data = responce.json()
question_data=data["results"]
