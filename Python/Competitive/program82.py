import threading

def Maximum(Data):
    Max = Data[0]

    for i in range(len(Data)):
        if(Data[i] > Max):
            Max = Data[i]

    print("Maximum elemnt is:",Max)

def Minimum(Data):
    Min = Data[0]

    for i in range(len(Data)):
        if(Data[i] < Min):
            Min = Data[i]

    print("Minimum elemnt is:",Min)

def main():
    Arr = list()

    value = int(input("How many numbers u want to store:"))

    print("Enter elements")
    
    for i in range(value ):
        No = int(input())
        Arr.append(No)

    t1 = threading.Thread(target=Maximum, args =(Arr,))
    t2 = threading.Thread(target=Minimum, args =(Arr,))
  
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()


if __name__ == "__main__":
    main()