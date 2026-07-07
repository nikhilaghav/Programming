from functools import reduce

filterx = lambda no: no % 2 == 0
Mapx =lambda no: no ** 2
Reducex = lambda no1,no2: no1 + no2

def main():
    Arr = list()

    value = int(input("How many numbers to store:"))

    print("Enter numbers:")

    for i in range(value):
        No = int(input())
        Arr.append(No) 

    FData =  list(filter(filterx,Arr))   

    print("Data after filter:",FData) 

    MData = list(map(Mapx,FData))

    print("Data after map:",MData)

    if(len(MData) > 0):
      RData = reduce(Reducex,MData)

      print("Data after reduce:",RData)

    else:
        print("No elememts to reduce")  

if __name__ == "__main__":
    main()    