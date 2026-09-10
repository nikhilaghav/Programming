def main():
    fname =input("Enter the file name:")
    
    fobj = open(fname,"r")

    data = fobj.read()

    print(data) 

if __name__ == "__main__":
    main()    