print(" !!! Welcome to the Library Management System !!!\n")

class libtary: 
 book=[]
 no_of_books=0 
 def add_book(self, book):
    self.book.append(book)
    self.no_of_books += 1
    print(f"Book '{book}' added. Total books are now: {self.no_of_books}")
    return self.no_of_books
 def remove_book(self, book):
        if book in self.books:
            self.book.remove(book)
            self.no_of_books -= 1
            print(f"Book '{book}' removed. Total books are now: {self.no_of_books}")
        else:
            print(f"Book '{book}' not found in the library.")
        return self.no_of_books
 
library1 = libtary()
while True:
    print("\nLibrary Management Menu:")
    print("====================================")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        no_of_books = int(input("Enter the number of books to add: "))
        # print(no_of_books)
        for _ in range(no_of_books):
         book_name = input("Enter the name of the book to add: ")
         library1.add_book(book_name)
    elif choice == '2':
        print("Available Books:", library1.book)
        try:
          no_of_books = int(input("Enter the number of books to remove: "))
          book_name = input("Enter the name of the book to remove: ")
          library1.remove_book(book_name)
        except Exception as e:
          print(f"An error occurred: {e}")
    elif choice == '3':
        print("Exiting the Library Management System.")
        break
    else:
        print("Invalid choice, please try again.")
    