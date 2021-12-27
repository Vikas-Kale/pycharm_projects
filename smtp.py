# import smtplib
# connection=smtplib.SMTP("smtp.gmail.com",587)
# connection.ehlo()
# connection.starttls()
# connection.login("kalevikas7798@gmail.com",'9422119274')
# connection.sendmail("kalevikas7798@gmail.com","vkale4938@gmail.com","Subject: This is Test Mail from python \n\n Hii, I am SMTP server from python library.")
# connection.quit()
import os
import smtplib

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.ehlo()
connection.starttls()
connection.login((os.environ.get("mailuser")), (os.environ.get("mailpass")))
connection.sendmail("kalevikas7798@gmail.com", "vkale4938@gmail.com",
                    "Subject:Test mail-2 from Pycharm \n\n Hii, I am Vikas Kale! I have completed my BE in Electrical Engineering. But now I want to be a software developer. \n Thanks & Regard's \n Vikas ")
connection.quit()
