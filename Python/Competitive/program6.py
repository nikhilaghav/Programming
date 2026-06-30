def Table(value):
    for i in range(1,11):
        print(i * value)
    
def main():
    value = int(input("Enter the number:"))

    Table(value)
    
if __name__ == "__main__":
    main()    