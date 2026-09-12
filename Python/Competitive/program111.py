import schedule
import time

def func():
    print("Jay Ganesh...")

def main():
    print("Automation script started...")
    schedule.every(2).seconds.do(func)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()    
