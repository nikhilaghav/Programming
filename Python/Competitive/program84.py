import threading

Sum = 0
Mult = 1

def SumElements(Arr):
    global Sum
    for no in Arr:
        Sum = Sum + no

def MultElements(Arr):
    global Mult
    for no in Arr:
        Mult = Mult * no
  
def main():

    Data = [1,2,3,4,5]

    t1 = threading.Thread(target=SumElements, args = (Data,))
    t2 = threading.Thread(target=MultElements , args =(Data,))
   
    t1.start()
    t2.start()
  
    t1.join()
    t2.join()

    print("Sum is:",Sum)
    print("Multiplication  is:",Mult)

if __name__ == "__main__":
    main()    