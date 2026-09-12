import schedule
import datetime
import time

def Task():
    fobj = open("Marvellous.txt", "a")

    current = datetime.datetime.now()

    fobj.write("Task executed at: ")
    fobj.write(current.strftime("%d-%m-%Y %I:%M:%S %p"))
    fobj.write("\n")

    fobj.close()


def main():
    print("Automation script started...")

    schedule.every(5).minutes.do(Task)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
