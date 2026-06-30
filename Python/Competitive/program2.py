def chkGreater(No1,No2):
    if (No1 > No2):
        print(No1,"is greater ")
    elif(No2 > No1):
        print(No2,"is greater")
    else:
        print("Both are equal")        

def main():
    value1 = int(input("Enter first number:"))
    value2 = int(input("Enter second number:"))

    chkGreater(value1,value2)

if __name__ == "__main__":
    main()    