import smtplib
from email.message import EmailMessage
import imghdr

from matplotlib.cbook import report_memory

EMAIL_ADDRESS = 'vetleeraa@gmail.com'
EMAIL_PASSWORD = 'tfwqebcilwtekiyq'

def sendmail():
    global msg
    msg = EmailMessage()
    msg['Subject'] = 'Daily IPS report'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'vetleeraa@gmail.com'  # insert head of security's information here

    with open('incident_report.txt', 'r') as f: # insert path to report file here
        file_data = f.read()
        file_type = imghdr.what(f.name)

    msg.add_attachment(file_data)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: # this has to change according to the mailing system being used in the task
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        smtp.send_message

sendmail()