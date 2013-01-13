#!/usr/bin/env python

"""
Send an email via Gmail either as a text or as an HTML.

# from jabbapylib.mail import gmail_send
"""

import os
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders


def mail_text(sender, to, subject, text, attach=None):
    """
    Send a TEXT mail via gmail.

    It can also send an attachment.
    "sender" is a dictionary with these keys:
    - gmail_user
    - gmail_name
    - gmail_pwd
    "to" is the target email address
    "subject" is the subject of the message
    "text" is the message text in text format
    "attach" is optional; it's the attached file's filename
    """
    msg = MIMEMultipart()

    msg['From'] = sender['gmail_name']
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(text, 'plain'))

    if attach:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(attach, 'rb').read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition',
            'attachment; filename="%s"' % os.path.basename(attach))
        msg.attach(part)

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(sender['gmail_user'], sender['gmail_pwd'])
    #mailServer.sendmail(gmail_user, to, msg.as_string())   # just e-mail address in the From: field
    mailServer.sendmail(sender['gmail_name'], to, msg.as_string())   # name + e-mail address in the From: field
    mailServer.close()


def mail_html(sender, to, subject, html, attach=None):
    """
    Send an HTML mail via gmail.

    It can also send an attachment.
    "sender" is a dictionary with these keys:
    - gmail_user
    - gmail_name
    - gmail_pwd
    "to" is the target email address
    "subject" is the subject of the message
    "html" is the message text in HTML format
    "attach" is optional; it's the attached file's filename
    """
    msg = MIMEMultipart()

    msg['From'] = sender['gmail_name']
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(html, 'html'))

    if attach:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(attach, 'rb').read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition',
            'attachment; filename="%s"' % os.path.basename(attach))
        msg.attach(part)

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(sender['gmail_user'], sender['gmail_pwd'])
    #mailServer.sendmail(gmail_user, to, msg.as_string())   # just e-mail address in the From: field
    mailServer.sendmail(sender['gmail_name'], to, msg.as_string())   # name + e-mail address in the From: field
    mailServer.close()

#############################################################################

if __name__ == "__main__":
    import getpass

    user = raw_input('gmail username: ')
    name = raw_input('displayed name: ')
    pwd = getpass.getpass('gmail password: ')
    sender = {
        'gmail_user': user,
        'gmail_name': name,
        'gmail_pwd': pwd
    }

    mail_html(sender, "...",
        "Hello from Python!",
        "This is an e-mail sent with Python. Visit <a href='http://www.python.org'>python.org</a>.")
