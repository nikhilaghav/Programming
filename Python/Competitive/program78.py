import threading

def EvenList(Arr):
    Sum = 0

    for no in Arr:
        if no % 2 == 0:
            Sum = Sum + no

    print("Sum of even elements is:",Sum)
        

def OddList(Arr):
    Sum = 0

    for no in Arr:
        if no % 2 != 0:
            Sum = Sum + no
            
    print("Sum of odd elements is:",Sum)
        
    
def main():
    Data = (1,2,3,4,5,6)
    t1 = threading.Thread(target=EvenList, args =(Data,))
    t2 = threading.Thread(target=OddList, args =(Data,))

    t1.start()
    t2.start()
   
    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()    