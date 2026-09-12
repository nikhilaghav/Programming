import schedule
import time

def CreateLog():

    timestamp = time.strftime("%Y_%m_%d_%I_%M_%S  %p")

    filename = "Marvellouslog_%s.txt"%timestamp

    fobj = open(filename,"w")

    fobj.write("Log file created succesfuly.\n")
    fobj.write(f"creation time:{timestamp}")

    fobj.close()

def main():
    schedule.every(5).seconds.do(CreateLog)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()