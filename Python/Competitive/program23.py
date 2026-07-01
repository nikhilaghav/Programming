def CheckPerfect(No):
    Sum = 0
    for i in range(1,No//2 + 1):
        if(No % i == 0):
            Sum = Sum + i
    return Sum == No        
    
def main():
    num = int(input("Enter number:"))

    Ret = CheckPerfect(num)

    if Ret:
        print("It is perfect")
    else:
        print("It is not perfect")    

if __name__ =="__main__":
    main()