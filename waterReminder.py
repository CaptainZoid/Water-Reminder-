import email, smtplib, ssl
from datetime import datetime
import time
import json
#ip address for raspberry pi is  10.0.0.241
def send_sms_via_email(number: str, message: str, sender_credentials: tuple, provider: str,
    subject: str="Water Reminder from your sexy boyfriend", smtp_server ="smtp.gmail.com", smpt_port: int = 465):
    sender_email, email_password = sender_credentials
    reciever_email = f"{number}@pcs.rogers.com"
    #reciever_email = f"{number}@msg.koodomobile.com"
    #reciever_email = f"{number}@fido.ca"
    email_message = f"Subject:{subject}\nTo:{reciever_email}\n{message}"

    with smtplib.SMTP_SSL(smtp_server, smpt_port, context=ssl.create_default_context()) as email:
        email.login(sender_email, email_password)
        email.sendmail(sender_email, reciever_email, email_message)


def main():
    f = open('providers.JSON', 'r')
    data = json.load(f)

    now = datetime.now()
    current_hour = now.strftime("%H")
    current_min = now.strftime("%M")
    
    if((current_hour == "10" and current_min == "00" ) or (current_hour == "13" and current_min == "00" ) or
    (current_hour == "16" and current_min == "00" ) or (current_hour == "20" and current_min == "00" ) or
    (current_hour == "22" and current_min == "00" ) or (current_hour == "18" and current_min == "20")):
        number = "4379960496"
        message = "This is your first water reminder, PLEASE DRINK WATER NOW DO IT NOW NOW NOW NOW"
        sender_credentials = ("pythonscriptsasan@gmail.com", "Boogh2345")
        send_sms_via_email(number, message, sender_credentials)
        time.sleep(60)

if __name__ == '__main__':
    while True:
        main()
