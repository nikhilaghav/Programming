import multiprocessing
import time
import os

def CountEven(No):
    Count = 0
    
    for i in range(2, No + 1, 2):
        Count = Count + 1

    print("Process ID:",os.getpid())
    print("Input number:",No)
    print("Even number count:",Count)

    print()

def main():
    Data = [1000000,2000000,30000000,4000000]

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()
    
    pobj.map(CountEven,Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print(f"Time required is:{end_time - start_time:.4f}")


if __name__ == "__main__":
    main()    