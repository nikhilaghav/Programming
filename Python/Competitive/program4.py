def Cube(No):
    value1 = No * No * No
    return value1
    
def main():
    value = int(input("Enter number:"))
    
    Ret = Cube(value)

    print(Ret)

if __name__ == "__main__":
    main()    