'''
Creates a database table for daily jokes
and populate this table based on a static file
'''

from datetime import datetime
import random
import mysql.connector
from mysql.connector import errorcode
from database import login_info

db = mysql.connector.Connect(**login_info)
cursor = db.cursor()
tbl = 'jotd'
filename = "jokes.txt"


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
    CREATE TABLE %s(
        id INTEGER AUTO_INCREMENT PRIMARY KEY,
        text LONGTEXT
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


def insert(curs, filename, tbl):
    '''
    Insert jokes into jotd
    '''

    try:
        with open(filename, 'r') as fh:
            lines = fh.readlines()
            for line in lines:
                line = line.rstrip()
                #d = datetime.strftime(startdate, "%Y-%m-%d %H:%M:%S")
                INSERT_DATA = """INSERT INTO {} (text) VALUES (\'{}\');""".format(tbl,line)
                curs.execute(INSERT_DATA)
    except mysql.connector.IntegrityError as err:
        message = "Insert table {}: {}".format(tbl, err)
    else:
        message = "Insert table {}: OK".format(tbl)

    return message


def retrieve(curs, tbl):
    '''
    Retrieves jokes from jotd randomly
    '''

    try:
        curs.execute("""SELECT MIN(id) from {}""".format(tbl))
        minid = curs.fetchone()[0]
        
        curs.execute("""SELECT MAX(id) from {}""".format(tbl))
        maxid = curs.fetchone()[0]
        randid = random.randint(minid, maxid)
        
        curs.execute("""SELECT * from {} where id={}""".format(tbl,randid))
        joke = curs.fetchone()[1]

    except mysql.connector.InterfaceError as err:
        joke = err
         
    return joke


def close():
    '''
    Closes the cursor, commits the changes and disconnects from server
    '''
    cursor.close()
    db.commit()
    db.close()
