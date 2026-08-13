def BigBazar():
    print("Inside bigbazr")

    def Amul():
          print("Inside amul icecream parlor")

def main():
    BigBazar()        #Allowed
    Amul()           #ERROR
    BigBazar.Amul()  #ERROR

    
if __name__ =="__main__":
        main()

