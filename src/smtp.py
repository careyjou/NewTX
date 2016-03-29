import json
import os
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def sendGmailSmtp(strGmailUser,strGmailPassword,strRecipient,strSubject,strContent):
    strMessage = MIMEMultipart()
    strMessage['From'] = strGmailUser
    strMessage['To'] = strRecipient
    strMessage['Subject'] = strSubject
    strMessage.attach(MIMEText(strContent))
    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(strGmailUser, strGmailPassword)
    mailServer.sendmail(strGmailUser, strRecipient, strMessage.as_string())
    mailServer.close()
    return 'sent'

if __name__ == '__main__':
    # for testing
    infile = '../configs/subscriber.json'
    with open(infile, 'r') as infile:
        ret = json.load(infile)

    for receiver in ret:
        print "To " + receiver + ": " + sendGmailSmtp('software.ellie','ifdadyajopyggrtd','yoshijava@gmail.com','Test for project ellie','as title')
