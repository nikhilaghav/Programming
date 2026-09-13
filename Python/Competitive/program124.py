import schedule
import time

def CreateFile():
    timestamp = time.strftime("%Y_%m_%d_%H_%M_%S")

    filename = "File_%s.txt"%timestamp

    fobj = open(filename,"w")

    fobj.write("Filename:"+filename+"\n")
    fobj.write(f"creation date:{time.strftime("%Y-%m-%d")}\n")
    fobj.write(f"creation time:{time.strftime("%H:%M:%S")}\n")

    fobj.close()

def main():
    schedule.every(1).minutes.do(CreateFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()    