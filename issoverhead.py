import requests
from datetime import datetime
import smtplib

SENDER_EMAIL = "mangesmahajan@gmail.com"
password = "acisoqfadsngobnu" 
EMAIL_ADDRS =  "mangesmahajan@gmail.com"
MY_LAT =18.584781
MY_LONG =73.736593

def send_email (email_addrs):
    '''Send a email when the iss is near the location .'''
    conntion = smtplib.SMTP("smtp.gmail.com")
    conntion.starttls()
    conntion.login(user=SENDER_EMAIL, password=password)
    conntion.sendmail(from_addr=SENDER_EMAIL,to_addrs=email_addrs,msg="Subject : look up👆\n\nThe iss is above you in the sky")
    conntion.close()

def is_iss_overhead():
    '''Check the location of iss and if it's near your location return true else false'''
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT-5<=iss_latitude<= MY_LAT+5 and MY_LONG-5<= iss_longitude<=MY_LAT+5:
        return True
    else:
        False



def is_it_dark():
    '''check is it night then return true else false'''
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
   
    if sunset<time_now.hour>sunrise:
        return True
    else:
       return False

# Check the conditon and run the send email when true
if is_iss_overhead and is_it_dark :
   send_email(EMAIL_ADDRS)




