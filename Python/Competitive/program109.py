import sys
import hashlib

def CalculateChkSum(fname):
    fobj = open(fname, "r+b")

    buffer = fobj.read(1024)

    hobj = hashlib.md5()

    while len(buffer) > 0:
       hobj.update(buffer)
       buffer = fobj.read(1024)
       
    fobj.close()

    return hobj.hexdigest()

def main():
    if(len(sys.argv) == 3):
        fname1 = sys.argv[1]
        fname2 = sys.argv[2]

        ChkSum1 = CalculateChkSum(fname1)
        ChkSum2 = CalculateChkSum(fname2)

        if ChkSum1 == ChkSum2:
           print("Success")

        else:
           print("Failure")   

    else:
     print("Invalid no. of arguments:")    
    
if __name__ == "__main__":
    main()