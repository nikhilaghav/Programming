def Score(No):
    if(No >= 75):
        print("Distinction")
    elif(No >=60 and No < 75):
        print("First class")   
    elif(No >=50 and No < 60):
        print("Second class")    
    else:
        print("fail")             
    
def main():
    num = float(input("Enter marks:"))

    Score(num)    

if __name__ =="__main__":
    main()