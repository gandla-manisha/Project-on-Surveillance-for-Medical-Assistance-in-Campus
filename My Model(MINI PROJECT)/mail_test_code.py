import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import geocoder
g = geocoder.ip('me')
l = g.latlng
#url = f'https://www.google.com/maps?q={l[0]},{l[1]}'

mail_content = f"This is info from a xyz, caught the and its location is url in google maps"
# The mail addresses and password
sender_address = 'medicalcenterpqr@gmail.com'
sender_pass = 'vury tlgl fhlr kini' #'rgqdhwantzrgilkv'
receiver_address = "gandlamanisha599081@gmail.com"
# Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = f'Emergency required '  # The subject line
# The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
# Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
session.starttls()  # enable security
session.login(sender_address, sender_pass)  # login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')