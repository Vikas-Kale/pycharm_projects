# import smtplib
#
# connection = smtplib.SMTP("smtp.gmail.com", 587)
# connection.ehlo()
# connection.starttls()
# connection.login("kalevikas7798@gmail.com", "9422119274")
# connection.sendmail("kalevikas7798@gmail.com", "vkale4938@gmail.com",
#                     "Subject: For Testng Purpose!\n\n Hii I am SMTP server from Pycharm! \n \n Thank's\n Vikas Kale")
# connection.quit()

# import smtplib
#
# print(dir(smtplib))
# help(smtplib.email)

import smtplib

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.ehlo()
connection.starttls()
connection.login("kalevikas7798@gmail.com","9422119274")
connection.sendmail("kalevikas7798@gmail.com", "vkale4938@gmail.com",
                                               "Subject :Hidden pass!\n\n Hello,\n\t In this mail we hide mail pass "
                                               "for security purpose. "
                                               "We add our mail id and password in environment variables settings."
                                               "\nTo use this we need to import os module.\n\nThank's \nVikas")
connection.quit()
