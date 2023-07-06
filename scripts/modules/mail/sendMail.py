import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart
import logging

def send_email(config, pdfTmpFile, SMTPpassword):
    logging.info("Sending mail")
    # Create Multipart Message
    msg = MIMEMultipart()
    msg['Subject'] = config['mail']['subject']
    msg['From'] = config['mail']['from']
    msg['To'] = config['mail']['to']
    # Create File Part
    with open(pdfTmpFile, 'rb') as attachement:
        file_part = MIMEBase("application", "octet-stream")
        file_part.set_payload(attachement.read())
        encoders.encode_base64(file_part)
        file_part.add_header("Content-Disposition", "attachement; filename=report.pdf")
    # Create HTML Part from Template
    with open(config['mail']['template'], "r") as mailtemplate:
        html_part = MIMEText(mailtemplate.read(), 'html')
    # Attach parts to multipart message
    msg.attach(html_part)
    msg.attach(file_part)
    # Send Mail
    with smtplib.SMTP_SSL(config['host'], config['port']) as smtp_server:
       smtp_server.login(config['mail']['from'], SMTPpassword)
       smtp_server.sendmail(config['mail']['from'], config['mail']['to'], msg.as_string())
       logging.info("Mail sent succesfully")
