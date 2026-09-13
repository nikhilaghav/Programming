import schedule
import time
import psutil
import sys

def ProcInfo(proc_name):

    fobj = open("Logfile.txt","a")

    found = False

    for proc in psutil.process_iter(["pid","name","username","status"]):
        if(proc.info["name"] == proc_name):
      
            fobj.write(f"Process Info: {proc.info}\n")
            found = True

    if found == False:
        print("Process is not running")    
            
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