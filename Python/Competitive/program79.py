import threading

def Small(Arr):
    print(f"current Thread name is {threading.current_thread().name} and id is {threading.get_ident()}")
    for i in range(0,len(Arr)):
        if(Arr[i] >= 'a' and Arr[i] <= 'z'):
            print(Arr[i])

def Capital(Arr):
    print(f"current Thread name is {threading.current_thread().name} and id is {threading.get_ident()}")
    
    for i in range(0,len(Arr)):
        if(Arr[i] >= 'A' and Arr[i] <= 'Z'):
            print(Arr[i])

def Digits(Arr):
    print(f"current Thread name is {threading.current_thread().name} and id is {threading.get_ident()}")
    
    for i in range(0,len(Arr)):
        if(Arr[i] >= '0' and Arr[i] <= '9'):
            print(Arr[i])
   
def main():
    Data = "MArvellous2511"
    t1 = threading.Thread(target=Small, args =(Data,), name ="Small")
    t2 = threading.Thread(target=Capital, args =(Data,) , name= "Capital")
    t3 = threading.Thread(target=Digits, args =(Data,), name = "Digits")

    t1.start()
    t2.start()
    t3.start()
   
    t1.join()
    t2.join()
    t3.join()

    print("Exit from main")

if __name__ == "__main__":
    main()    