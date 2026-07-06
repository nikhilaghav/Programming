def CountDigit(No):
    Count = 0

    while(No != 0):
        Digit = No % 10
        Count = Count + 1
        No = No // 10 
    return Count    

def main():
    value = int(input("enter number:"))

    Ret =CountDigit(value)

    print("Number of digits are:",Ret)

if __name__ =="__main__":
    main()    