# importing the necessary modules and functions
from email.message import EmailMessage
import ssl
import smtplib

# a function to generate the emails and send them
def generate_email(email_sender, email_reciever, subject, body, email_password):
    # create and fill the message
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_reciever
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    # a secure connection to the server
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
        # login
        smtp.login(email_sender, email_password)
        # send
        smtp.sendmail(email_sender, email_reciever, em.as_string())