import schedule
import datetime
import time

def func():
    print("coding kar...")

def main():
    schedule.every(30).minutes.do(func)

    while True:
        schedule.run_pending()
        time.sleep(1)        

if __name__ == "__main__":
    main()