import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "chinonsodomnic@gmail.com"
receiver_email = "dominicmorba@gmail.con"
smtp_server = "smtp.gmail.com"
smtp_port = 465
smtp_username = "Chinonso Morba"
smtp_password = ""

# Create the email message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subjest'] = "Testing cutting edge tech"

# Body of the email
body = "This is me testing the smtp server and improving some of my skills"
message.attach(MIMEText(body, 'plain'))

server = None
# setup the server and send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)

    print("Email sent successfully!")
except Exception as e:
    print(f'error: {str(e)}')
finally:
    if server:
        server.quit()
