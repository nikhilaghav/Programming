import schedule
import time
import psutil
import sys
import os

import smtplib
from email.message import EmailMessage

def send_mail(file_path,receiver_mail):

     fobj = open(file_path,"rb")
     data = fobj.read()
     fobj.close()

     msg = EmailMessage()

     sender_email = "nikhilaghav25@gmail.com"
     app_password = "xamx gxep srmx cpeb"

     msg["To"] = receiver_mail
     msg["From"] = "nikhilaaghav@gmail.com"
     msg["Subject"] =" sending logfile "

     msg.add_attachment(data, maintype = "text", subtype = "plain", filename = file_path)

     smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)
     smtp.login(sender_email, app_password)
     
     smtp.send_message(msg)
     
     smtp.quit()
     
     print("Log file sent successfully")
             
def ProcInfo(dirname,reciever_mail):

    LogFileName = "LogFile.txt"

    file_path = os.path.join(dirname,LogFileName)

    fobj = open(file_path,"a")

    for proc in psutil.process_iter(["pid","name","username","status"]):
    
            fobj.write(f"Process name: {proc.name()}\n")
            fobj.write(f"PID: {proc.pid}\n")
            fobj.write(f"username: {proc.username()}\n")
            fobj.write(f"status: {proc.status()}\n")
            
    fobj.close()  

    send_mail(file_path,reciever_mail)

def main():
    if (len(sys.argv)==3):
    
        schedule.every(1).minutes.do(ProcInfo,sys.argv[1],sys.argv[2])

        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print("invalid no. pf paramaeters")        

if __name__ == "__main__":
    main()    