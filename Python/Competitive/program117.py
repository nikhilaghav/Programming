import schedule
import time
import sys
import os
import shutil

def BackupFile(source, Destination):
    timestamp = time.strftime("%Y-%m-%d_%H_%M_%S")
         
    backup_filename = "backup_%s.txt"%timestamp
         
    backup_path = os.path.join(Destination,backup_filename)
         
    shutil.copy2(source,backup_path)
         
    fobj = open("backup_log.txt","a")
         
    fobj.write(f"Backup completed successfully at {timestamp}\n")
         
    fobj.close()
         
def main():
     if(len(sys.argv) == 2):
    
            if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
                print("This automation script is used to perform file backup")
                print("Please execute the scipt as ")
                print("python source_File_path destination_Directory_path")
                print("source and destination should be absolute path")

     elif(len(sys.argv) ==3):
                schedule.every().hour.do(BackupFile,sys.argv[1],sys.argv[2])
                
                while True:
                    schedule.run_pending()
                    time.sleep(1)    
           
     else:
        print("Invalid no. of arguments")
        print("please press --h for more information")

if __name__ == "__main__":
    main()