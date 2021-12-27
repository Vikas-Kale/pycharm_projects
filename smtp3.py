import smtplib

conn = smtplib.SMTP("smtp.gmail.com", 587)
conn.ehlo()
conn.starttls()
conn.login("kalevikas7798@gmail.com", "9422119274")
conn.sendmail("kalevikas7798@gmail.com", "vkale4938@gmail.com",
              "Subject : Mail from smtplib. \n\n Hii Vikas,\n\t I am from python smtplib library.\nYou are very intellegent"
              "never give up one day you will achieve your goal.For this you have to strugle today.\n\n"
              "Thanks & regards\n"
              "Python")
conn.quit()