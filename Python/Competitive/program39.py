from  functools import reduce

Addition = lambda no1, no2 : no1 + no2 

def main():
    Data =[1,2,3,4,5]

    RData = reduce(Addition,Data)

    print(RData)

if __name__ == "__main__":
    main()    