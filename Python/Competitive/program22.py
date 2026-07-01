def AreaCircle(radius):
    Area = 3.14 * radius * radius
    return Area
    
def main():
    num = float(input("Enter radius:"))

    Ret = AreaCircle(num)

    print("Area is:",Ret)

if __name__ =="__main__":
    main()