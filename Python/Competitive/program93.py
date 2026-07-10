import multiprocessing
import time
import os

def Factorial(No):
    Mult = 1
    
    for i in range(1, No + 1, 1):
        Mult = Mult * i

    print("Process ID:",os.getpid())
    print("Input number:",No)
    print("Factorial:",Mult)

    print()

def main():
    Data = [10,15,20,25]

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()
    
    pobj.map(Factorial,Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print(f"Time required is:{end_time - start_time:.4f}")


if __name__ == "__main__":
    main()    