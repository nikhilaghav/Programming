def Display(No):
    for i in range(1,No + 1):
        for j in range(1,No + 1):
            if( i<j or i==j):
                print("* ", end = " ")
        
        print()    

def main():
    value = int(input("enter number:"))

    Display(value)

if __name__ =="__main__":
    main()    