def CheckPalindrome(No):
    Rev = 0
    No1 = No

    while(No != 0):
        Digit = No % 10
        Rev = Rev * 10 + Digit
        No = int(No / 10)

    return Rev == No1    


def main():
    value = int(input("Enter Number:"))

    Ret = CheckPalindrome(value)

    if Ret:
        print("It is palnidrome")
    else:
        print("It is not palindrome")    


if __name__ == "__main__":
    main()        

