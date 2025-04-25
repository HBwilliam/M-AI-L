from imap_tools import MailBox, AND
from datetime import date, timedelta
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASS = os.getenv('EMAIL_PASS')
IMAP_SERVER = os.getenv('IMAP_SERVER')

# gmail : imap.gmail.com
# outlook : imap-mail.outlook.com
# yahoo : imap.mail.yahoo.com

def get_email_today(mailbox):
        today = date.today()
        for msg in mailbox.fetch(AND(date=today)):
            print(msg.date, msg.subject, len(msg.text or msg.html))

def get_email_yesterday(mailbox):
        yesterday = date.today() - timedelta(days=1)
        for msg in mailbox.fetch(AND(date=yesterday)):
            print(msg.date, msg.subject, len(msg.text or msg.html))

if __name__ == '__main__':
    mailbox = MailBox(IMAP_SERVER).login(EMAIL_USER, EMAIL_PASS)
    get_email_today(mailbox)
          