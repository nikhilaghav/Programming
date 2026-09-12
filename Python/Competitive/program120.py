import schedule
import os
import time

def DirectoryScan():
    TotalFiles = 0
    Total_SubFolders = 0

    for Foldername, Subfolder, Filename in os.walk("Marvellous"):
        TotalFiles = TotalFiles + len(Filename)
        Total_SubFolders = Total_SubFolders + len(Subfolder)

    print("Directory scanned:Marvellous")
    print("Total files:",TotalFiles)
    print("Toatl subfolders:",Total_SubFolders)
    print(f"scan time {time.strftime("%Y-%m-%d %H:%M:%S")}")    

def main():
    schedule.every(1).minutes.do(DirectoryScan)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()