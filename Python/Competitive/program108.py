import sys

def main():
    if(len(sys.argv) == 2):
        fobj =open(sys.argv[1], "r")
        fobj2 = open("Demo.txt", "w")

        fobj2.write(fobj.read())

        fobj.close()
        fobj2.close()

        print("File copied succesfuly")

    else:
     print("Invalid no. of arguments:")    
    
if __name__ == "__main__":
    main()