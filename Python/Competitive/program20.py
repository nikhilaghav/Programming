def RevSequence(No):
    for i in range(No,0,-1):
        print(i)
    
def main():
    num = int(input("Enter number:"))

    RevSequence(num)

if __name__ =="__main__":
    main()