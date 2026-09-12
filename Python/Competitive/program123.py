import schedule
import time

def fun():
    print("start your weekly goals")

def gun():
    print("Review your weekly progress")

def sun():    
    print("weekly work completed")

def main():

    schedule.every().monday.at("09:00").do(fun)
    schedule.every().wednesday.at("17:00").do(gun)
    schedule.every().friday.at("18:00").do(sun)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()    