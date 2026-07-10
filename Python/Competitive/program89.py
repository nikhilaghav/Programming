import os
import multiprocessing
import time

def SumEven(No):
    Sum = 0
    for i in range(2, No+1, 2):
        Sum = Sum + i

    return (os.getpid(),No,Sum) 
   
def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumEven, Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    for no in Result:
        print("Process ID:",no[0])
        print("Input Number:",no[1])
        print("Sum of even Numbers:",no[2])


    print(f"Time required is : {end_time - start_time:.4f}")

if __name__ == "__main__":
    main()

""""
import os
import multiprocessing
import time

def SumEven(No):
    Sum = 0
    for i in range(2, No+1, 2):
        Sum = Sum + i

    print("Process ID:",os.getpid())
    print("input number:",No)
    print("Sum of even numbers:",Sum)

   
def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    pobj.map(SumEven, Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()


    print(f"Time required is : {end_time - start_time:.4f}")

if __name__ == "__main__":
    main()


"""