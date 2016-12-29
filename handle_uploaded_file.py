from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys

def handle_uploaded_file(receiver,sender,f,nameOfIdea):
#    with open('try.txt', 'wb+') as destination:
 #       for chunk in f.chunks():
  #          destination.write(chunk)
#!/usr/bin/env python


    recipients = ['shikharsrivastavalfs@gmail.com']
    emaillist = [elem.strip().split(',') for elem in recipients]
    msg = MIMEMultipart()
    msg['Subject'] = "resume for idea "+str(nameOfIdea)#str(sys.argv[1])
    msg['From'] = 'shikharsrivastavalfs@gmail.com'
    msg['Reply-to'] = 'shikharsrivastavalfs@gmail.com'

    msg.preamble = 'Multipart massage.\n'

    part = MIMEText("Hi, please find the attached file")
    msg.attach(part)
    #str(sys.argv[2])
    part = MIMEApplication(open(f,"rb").read())
    part.add_header('Content-Disposition', 'attachment', filename=str('django.pdf'))
    msg.attach(part)


    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login("shikharsrivastavalfs@gmail.com", "cuteunnatiis1234")

    server.sendmail(msg['From'], emaillist , msg.as_string())

