from functools import reduce

def ChkPrime(No):
    if(No <= 1):
        return False
    for i in range(2,No//2 + 1):
        if( No % i == 0):
            return False

    return True

def Mult(No):
    return No * 2

def Maximum(No1,No2):
    if(No1 > No2):
        return No1
    else :
        return No2

def main():
    Arr = list()

    value = int(input("How many numbers to store:"))

    print("Enter numbers:")

    for i in range(value):
        No = int(input())
        Arr.append(No) 

    FData = list(filter(ChkPrime,Arr))

    print("Data after filter is:",FData)

    MData = list(map(Mult,FData))

    print("Data after map is:",MData)

    if(len(MData) > 0):

       RData = reduce(Maximum,MData)    

       print("Data after reduce is:",RData)

    else:
        print("No elements to reduce")   
    
if __name__ == "__main__":
    main()    