import threading

lock = threading.Lock()

count = 0

def Display():
    global count

    for i in range(0,1000):
        lock.acquire()
        count = count + 1
        lock.release()

def main():
    t1 = threading.Thread(target=Display)
    t2 = threading.Thread(target=Display)
    t3 = threading.Thread(target=Display)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print(count)

if __name__ == "__main__":
    main()    