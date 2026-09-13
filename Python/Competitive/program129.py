import schedule
import time
import psutil

def ProcInfo():

    fobj = open("Logfile.txt","a")
    
    for proc in psutil.process_iter():
      
        fobj.write(f"Process name: {proc.name()}\n")
        fobj.write(f"PID: {proc.pid}\n")
        fobj.write(f"Username: {proc.username()}\n")

    fobj.close()    

def main():
    schedule.every(1).minutes.do(ProcInfo)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()    