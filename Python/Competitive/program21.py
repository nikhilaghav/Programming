def AreaRect(length,width):
    Area = length * width
    return Area
    
def main():
    num1 = float(input("Enter length:"))
    num2 = float(input("Enter width:"))

    Ret = AreaRect(num1,num2)

    print("Area is:",Ret)

if __name__ =="__main__":
    main()