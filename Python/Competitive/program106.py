import os

def main():
    fname = input("Enter file name:")

    ret = os.path.isfile(fname)

    if ret ==True:
        print("File exists")
    else:
        print("File does not exist")    

if __name__ == "__main__":
    main()