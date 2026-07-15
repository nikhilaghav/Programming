class Numbers:
        def __init__(self, No):
                self.value = No

        def ChkPrime(self):
                i = 0

                if(self.value <= 0):
                        return False
                
                for i in range(2, self.value//2 + 1):
                        if(self.value % i == 0):
                                return False

                return True
        
        def ChkPerfect(self):
                sum = 0

                for i in range(1, self.value//2 + 1):
                        if(self.value % i == 0):
                                sum = sum + i

                if(sum == self.value):
                        return True
                
                else:
                        return False
                
        def Factors(self):
                for i in range(1, self.value//2 + 1):
                        if(self.value % i == 0):
                                print(i)

        def SumFactors(self):
                sum = 0

                for i in range(1, self.value//2 + 1):
                        if(self.value % i == 0):
                                sum = sum + i
                
                return sum

def main():
        obj1 = Numbers(28)

        Ret =obj1.ChkPrime()
        if Ret:
                print("It is Prime")
        else:
                print("It is not prime")

        Ret = obj1.ChkPerfect()
        if Ret:
                print("It is perfect")
        else:
                print("It is not perfect")

        obj1.Factors()

        Ret = obj1.SumFactors()
        print("sum of factors is:",Ret)

        
if __name__ == "__main__":
        main()        