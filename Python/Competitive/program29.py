Min = lambda no1, no2 : no1 if no1 < no2 else no2

def main():
    Ret = Min(26,13)

    if Ret:
      print("Minimum is:",Ret)

if __name__ == "__main__":
    main()    