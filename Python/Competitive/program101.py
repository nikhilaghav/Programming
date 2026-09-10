def main():
    fname =input("Enter the file name:")

    fobj = open(fname,"r")

    print(len(fobj.readlines()))

    fobj.close()

if __name__ =="__main__":
    main()

# second method is as below

"""
def CountLines(FileName):
    Count = 0

    fobj = open(FileName, "r")

    for line in fobj:
        Count = Count + 1

    fobj.close()

    return Count


def main():
    FileName = input("Enter file name: ")

    Ret = CountLines(FileName)

    print("Number of lines in file:", Ret)


if __name__ == "__main__":
    main()
"""


