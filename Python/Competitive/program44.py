from functools import reduce

mult = lambda no1,no2:no1*no2

def main():
    Data = [11,2,3,4,5]

    FData = reduce(mult,Data)

    print(FData)


if __name__ =="__main__":
    main()    