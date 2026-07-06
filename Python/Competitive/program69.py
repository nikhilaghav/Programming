def Search(Data,No):
    count = 0

    for i in range(len(Data)):
        if(No == Data[i]):
            count = count + 1
    return count

def main():
    Arr = list()

    value1 = int(input("How many numbers u want to store:"))

    print("enter elements:")

    for i in range(value1 ):
        No = int(input())
        Arr.append(No)

    value2 = int(input("enter element to search:"))
      
    Ret = Search(Arr,value2)

    print(f"Frequency of {value2} is:",Ret)

if __name__ == "__main__":
    main()

