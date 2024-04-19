# -*- coding: utf-8 -*-
"""
Send email and msg
@author: Victor Prudente
"""

import smtplib
# from email.message import EmailMessage

"""

1- You need configure your email (in my case, gmail) to use on APP password. This will allow you to send emails and sms using python
    - source:(https://www.youtube.com/watch?v=YKn6iRlYd_Q) 
    - https://myaccount.google.com/apppasswords

2- I am not creating this from strech. Here there are some references that I used to create it:
    - https://www.youtube.com/watch?v=3247tuklMEk
    - https://github.com/AdamGetbags/emailToSMS/blob/main/emailToSMSConfig.py
    - https://medium.com/testingonprod/how-to-send-text-messages-with-python-for-free-a7c92816e1a4

"""




CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@messaging.sprintpcs.com"
}
 
EMAIL = "your.email@gmail.com"
PASSWORD = 'xxxx xxxx xxxx xxxx' # from the app password
 
def send_sms(phone_number, carrier, message):
    
    recipient = phone_number + CARRIERS[carrier]
    auth = (EMAIL, PASSWORD)
 
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])
 
    server.sendmail(auth[0], recipient, message)
    server.close()



def send_email(reciverEmail, subject, body): 
    
    
    #The smtplib.SMTP() class is typically used to establish a connection to an SMTP server, allowing you to send emails using your Python script.
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()# Use this line for TLS connection
    auth = (EMAIL, PASSWORD)

    #Loguin in your accoutn
    server.login(auth[0], auth[1])

    #creating the msg
    message = f"Subject: {subject}\n\n{body}"


    #Send the email
    server.sendmail(auth[0], reciverEmail, message)
    server.close()

def send_email_msg(reciverEmail, subject, body, phone_number, carrier):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()# Use this line for TLS connection
    auth = (EMAIL, PASSWORD)

    #Loguin in your accoutn
    server.login(auth[0], auth[1])

    #creating the msg
    message = f"Subject: {subject}\n\n{body}"


    #Send the email
    server.sendmail(auth[0], reciverEmail, message)
    
    # server.starttls()# Use this line for TLS connection
    # auth = (EMAIL, PASSWORD)

    # #Loguin in your accoutn
    # server.login(auth[0], auth[1])

    recipient = phone_number + CARRIERS[carrier]
 
    server.sendmail(auth[0], recipient, message)
    server.close()






