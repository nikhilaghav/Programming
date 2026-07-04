CountEven = lambda no : (no % 2 == 0)

def main():
    Data = [2,3,4,5,6,7,8]

    FData = list(filter(CountEven,Data))

    print(len(FData))


if __name__ =="__main__":
    main()    