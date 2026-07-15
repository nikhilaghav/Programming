class BankAccount:
    ROI = 10.5

    def __init__(self,Name,Amount):
        self.name = Name 
        self.amount = Amount

    def Display(self):
        print(f"Name:{self.name} Balance:{self.amount}")

    def Deposit(self):
        value = int(input("Enter amount to deposit:"))
        self.amount = self.amount + value

    def Withdraw(self):
        value = int(input("Enter rupees to withdraw:"))

        if(value <= 0):
            print("Invalid input..")
        elif(value > self.amount):
            print("You dont have enough balance...")

        else:
            self.amount = self.amount - value

    def CalculateInterest(self):
        return ((self.amount) * self.ROI) / 100    

def main():
    obj1 = BankAccount("Nikhil", 50000)
    obj2 = BankAccount("Aman",20000)

    obj1.Display()
    obj1.Deposit()
    obj1.Display()
    obj1.Withdraw()
    obj1.Display()

    Ret = obj1.CalculateInterest()
    print(f"Interest will be:{Ret} rupees")




if __name__ == "__main__":
    main()   