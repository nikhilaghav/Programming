def SumDigit(No):
    Sum = 0

    while(No != 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10 
    return Sum    

def main():
    value = int(input("enter number:"))

    Ret =SumDigit(value)

    print("Sum of digits are:",Ret)

if __name__ =="__main__":
    main()    