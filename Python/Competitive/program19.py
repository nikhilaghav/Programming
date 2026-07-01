def Sequence(No):
    for i in range(1,No + 1):
        print(i)
    
def main():
    num = int(input("Enter number:"))

    Sequence(num)

if __name__ =="__main__":
    main()