import schedule
import os
import time

def MonitorFile(filepath):
    fobj = open("FileSizeLog","a")

    fobj.write(f"file path:{filepath}\n")
    fobj.write(f"file size:{os.path.getsize(filepath)} bytes \n")
    fobj.write(f"creation on:{time.strftime("%Y-%m-%d %H:%M:%S")}\n")
    fobj.write("-------------------------------------------------")

    fobj.close()

def main():
    filepath = input("Enter file path:")

    if(os.path.exists(filepath)):
        schedule.every(30).seconds.do(MonitorFile,filepath)

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("file does not exist")
if __name__ == "__main__":
    main()