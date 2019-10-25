import smtplib 

def MailSent(gmailaddress,gmailpassword,mailto,msg):
    mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
    mailServer.starttls()
    mailServer.login(gmailaddress , gmailpassword)
    mailServer.sendmail(gmailaddress, mailto ,msg)
    mailServer.quit()


