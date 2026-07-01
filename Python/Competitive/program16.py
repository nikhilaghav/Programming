def CheckVowel(ch):
    ch = ch.lower()
    return ch in "aeiou"

def main():
    ch = input("enter character:")
    
    Ret = CheckVowel(ch)
    if Ret:
        print("It is Vowel")
    else:
        print("It is Consonant")    

if __name__ == "__main__":
    main()        