import schedule
import time
import psutil
import sys
import os

def ProcInfo(dirname):

    LogFileName = "LogFile.txt"

    file_path = os.path.join(dirname,LogFileName)

    fobj = open(file_path,"a")

    for proc in psutil.process_iter(["pid","name","username","status"]):
    
            fobj.write(f"Process name: {proc.name()}\n")
            fobj.write(f"PID: {proc.pid}\n")
            fobj.write(f"username: {proc.username()}\n")
            fobj.write(f"status: {proc.status()}\n")
            
    fobj.close()    

def main():
    if (len(sys.argv)==2):
    
        schedule.every(30).seconds.do(ProcInfo,sys.argv[1])

        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print("invalid no. pf paramaeters")        

if __name__ == "__main__":
    main()    