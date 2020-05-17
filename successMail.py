import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "arundsnewjenkins@gmail.com"
receiver_email = "arundsnew@gmail.com"
password = "!1DockerJenkins*"
message = """\
Subject: Successfully tested

Code ready to deploy in production environment."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    
except:
    print("Error occured, mail not sent")
else:
    print("Mail successfully sent")