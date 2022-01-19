class Library:

    def __init__(self,library_name, books_list):
        self.books_list = books_list
        self.library_name = library_name
        self.lend_record = {}

    def available(self):
        return self.books_list

    def add_book(self):
        book = input("Enter Book name : ")
        self.books_list.append(book)
        print("Thankyou for your contribution !!!")

    def not_available(self):
        return self.lend_record

    def lend_book(self):
        book = input("Enter Book you want to lend : ").capitalize()
        if book not in self.lend_record:
            name = input("Enter your name : ").capitalize()
            self.lend_record.update({book:name})
            print("Transaction Successful")
        else:
            print(f"This book is taken by {self.lend_record[book]}")

    def return_book(self):
        book = input("Enter the book you want to return : ").capitalize()
        if book in self.lend_record:
            self.books_list.append(book)
            print("Transaction Successful.")
        else:
            print("Its an invalid input !!! -- Return the book that you have.")

if __name__ == '__main__':

    books = ["PYTHON-PROGRAMMING","CLOUD COMPUTING AZURE","SQL DATABASE","FOGLIGHT ARCHITECTURE","VOYA FINANCIALS","COGNIZANT"]
    Aaquibs_library = Library("Aaquibs Library",books)
    print(f"\n\t\t\tWelcome To {Aaquibs_library.library_name}")

    while True:

        choice = int(input("\nEnter you Choice { 1 - available , 2 - lend , 3 - return , 4 - donate , 5 - Exit } = "))

        if choice == 1 :
            print("\nThese are the books we own :",*Aaquibs_library.available(),sep="\n")
            print("\nThese are the books not available :",*Aaquibs_library.not_available(),sep="\n")

        elif choice == 2 :
            Aaquibs_library.lend_book()

        elif choice == 3 :
            Aaquibs_library.return_book()

        elif choice == 4 :
            Aaquibs_library.add_book()

        elif choice == 5 :
            exit()

        else:
            print("Enter a valid Choice !")








