#gmail_sender.py

from email import message
import smtplib
import ssl

port = 465
smtp_server = "smtp.gmail.com"
sender_email = "email@gmail.com"
receiver_email = "EMAIL@outlook.com"
password = "PASSWORD"

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    try:
        server.login(sender_email, password)
        res = server.sendmail(sender_email, receiver_email, message)
        print('Wow! email sent!')
    except:
        print("Sorry, could not login or send the email")