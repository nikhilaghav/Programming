class Circle:
    PI = 3.14

    def __init__(self):
        self.radius = 0
        self.Area = 0
        self.circumference = 0
    
    def Accept(self):
        self.radius = int(input("enter radius:"))

    def CalculateArea(self):
        self.Area = Circle.PI * self.radius * self.radius     

    def CalculateCircumferenc(self):
        self.circumference = 2 * Circle.PI * self.radius

    def Display(self):
        print("entered radius is:",self.radius)
        print("Area is:",self.Area)         
        print("Circumference is:",self.circumference)         

def main():
    obj1 = Circle()
    obj2 = Circle()

    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumferenc()
    obj1.Display()

    print("")

    obj2.Accept()
    obj2.CalculateArea()
    obj2.CalculateCircumferenc()
    obj2.Display()

if __name__ == "__main__":
    main()    