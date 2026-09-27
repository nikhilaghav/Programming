CheckEven = lambda No:(No % 2 == 0)

Increment = lambda No: No + 1

Addition = lambda No1, No2: No1 + No2

def FilterX(Task,Elements):
    Result = []

    for no in Elements:
        Ret = Task(no)  #CheckEven(no)

        if(Ret == True):
            Result.append(no)

    return Result            

def MapX(Task,Elements):
    Result = []

    for no in Elements:
        Ret = Task(no)  #Increment(no)
        Result.append(Ret)

    return Result  

def ReduceX(Task,Elements):
    Sum = 0
    for no in Elements:
        Sum = Task(Sum,no)

    return Sum    

def main():
    Data = [13,12,8,10,11,20]
    
    print("Input data is:",Data)

    FData = list(FilterX(CheckEven, Data))

    print("Data after filter:",FData)

    MData = list(MapX(Increment,FData))

    print("Data after map:",MData)

    RData = ReduceX(Addition, MData)

    print("Data after reduce :",RData)

if __name__ == "__main__":
    main()    