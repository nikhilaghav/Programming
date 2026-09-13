import schedule
import os
import time
import shutil

def CopyFile(source, dest):
    for Foldername, Subfolder,Filename in os.walk(source):
        for fname in Filename:
            if fname.endswith(".txt"):
                source_path = os.path.join(Foldername,fname)
                dest_path = os.path.join(dest,fname)

                try:
                    shutil.copy(source_path,dest_path)
                    print(fname,"copied succesfuly")

                except Exception :
                    print("file cannot be copied")
                    continue

                fobj = open("LogFile.txt","a")
                fobj.write(fname + "\n")
                fobj.close()

def main():
    source = input("Enter source directory:")
    dest = input("enter destination directory:")

    if(os.path.isdir(source)):
        if(os.path.isdir(dest)):
            schedule.every(15).seconds.do(CopyFile,source,dest)

            while True:
                schedule.run_pending()
                time.sleep(1)
    else:
        print("invalid parameters")
if __name__ == "__main__":
    main()