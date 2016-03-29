import json
import os
import smtplib
import time
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def send_gmail_smtp(username, password, recipient, subject, content):
    message = MIMEMultipart()
    message['From'] = username
    message['To'] = recipient
    message['Subject'] = subject
    message.attach(MIMEText(content))
    mail_server = smtplib.SMTP('smtp.gmail.com', 587)
    mail_server.ehlo()
    mail_server.starttls()
    mail_server.ehlo()
    mail_server.login(username,  password)
    mail_server.sendmail(username, recipient, message.as_string())
    mail_server.close()
    return 'sent'

if __name__ == '__main__':
    # for testing
    infile = '../configs/subscriber.json'
    with open(infile, 'r') as infile:
        ret = json.load(infile)

    for receiver in ret:
        subject = time.strftime("From Ellie @ %Y-%m-%d %H:%M:%S")
        content = "As title"
        print "To " + receiver + ": " + send_gmail_smtp('software.ellie', 'ifdadyajopyggrtd', 'yoshijava@gmail.com', subject, content)
