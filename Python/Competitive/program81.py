import threading

def ChkPrime(No):
    if(No <= 1 ):
        return False
    for i in range(2, No//2 + 1 ):
        if(No % i == 0):
            return False
    
    return True
    
def DisplayPrime(Data):
    print("Prime numbers are:")
    for no in Data:
        if ChkPrime(no):
            print(no)

def DisplayNonPrime(Data):
    print("Non Prime numbers are:")
    for no in Data:
        if ChkPrime(no) == False:
            print(no)

def NonPrime(Arr):
   
    for i in range(50,0,-1):
        print(i)   
    
def main():

    Arr = [1,2,3,4,5,6,7,8]
    
    t1 = threading.Thread(target=DisplayPrime, args =(Arr,))
    t2 = threading.Thread(target=DisplayNonPrime, args =(Arr,))
  
    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()    