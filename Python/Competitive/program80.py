import threading

def Display():
    print(f"current Thread name is {threading.current_thread().name}")

    for i in range(1,51):
        print(i)
 
def DisplayRev():
    print(f"current Thread name is {threading.current_thread().name}")

    for i in range(50,0,-1):
        print(i)   
    
def main():
    
    t1 = threading.Thread(target=Display, args =(), name = "Thread1")
    t2 = threading.Thread(target=DisplayRev, args =(), name = "Thread2")
  
    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()    