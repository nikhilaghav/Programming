def Maximum(Arr):
    max = Arr[0]
    
    for i in range(len(Arr)):
        if(Arr[i] > max):
            max = Arr[i]

    return max;

def main():
    
    Data = list()

    value = int(input("How many numbers u want to store:"))

    print("Enter number:")

    for i in range(1, value + 1):
        No =int(input())
        Data.append(No)

    Ret =Maximum(Data)    

    print("Maximum number is:",Ret)    

if __name__ == "__main__":
    main()    