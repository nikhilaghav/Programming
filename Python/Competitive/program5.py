def Division(value):
    if(value % 3 == 0 and value % 5 == 0):
        return True
    else:
        return False
    
def main():
    value = int(input("Enter the number:"))

    Ret = Division(value)
    if(Ret == True):
        print("Number is divisible by 3 & 5")
    else:
        print("Number is not divisible by 3 & 5")    

if __name__ == "__main__":
    main()    