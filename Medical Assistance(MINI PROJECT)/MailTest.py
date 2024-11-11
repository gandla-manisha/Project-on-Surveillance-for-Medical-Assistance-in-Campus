# Python code to illustrate Sending mail
# to multiple users
# from your Gmail account
import smtplib

# list of email_id to send the mail
li = ["gandlamanisha599081@gmail.com", "gandlamanisha3563@gmail.com"]

for dest in li:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("medicalcenterpqr@gmail.com", "vury tlgl fhlr kini")
    message = "Message_you_need_to_send"
    s.sendmail("medicalcenterpqr@gmail.com", dest, message)
    s.quit()