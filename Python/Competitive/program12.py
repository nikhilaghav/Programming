def CountDigits(No):
    count = 0
    
    while(No != 0):
        Digit = No % 10
        count= count + 1
        No = int(No / 10)
    return count    

def main():
    value = int(input("enter number:"))

    Ret = CountDigits(value)

    print("Number of digits are:",Ret)


if __name__ == "__main__":
    main()        