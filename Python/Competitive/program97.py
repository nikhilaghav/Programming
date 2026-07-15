class BookStore:
    NoOfBooks = 0

    def __init__(self,Name,Author):
        self.name = Name 
        self.author = Author

        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print(f"{self.name} by {self.author} No. of books:{BookStore.NoOfBooks}")
        print()

def main():
    obj1 = BookStore("Linux system programming","Robert love")
    obj1.Display()

    obj1 = BookStore("C programming","Dennis Ritchie")
    obj1.Display()

if __name__ == "__main__":
    main()   