import multiprocessing
import time
import os

def SumOdd(No):

    Sum = 0

    for i in range(1, No + 1, 2):
        Sum = Sum + i

    print("Process ID:",os.getpid())
    print("Input number:",No)
    print("Sum of odd numbers:",Sum)

    print()

def main():
    Data = [1000000,2000000,30000000,4000000]

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()
    
    pobj.map(SumOdd,Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print(f"Time required is:{end_time - start_time:.4f}")


if __name__ == "__main__":
    main()    