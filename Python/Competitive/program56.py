import Arithmetic

value1 = int(input("Enetr first number:"))
value2 = int(input("Enetr second number:"))

Ret = Arithmetic.Add(value1,value2)
print("Addition is:",Ret)

Ret = Arithmetic.Sub(value1,value2)
print("Subtraction is:",Ret)

Ret = Arithmetic.Mult(value1,value2)
print("multiplication is:",Ret)

Ret = Arithmetic.Div(value1,value2)
print("division is:",Ret)

