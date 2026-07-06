def Add(Arr):
    Sum = 0

    for no in Arr:
        Sum = Sum + no
    
    return Sum

def main():
    Data = list()

    value = int(input("How many numbers u want to store:"))

    print("Enter number:")

    for i in range(1, value + 1):
        No =int(input())
        Data.append(No)

    Ret =Add(Data)    

    print("Sum is:",Ret)    

if __name__ == "__main__":
    main()    