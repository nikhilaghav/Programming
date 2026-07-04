from  functools import reduce

Max = lambda no1, no2 : no1 if (no1 > no2) else no2 

def main():
    Data =[1,2,3,4,5]

    RData = reduce(Max,Data)

    print(RData)

if __name__ == "__main__":
    main()    