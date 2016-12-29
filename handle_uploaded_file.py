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


    recipients = ['idearise.msrit@gmail.com'] #receiver
    emaillist = [elem.strip().split(',') for elem in recipients]
    msg = MIMEMultipart()
    msg['Subject'] = "resume for idea "+str(nameOfIdea)#str(sys.argv[1])
    msg['From'] = 'idearise.msrit@gmail.com'
    msg['Reply-to'] = 'idearise.msrit@gmail.com'

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
    server.login("idearise.msrit@gmail.com", "asdf1234!@#$")

    server.sendmail(msg['From'], emaillist , msg.as_string())

def handle_uploaded(rece):
#    with open('try.txt', 'wb+') as destination:
 #       for chunk in f.chunks():
  #          destination.write(chunk)
#!/usr/bin/env python


    recipients = ['idearise.msrit@gmail.com'] #rece
    emaillist = [elem.strip().split(',') for elem in recipients]
    msg = MIMEMultipart()
    msg['Subject'] = "guidelines for idearise "#str(sys.argv[1])
    msg['From'] = 'idearise.msrit@gmail.com'
    msg['Reply-to'] = 'idearise.msrit@gmail.com'

    msg.preamble = 'Multipart massage.\n'

    part = MIMEText("Hi, please find the attached file")
    msg.attach(part)
    #str(sys.argv[2])
    part = MIMEApplication(open('uploads/guideline.pdf',"rb").read())
    part.add_header('Content-Disposition', 'attachment', filename=str('IdeaRiseGuideline.pdf'))
    msg.attach(part)


    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login("idearise.msrit@gmail.com", "asdf1234!@#$")

    server.sendmail(msg['From'], emaillist , msg.as_string())

def handle_upload_sendidea(f,ideaname):
#    with open('try.txt', 'wb+') as destination:
 #       for chunk in f.chunks():
  #          destination.write(chunk)
#!/usr/bin/env python


    recipients = ['iderise.msrit@gmail.com']
    emaillist = [elem.strip().split(',') for elem in recipients]
    msg = MIMEMultipart()
    msg['Subject'] = "file for idearise of idea "+str(ideaname)#str(sys.argv[1])
    msg['From'] = 'idearise.msrit@gmail.com'
    msg['Reply-to'] = 'idearise.msrit@gmail.com'

    msg.preamble = 'Multipart massage.\n'

    part = MIMEText("Hi, please find the attached file")
    msg.attach(part)
    #str(sys.argv[2])
    k="uploads/"+f
    part = MIMEApplication(open(k,"rb").read())
    part.add_header('Content-Disposition', 'attachment', filename=str(f))
    msg.attach(part)


    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login("idearise.msrit@gmail.com", "asdf1234!@#$")

    server.sendmail(msg['From'], emaillist , msg.as_string())

