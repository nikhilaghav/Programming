def ReverseDigits(No):
        Rev = 0
        while(No != 0):
            Digit = No % 10
            Rev = (Rev * 10) + Digit
            No = No // 10

        print(Rev)

def main():
    value = int(input("enter number:"))

    ReverseDigits(value)

if __name__ == "__main__":
    main()        