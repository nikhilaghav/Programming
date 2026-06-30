def Factorial(No):
    Mult = 1
    for i in range(No,0,-1):
        Mult = Mult * i
    return Mult    

def main():
   value = int(input("Enter number:"))

   Ret = Factorial(value)

   print("Factorial is:",Ret)

if __name__ == "__main__":
    main()    