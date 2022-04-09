import smtplib
from socket import MsgFlag
server=smtplib.SMTP('smtp.gmail.com','587')

# connection starting with transport layer security.
server.starttls()

server.login('rk359979@gmail.com','type in your password😄') 
subject="send using python"
body="this mail is send using python"

msg="subject:{}\n\n\n.".format(subject,body)
maillist=["email1@gmail.com","email2@gmail.com"]
server.sendmail("rk359979@gmail.com",maillist,msg)
print("Send successfully...!!")
server.quit()