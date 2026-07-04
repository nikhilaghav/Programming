Odd = lambda no : (no % 2 != 0)

def main():
    Data =[1,2,3,4,5]

    FData = list(filter(Odd,Data))

    print(FData)

if __name__ == "__main__":
    main()    