import schedule
import datetime
import time

def fun():
    print("Lunch Time!")

def gun():
    print("Wrap up work")   

def main():
    print("automation scrpit started...")
    schedule.every().day.at("13:00").do(fun)
    schedule.every().day.at("18:00").do(gun)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()