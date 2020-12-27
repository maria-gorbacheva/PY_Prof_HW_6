
import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Email:

    GMAIL_SMTP = "smtp.gmail.com"
    GMAIL_IMAP = "imap.gmail.com"

    def __init__(self, login='login@gmail.com', password='qwerty'):
        self.login = login
        self.password = password

    def send_email(self, subject='Subject', recipients=None, message='Message', header=None):
        if recipients is None:
            recipients = ['vasya@email.com', 'petya@email.com']

        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        server = smtplib.SMTP(self.GMAIL_SMTP, 587)
        # identify ourselves to smtp gmail client
        server.ehlo()
        # secure our email with tls encryption
        server.starttls()
        # re-identify ourselves as an encrypted connection
        server.ehlo()

        server.login(self.login, self.password)
        server.sendmail(self.login, server, msg.as_string())

        server.quit()

    def receive_email(self, header=None):

        mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()


if __name__ == '__main__':
    my_email = Email('login@gmail.com', 'password')
    # my_email.send_email('Subject', 'somebody@gmail.com', 'Это тестовое письмо')
    my_email.receive_email()