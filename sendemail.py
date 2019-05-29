import smtplib

"""
SMTP Server Information
1. Gmail.com: smtp.gmail.com:587
2. Outlook.com: smtp-mail.outlook.com:587
3. Office 365: outlook.office365.com
Please verify your SMTP settings info.
"""

FROM = "xxxx@xxxx.com"
PWD = "xxxxx"
recipient = ["yyy@yyy.com"]
TO = recipient if isinstance(recipient, list) else [recipient]
SUBJECT = "Test Message"
TEXT = "Hello Mahendra"


# Function that send email.
def send_mail(username, password, from_addr, to_addrs, message):
    server = smtplib.SMTP('smtp-mail.outlook.com', '587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(from_addr, to_addrs, message)
    server.quit()


def prepare():
    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    send_mail(FROM, PWD, FROM, TO, message)


if __name__ == '__main__':
    prepare()
