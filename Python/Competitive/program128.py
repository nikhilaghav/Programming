import schedule
import os
import time

def Delete_Empty_File(dir):
    for Foldername, Subfolder,Filename in os.walk(dir):
        for fname in Filename:
            os.path.join(Foldername,fname)
            if(os.path.getsize(fname) == 0):
                os.remove()
                fobj = open("Logfile.txt","a")

                fobj.write("Files deleted are:\n")
                fobj.write(fname +"\n")
                fobj.close()
       
def main():
    dir = input("Enter directory name:")

    schedule.every(1).minutes.do(Delete_Empty_File,dir)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()