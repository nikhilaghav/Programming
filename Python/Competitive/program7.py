def SumNatural(No):
    Sum = 0
    for i in range(1,No + 1):
        Sum = Sum + i
    return Sum    

def main():
    value = int(input("Enter number:"))

    Ret =SumNatural(value)

    print("Sum is:",Ret)

if __name__ == "__main__":
    main()    