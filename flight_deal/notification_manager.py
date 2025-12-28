from dotenv import load_dotenv
import os 
import smtplib

load_dotenv()

class NotificationManager:
    
    def __init__(self):
        self.sender_email = os.getenv("SENDER_EMAIL")
        self.password = os.getenv("password") 
        self.reciver_email=os.getenv("EMAIL_ADDRS")
        

    def send_email (self,message):
        
        conntion = smtplib.SMTP("smtp.gmail.com")
        conntion.starttls()
        conntion.login(user=self.sender_email, password=self.password)
        conntion.sendmail(from_addr=self.sender_email,to_addrs=self.reciver_email,msg=message)
        conntion.close()