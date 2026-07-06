def ChkPrime(No):
    if(No <= 1 ):
        return False
    
    for i in range(2, int(No/2 + 1)):
        if(No % i == 0):
            return False

    return True    

def main():
    value = int(input("enter number:"))

    Ret= ChkPrime(value)

    if Ret:
        print("Number is prime")
    else:
        print("Number is not prime")    

if __name__ =="__main__":
    main()    