from Scripts.send_email_sms import * #import all functions inside the python file

#To configure carrier and yor app password, change the file in Scripts/send_email_sms.py

# Content that you want to sent
msg = f"Hello world"
subject = 'Python is amazing'

#Just a sms
email = send_sms(phone_number='1111111111', 
                carrier = 'att', 
                 message = msg)

#Just and email
email = send_email(reciverEmail='email@gmail.com', 
            subject =subject, 
            body = msg)


#e-mail and sms
email = send_email_msg(reciverEmail='email@gmail.com', 
            subject = subject, 
            body = msg, 
            phone_number='1111111111', 
            carrier = 'att')