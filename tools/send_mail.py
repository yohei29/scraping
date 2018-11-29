import smtplib
from email.mime.text import MIMEText
from email.header import Header

msg = MIMEText('send mail')
msg['Subject'] = Header('subject', 'utf-8')
msg['From'] = 'me@emil.com'
msg['To'] = 'you@emil.com'

with smtplib.SMTP('localhost') as smtp:
    # sending mail by me
    smtp.send_message(msg)

with smtplib.SMTP_SSL('smtp,gmail.com') as smtp:
    # sending mail by gmail
    smtp.login('login name', 'password')
    smtp.send_message(msg)