def main():
    fname1 =input("Enter the existing file name:")
    fname2 =input("Enter the second file name:")

    fobj1 = open(fname1,"r")
    fobj2 = open(fname2,"w")

    data = fobj1.read()
    fobj2.write(data)

    fobj1.close()
    fobj2.close()

    print("File copied succesfuly")

if __name__ == "__main__":
    main()    