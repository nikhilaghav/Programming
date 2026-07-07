import threading

def EvenFactor(No):
    Sum = 0

    for i in range(2, (No + 1)//2 + 1,2):
        if(No % i == 0):
            Sum = Sum + i

    print("Sum of even factors is:",Sum)
        

def OddFactor(No):
    Sum = 0

    for i in range(1, No//2 + 1,2):
        if(No % i == 0):
            Sum = Sum + i

    print("Sum of odd factors is:",Sum)
    
def main():
    t1 = threading.Thread(target=EvenFactor, args =(18,))
    t2 = threading.Thread(target=OddFactor, args =(18,))

    t1.start()
    t2.start()
   
    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()    