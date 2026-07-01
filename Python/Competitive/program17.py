def Factors(No):
    for i in range(1,No+1):
        if(No % i == 0):
            print(i)

def main():
    num = int(input("enter number:"))
    
    Ret = Factors(num)
   
if __name__ == "__main__":
    main()        