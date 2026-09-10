def main():
    fname = input("Enter file name:")

    fobj = open(fname,"r")

    print(fobj.read())

    fobj.close()

if __name__ == "__main__":
    main()