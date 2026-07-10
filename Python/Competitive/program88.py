import os
import multiprocessing
import time

def SumFive(No):
    print(f"Process is running with PID:{os.getpid()} and parent PID:{os.getppid()}")
    
    Sum = 0

    for i in range(1 , No + 1):
        Sum = Sum + i**

    return Sum    

def main():
    print("Main Process is running with PID:",os.getpid())

    Arr =[1000000,2000000,3000000,4000000]
    Data=[]

    start_time = time.perf_counter()

    pobj= multiprocessing.Pool()

    Data = pobj.map(SumFive,Arr)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print("Result is:")
    print(Data)
    print(f"Time required is:{end_time - start_time:.4f}")

if __name__ == "__main__":
    main()    