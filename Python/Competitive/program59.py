def FactAdd(No):
    Sum = 0;

    for i in range(1, int((No + 1)/2 + 1)):
        if( No % i == 0 ):
            Sum = Sum + i

    return Sum;

def main():
    value = int(input("enter number:"))

    Ret= FactAdd(value)

    print(" Addition of Factors is:",Ret);

if __name__ =="__main__":
    main()    