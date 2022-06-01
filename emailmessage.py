import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = 'automated.mail@freelabs.com'
EMAIL_PASSWORD = ''


def sendmail(date):
    msg = EmailMessage()
    msg['Subject'] = 'Daily IPS report'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'head.of.security@freelabs.com'  # insert head of security's information here
    msg.set_content('Incident report')
    msg.add_attachment(open('incident_report', 'r').read(), filaneme = 'incident_report.txt - ' + date)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: # this has to change according to the mailing system being used in the task
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        smtp.send_message(msg)
