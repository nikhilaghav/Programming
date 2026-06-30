def square(No):
    value1 = No * No
    return value1
    
def main():
    print("Enter number:")
    value = int(input())

    Ret = square(value)

    print(Ret)

if __name__ == "__main__":
    main()    