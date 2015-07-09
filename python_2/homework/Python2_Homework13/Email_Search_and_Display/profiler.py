import timeit
import jokes
import messages
import mysql.connector
from database import login_info

# Database connection
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
print('Running profiler...')
daycounts = (1, 10, 50, 100, 500)
for days in daycounts:
    setup = """
import mysql.connector
from database import login_info
import settings
import emailgenerator
startdate = settings.STARTTIME
recipients = settings.RECIPIENTS
sender = settings.SENDER
db = mysql.connector.Connect(**login_info)
curs = db.cursor()
email_tbl = 'message'
days = %d""" % days

    # Run 10 times and report only the best one
    bestrun = min(timeit.repeat(
        'emailgenerator.create_email(curs,sender,recipients, startdate, days, email_tbl)', setup=setup, repeat=10, number=1))

    print("daycount={0}\tBest Time={1}\tAvg Time/msg={2}".format(
        days, round(bestrun, 6), round(bestrun / days, 6)))





    
     

    
   
    


