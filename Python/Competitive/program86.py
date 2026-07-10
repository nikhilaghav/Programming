import os
import multiprocessing
import time

def Factorial(No):
    print(f"Process is running with PID:{os.getpid()} and parent PID:{os.getppid()}")
    
    Mult = 1

    for i in range(1 , No + 1):
        Mult = Mult * i

    return Mult   

def main():
    print("Main Process is running with PID:",os.getpid())

    Arr =[10,15,20,25]
    Data=[]

    start_time = time.perf_counter()

    pobj= multiprocessing.Pool()

    Data = pobj.map(Factorial,Arr)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print("Result is:")
    print(Data)
    print(f"Time required is:{end_time - start_time:.4f}")

if __name__ == "__main__":
    main()    