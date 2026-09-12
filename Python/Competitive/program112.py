import schedule
import datetime
import time

def func():
    print("current date and time:",datetime.datetime.now())

def main():
    schedule.every(1).minutes.do(func)

    while True:
        schedule.run_pending()
        time.sleep(1)        

if __name__ == "__main__":
    main()