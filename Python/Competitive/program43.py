Div = lambda  no: (no % 3 ==0 and no % 5 == 0) 

def main():
    Data = [15,10,3,30,45]
    
    FData = list(filter(Div,Data))

    print(FData)

if __name__ == "__main__":
    main()    