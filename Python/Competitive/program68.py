def Minimum(Data):
    min = Data[0]

    for i in range(len(Data)):
        if(Data[i] < min):
            min = Data[i]
    return min

def main():
    Arr = list()

    value = int(input("How many numbers u want to store:"))

    print("Enter elements")

    for i in range(value ):
        No = int(input())
        Arr.append(No)

    Ret = Minimum(Arr)

    print("Minimum value:",Ret)    


if __name__ == "__main__":
    main()

