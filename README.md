Email Sender:

This is a simple command-line Python script that sends an email using the SMTP_SSL protocol. 

The email contains a subject and a body message.

Dependencies:
Python 3.x
smtplib and ssl (both are part of the Python Standard Library)

Setup:
Ensure that you have Python 3.x installed on your computer.
Create a file named py_code.py and store your Gmail app password in a variable named password:

  password = "your_gmail_app_password"
  
Replace the email_sender variable with your Gmail email address.
Replace the email_receiver variable with the recipient's email address.
Update the subject and body variables as needed.

How to Run:
 Run the Email Sender script by executing the Python script
  python email_sender.py
  
The email will be sent to the specified recipient.


Code Structure:
email_sender: Sender's email address (your Gmail address)

email_password: Gmail app password (imported from the py_code.py file)

email_receiver: Recipient's email address

subject: Email subject

body: Email body message

em: Instance of the EmailMessage class

context: SSL context for secure communication

smtplib.SMTP_SSL: Establishes a connection with the Gmail SMTP server and sends the email

Usage:
  The script sends an email with the specified subject and body message to the recipient using the sender's Gmail account. It uses the SMTP_SSL protocol for secure communication with the Gmail SMTP server.
