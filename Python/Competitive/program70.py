import MarvellousNum

def ListPrime(Data):
    Sum = 0

    for no in Data:
        if MarvellousNum.ChkPrime(no) :
            Sum = Sum + no

    return Sum

def main():
    Arr = list()

    value1 = int(input("How many numbers u want to store:"))

    print("enter elements:")

    for i in range(value1 ):
        No = int(input())
        Arr.append(No)

    Ret = ListPrime(Arr)

    print("Addition is:",Ret)

if __name__ == "__main__":
    main()

