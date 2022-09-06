from email.message import EmailMessage
from py_code import password
import ssl
import smtplib

email_sender = 'azurebarrage@gmail.com'
email_password = password       # importing google app pw from other pyfile.

email_receiver = 'bakewoj229@oncebar.com'

subject = "Greetings!"
body = """Hello, my name is Julian and I am an aspiring Full Stack Software Developer"""

em = EmailMessage()             # instance of email message
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:      # Use SMTP to login and send email
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())