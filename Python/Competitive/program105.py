def ChkWord(fname,word):
    fobj = open(fname,"r")
    
    data = fobj.readlines()
    
    for line in data:
        line2=line.split()
        for w in line2:
            if word == w:
                fobj.close()
                return True

    fobj.close()
    return False

def main():
    fname=input("Enter the file name:")
    word = input("enter the word:")

    ret = ChkWord(fname,word)

    if ret == True:
        print("word is present")
    else:
        print("word is not present")    
    
if __name__ == "__main__":
    main()    