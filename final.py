import smtplib
import time
import datetime
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
from base64 import encodebytes
import csv
import os, sys
import psycopg2 
from config import config
from GetServerDetails import getserverdetails
from GetMailData import getmaildata
params = config()			
# connect to the PostgreSQL server
print('Connecting to the PostgreSQL database...')
conn = psycopg2.connect(**params)
cur = conn.cursor()  
cur.execute("select * from txn_event_notifications where status = 0")
rows = cur.fetchall()
print("The number of parts: ", cur.rowcount)
for row in rows:
    print(row)
    print(row[5])
    cur.close()
    subject = row[7]
    body = row[8]
    fromaddr = "letsmove.suite@gmail.com"
    toaddr = [row[5]]
    #tocc  = ["javed.bhai@gmail.com","nikhil66766@gmail.com" , "nabin.kumar.mca10@gmail.com"]
    #   Date
    today = datetime.datetime.today ()
    tday = today.strftime ("%m-%d-%Y")

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    recto = ", ".join(toaddr)
    #reccc = ", ".join(tocc)
    print(recto)
    msg['To'] = recto
    #msg['Cc'] = reccc
    #print(reccc)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))
    
if row[9] == False:
 filename = "test.csv"
 attachment = open(r"E:\softwares\test.csv")
 part = MIMEBase('application', 'octet-stream')
 part.set_payload((attachment).read())
 encoders.encode_base64(part)
 part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 msg.attach(part)
 
try:
 server = smtplib.SMTP('smtp.gmail.com', 587)
 server.starttls()
 server.login(fromaddr, "suite@jamsuite")
 text = msg.as_string()
 server.sendmail(fromaddr, toaddr, text)
 server.quit()
except smtplib.SMTPException as e:
 print(str(e))