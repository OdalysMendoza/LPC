from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json
import argparse
import requests

parser = argparse.ArgumentParser()  
parser.add_argument("-mensaje", dest="param1")
parser.add_argument("-destinatario", dest="param2")
params = parser.parse_args()  
 
data = {}
# {
# "user: "odalys.mendozagz@uanl.edu.mx"
# "pass": "password_super_secreto"
# }
#
#
with open("pass.json") as f:
    data = json.load(f)
# create and setup the parameters of the message
email_msg = MIMEMultipart()
email_msg["From"] = data["user"]
receipents = (params.param2)
email_msg["To"] = ", ".join(receipents)
email_msg["Subject"] = "Salu2"

# add in the message body
message = (params.param1)
email_msg.attach(MIMEText(message, "plain"))

# create server
server = smtplib.SMTP("smtp.office365.com:587")
server.starttls()
# Login Credentials for sending the mail
server.login(data["user"], data["pass"])


# send the message via the server.
server.sendmail(email_msg["From"], receipents, email_msg.as_string())
server.quit()
print("successfully sent email to %s:" % (email_msg["To"]))
