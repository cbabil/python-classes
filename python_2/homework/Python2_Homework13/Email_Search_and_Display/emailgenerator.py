'''
Creates a database table for daily jokes
and populate this table based on a static file
'''
import mysql.connector
from database import login_info
from datetime import timedelta
import settings
import jokes
import messages
from email.utils import make_msgid
from email import message_from_string
from email.mime.text import MIMEText

def create_email(curs,sender, recipients, startdate, daycount, tbl):
    # Loop through our days
    for day in range(daycount):
        d = startdate + timedelta(days=day)

        # Create our message
        for name, recipient in recipients:
            
            msg = message_from_string(name + ', \n' + 'Joke of the day')
            msg['To'] = recipient
            msg['Subject'] = 'Joke of the Day - ' + str(d)
            messageDate = d.strftime('%d %b %Y %H:%M:%S - 0500')
            From = sender
            MessageID= make_msgid()
            body = jokes.retrieve(curs,'jotd')
            msg = MIMEText(body,'plain')

            messages.insert(curs, MessageID, messageDate, name,  From, msg.as_string(), tbl)
            
if __name__=='__main__':
    
    db = mysql.connector.Connect(**login_info)
    curs = db.cursor()
    jotd_tbl = 'jotd'
    jotd_file = "jokes.txt"
    
    # Create jokes db
    jotd_drop_status = jokes.drop(curs, jotd_tbl)
    print(jotd_drop_status)
    jotd_create_status = jokes.create(curs, jotd_tbl)
    print(jotd_create_status)
    jotd_insert_status = jokes.insert(
        curs, jotd_file, jotd_tbl) 
    print(jotd_insert_status)   
    # Create email db
    email_tbl = 'message' 
    message_drop_status = messages.drop(curs, email_tbl)
    print(message_drop_status)
    message_create_status = messages.create(curs, email_tbl)
    print(message_create_status)
    
    # Create email message
    print('Creating email messages...')
    startdate = settings.STARTTIME
    daycount = settings.DAYCOUNT
    recipients = settings.RECIPIENTS
    sender = settings.SENDER
    create_email(curs,sender, recipients, startdate, daycount, email_tbl)
