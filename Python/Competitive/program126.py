import schedule
import os
import time

def DisplayFile(filename):

    try:
        fobj = open(filename,"r")

        data = fobj.read()

        print(data)

        fobj.close()

    except PermissionError:
        print("permission denied")

    except OSError:
        print("file cannot be opened")        

def main():
    filename = input("Enter file name:")

    if(os.path.exists(filename)):
        if(os.path.getsize(filename) == 0):
            print("file is empty")
            return

        schedule.every(1).minutes.do(DisplayFile,filename)

        while(True):
            schedule.run_pending()
            time.sleep(1)

    else:
        print("file does not exist")        
    
if __name__ == "__main__":
    main()