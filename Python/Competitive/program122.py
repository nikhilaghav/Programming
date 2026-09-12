import schedule
import time
import os

def CountFiles(Directoryname):
    TotalFiles = 0

    for Foldername, subfolder,Filename in os.walk(Directoryname):
        TotalFiles = TotalFiles + len(Filename)

    fobj = open("DirectoryCountLog.txt","w")

    fobj.write("Directory name:"+Directoryname+"\n")
    fobj.write(f"number of files:{TotalFiles}\n")
    fobj.write(f"date and time:{time.strftime('%Y-%m-%d %H:%M:%S')}\n") 
    fobj.write("\n")

    fobj.close()   

def main():
    dname = input("Enter directory name:")

    schedule.every(5).minutes.do(CountFiles,dname)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()    