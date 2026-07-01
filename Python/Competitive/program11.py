def CheckPrime(No):
    flag = True

    if(No == 0 or No == 1 ):
       return False

    for i in range(2,int(No/2 + 1)):
        if(No % i == 0):
           flag = False
           break
    
    return flag   

def main():
   value = int(input("Enter number:"))

   Ret = CheckPrime(value)

   if(Ret == True):
       print("It is prime")
   else:
    print("It is not prime")   
           
if __name__ == "__main__":
    main()  