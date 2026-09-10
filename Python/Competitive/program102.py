def main():
    fname =input("Enter the file name:")
    
    fobj = open(fname,"r")

    data = fobj.readlines()

    count = 0

    for line in data:
        count = count + len(line.split())

    print(f"Total no. of words in {fname} is {count}")    

if __name__ == "__main__":
    main()    