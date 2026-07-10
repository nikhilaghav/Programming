import os
import multiprocessing
import time

def CheckPrime(No):
    if (No <= 1):
        return False
    
    for i in range(2,No//2 + 1):
        if No % i == 0:
            return False

    return True

def CountPrime(No):
    count =0

    print(f"Process is running with PID:{os.getpid()} and parent PID:{os.getppid()}")
    
    for i in range(1,No + 1):
        if CheckPrime(i):
            count= count + 1

    return count                

def main():
    print("Main Process is running with PID:",os.getpid())

    Arr =[10,15,20,25]
    Data=[]

    start_time = time.perf_counter()

    pobj= multiprocessing.Pool()

    Data = pobj.map(CountPrime,Arr)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print("Result is:")
    print(Data)
    print(f"Time required is:{end_time - start_time:.4f}")

if __name__ == "__main__":
    main()    