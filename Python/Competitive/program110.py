def main():
    fname = input("Enter file name:")
    str = input("Enter the string:")

    fobj = open(fname,"r")

    data = fobj.readlines()

    count = 0

    for line in data:
        words = line.split()
        for s in words:
            if s == str:
                count = count + 1

    print("Frequncy is:",count)

if __name__ == "__main__":
    main()