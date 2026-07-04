length = lambda str : len(str) > 5

def main():
    Data = ["pune","mumbai","nashik","satara"]
    
    FData = list(filter(length,Data))

    print(FData)

if __name__ == "__main__":
    main()    