'''
Creates a database table for daily email
and populate this table with jokes
'''

import mysql.connector
from mysql.connector import errorcode
from database import login_info
import settings

db = mysql.connector.Connect(**login_info)
cursor = db.cursor()
tbl = 'message'
daycount = settings.DAYCOUNT
recipients = settings.RECIPIENTS
sender = settings.SENDER


def drop(curs, tbl):
    '''
    Drops database table tbl
    '''

    DROP_TABLE = """ DROP TABLE IF EXISTS {} """.format(tbl)

    try:
        curs.execute(DROP_TABLE)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_TABLE_ERROR:
            message = "Droping table {}: does not exists".format(tbl)
    else:
        message = "Droping table {}: OK".format(tbl)

    return message


def create(curs, tbl):
    '''
    Creates database table tbl
    '''

    CREATE_TABLE = """\
        CREATE TABLE IF NOT EXISTS %s(
        msgID INTEGER AUTO_INCREMENT PRIMARY KEY,
        msgMessageID VARCHAR(128),
        msgDate VARCHAR(128),
        msgSenderName VARCHAR(128),
        msgSenderAddress VARCHAR(128),
        msgText LONGTEXT
    )""" % tbl

    try:
        curs.execute(CREATE_TABLE)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            message = "Creating table {}: already exist".format(tbl)
        else:
            message = err.msg
    else:
        message = "Creating table {}: OK".format(tbl)

    return message

def insert(curs, mID, mDate, mFrom, mTo, mText, tbl):
    '''
    Insert msg into message
    '''
    
    try:
        curs.execute("INSERT INTO message (msgMessageID, msgDate, msgSenderName, msgSenderAddress, msgText) VALUES (%s, %s, %s, %s, %s)", (mID, mDate, mFrom, mTo, mText))
        
        
        #INSERT_DATA = "INSERT INTO {} (msgMessageID, msgDate, msgSenderName, msgSenderAddress, msgText) VALUES (\'{}\', \'{}\', \'{}\', \'{}\', \'{}\')""".format(tbl, mID, mDate, mSenderName, mSenderAddress, mText)
        #curs.execute(INSERT_DATA)
    except mysql.connector.IntegrityError as err:
        message = "Insert table {}: {}".format(tbl, err)
    else:
        message = "Insert table {}: OK".format(tbl)
    return message


def retrieveall(curs,tbl):
    '''
    Retrieves messages from message
    '''

    try:
        curs.execute("""SELECT * from message""", format(tbl))
        emails = curs.fetchall()
    except mysql.connector.InterfaceError as err:
        emails = ""

    return emails


def close():
    '''
    Closes the cursor, commits the changes and disconnects from server
    '''
    cursor.close()
    db.commit()
    db.close()