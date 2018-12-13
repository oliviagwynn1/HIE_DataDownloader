import sendgrid
import os
from sendgrid.helpers.mail import *


def send_email(address):
    """
    Sends email if patient is tachycardic
    """
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("nmolino22@gmail.com")
    to_email = Email(address)
    subject = "Patient tachycardic warning "
    content = Content("text/plain", "Warning: Your patient is tachycardic")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)

