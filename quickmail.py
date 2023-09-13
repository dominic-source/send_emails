import smtplib
import os
from time import sleep
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def mailSender(sub= None, body=None, addr="smtp.gmail.com", pas=None, 
               sen=None, rec=None, port=465):
    if (sen is None or rec is None):
        return
    x = 0
    # load environmental variables
    load_dotenv()

    # get the environmental variable which has the password or use argument password
    if (pas is None):
        pas = os.getenv("GTP")

    # Prepare the message
    message = MIMEMultipart()
    message['From'] = sen
    message['To'] = rec
    if (not sub):
        message['Subject'] = "Practising risky email communication"
    else:
        message["Subject"] = sub
    if (not body):
        body = "There is chinonso morba, a software engineer from alx."
        body += " Software engineering is good, but also has some disadvantage."
    message.attach(MIMEText(body, "plain"))


    while (x < 7):
        # loop 7 times until mail is sent the mail
        
        try:
            # create the server
            server = smtplib.SMTP_SSL(addr, port)
            server.login(sen, pas)
            server.sendmail(sen, rec, message.as_string())
        except Exception as e:
            print(f"error:{str(e)}")
            print("Please wait, retrying ...")
            sleep(2)
        else:
            print("mail sent!")
            if (server):
                server.quit()
            break
        finally:
            print("I am working hard 😎")
        x += 1

# test me
mailSender(sen="chinonsodomnic@gmail.com", rec="dominicmorba@gmail.com", pas=None)