square = lambda no : no * no

def main():
    Data =[1,2,3,4,5]

    MData = list(map(square,Data))

    print(MData)

if __name__ == "__main__":
    main()    