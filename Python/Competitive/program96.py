class Arithmetic:
    PI = 3.14

    def __init__(self):
        self.value1 = 0
        self.value2= 0
    
    def Accept(self):
        self.value1 = int(input("enter first number:"))
        self.value2 = int(input("enter second number:"))


    def Addition(self):
        return self.value1 + self.value2     

    def Subtraction(self):
        return self.value1 - self.value2

    def Multiplication(self):
        return self.value1 * self.value2

    def Division(self):
        if(self.value2 == 0):
            print("Division by zero not possible")
            return None
        else:
            return self.value1 / self.value2      

def main():
    obj1 = Arithmetic()
    obj2 = Arithmetic()

    obj1.Accept()
    
    Ret = obj1.Addition()
    print("Addition is:",Ret)

    Ret = obj1.Subtraction()
    print("Subtraction is:",Ret)

    Ret = obj1.Multiplication()
    print("multiplication is:",Ret)
    
    Ret = obj1.Division()
    print("Division is:",Ret)

    print("")

    obj2.Accept()
    
    Ret = obj2.Addition()
    print("Addition is:",Ret)

    Ret = obj2.Subtraction()
    print("Subtraction is:",Ret)
    
    Ret = obj2.Multiplication()
    print("multiplication is:",Ret)
    
    Ret = obj2.Division()
    print("Division is:",Ret)

if __name__ == "__main__":
    main()    