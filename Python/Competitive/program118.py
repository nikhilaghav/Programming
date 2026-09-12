import schedule
import time

def DisplayMessage(message):
    print(message)
    
def main():
    message = input("Enter message:")
    stime = int(input("enter time interval in seconds:")) 

    if(stime > 0):
      schedule.every(stime).seconds.do(DisplayMessage,message)

      while True:
        schedule.run_pending()
        time.sleep(1)
    else:
       print("Please enter valid time")
if __name__ == "__main__":
    main()