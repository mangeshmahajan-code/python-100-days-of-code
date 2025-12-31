from dotenv import load_dotenv
import os 
import smtplib

load_dotenv()

class NotificationManager:
    
    def __init__(self):
        self.sender_email = os.getenv("SENDER_EMAIL")
        self.password = os.getenv("password") 
        self.reciver_email=os.getenv("EMAIL_ADDRS")
        

    def send_email (self,email_list,message):
        for email in email_list :
            conntion = smtplib.SMTP("smtp.gmail.com")
            conntion.starttls()
            conntion.login(user=self.sender_email, password=self.password)
            conntion.sendmail(from_addr=self.sender_email,to_addrs=email,msg=f"Subject :New Low Price Flight!\n\n{message}")
            conntion.close()
       