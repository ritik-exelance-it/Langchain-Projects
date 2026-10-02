### Sending Email Agent - send_email

import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from langchain.tools import tool

# 1. Define configuration variables
smtp_server = "smtp.gmail.com"
smtp_port = 587              
def send_email_by_gmail(to:str, subject:str, body_text:str):
    sender_email = os.getenv("GMAIL_ADDRESS")
    password = os.getenv("GMAIL_APP_PASSWORD")
    if not sender_email or not password:
        raise ValueError("Set GMAIL_ADDRESS and GMAIL_APP_PASSWORD in .env.")

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to
    message["Subject"] = subject

    message.attach(MIMEText(body_text, "plain"))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, to, message.as_string())

@tool
def send_email(to:str, subject:str, body:str):
    """
     Send Email to any email address by providing the correct email address, subject and body.
     Args:
        to - email address
        subject - email subject in one line
        body - email body in plane text
    """
    send_email_by_gmail(to, subject, body_text=body)
    return "Email Send Successfully..."

ALL_TOOLS = [send_email]