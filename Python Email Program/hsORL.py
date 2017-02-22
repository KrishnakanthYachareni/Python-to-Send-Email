import os
import time

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def send_email(iM,s):

        fromaddr = 'doorbell5693@gmail.com'
	toaddrs=str(iM)
        msg = MIMEMultipart()

        text = MIMEText(str(s))
        msg['Subject'] = 'RPI  NOTIFICATION'
        msg.attach(text)
        img_data = open('test1.jpg', 'rb').read()
        image = MIMEImage(img_data, name='test1.jpg')
        msg.attach(image)

        # Credentials (if needed)
        username = 'doorbell5693@gmail.com'
        password = 'carvingnotions'

        # The actual mail send
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg.as_string())
        server.quit()
        print('e-Mail Sent')

#send_email('shyamkumar6555@gmail.com','Test Mail')
