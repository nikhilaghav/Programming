def Arithmetic(No1,No2):
    add = No1 + No2
    Mult = No1 * No2
    Div = No1 // No2
    Sub = No1 - No2

    return add,Mult,Div,Sub

def main():
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))

    Ret1,Ret2,Ret3,Ret4 = Arithmetic(num1,num2)

    print("Addition is:",Ret1)
    print("Multiplication is:",Ret2)
    print("Divison is:",Ret3)
    print("Subtraction is:",Ret4)

if __name__ =="__main__":
    main()