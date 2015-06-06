import mimetypes
import os
from email.mime.multipart import MIMEMultipart
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText



def generate_email(toaddress, body, attachments):
    ''' Function to write an email including attachments '''

    msg = MIMEMultipart()

    msg['From'] = 'me@me.com'
    msg['To'] = toaddress
    body_msg = MIMEText(body, 'plain')
    msg.attach(body_msg)

    if attachments:
        for fn in attachments:

            # if file exists
            if (os.path.isfile(fn)): 
                try:
                    format, enc = mimetypes.guess_type(fn)
                    type, subtype = format.split('/')
                except AttributeError:
                    format, enc = ('application/octet-stream', 'None')
            
                type, subtype = format.split('/')
                if type == "text":
                    fp = open(fn)
                    mime = MIMEText(fp.read(), _subtype=subtype)
                elif type == "image":
                    fp = open(fn, 'rb')
                    mime = MIMEImage(fp.read(), _subtype=subtype)
                elif type == 'audio':
                    fp = open(fn, 'rb')
                    mime = MIMEAudio(fp.read(), _subtype=subtype)
                else:
                    fp = open(fn, 'rb')
                    mime = MIMEBase(type, subtype)
                    mime.set_payload(fp.read())

                mime.add_header(
                    'Content-Disposition', 'attachment',
                    filename=os.path.basename(fn)
                )
                msg.attach(mime)
                fp.close()

    return msg

if __name__ == "__main__":
    PATH = str(os.getcwd())
    attach_png = PATH + "\\" + "python-logo.png"
    attach_txt = PATH + "\\" + "sample.txt"
    attachments = [attach_png, attach_txt]
    newemail = generate_email("you@you.com", "Email body.", attachments)
    if newemail:
        print(newemail)
    else:
        print("Email was not created")