'''
Create a Library Management System in Python using OOP with Book and EBook classes, 
a Library class, file handling, exception handling, and a menu loop until the user exits.

Key points (bullets):

1. Use classes: Book, EBook (inherits Book with file_size), and Library.
2. Library must support: add book, remove by ISBN, search by title.
3. Prevent duplicate books (check by ISBN).
4. Use file handling (save/load books in a file, e.g., JSON).
5. Use try-except for input and file errors.
6. Use a while loop menu (Add / Remove / Search / Exit).
 
'''


class Book:

    def __init__(self, book_id, title, author_name,  quantity):
        self.book_id=book_id
        self.title=title
        self.author_name=author_name
        # self.price=price
        self.quantity=quantity    # Available quantity of the book

    def display_book_info(self):
        print(f"{self.book_id},{self.title},{self.author_name},{self.price},{self.quantity}")

    def check_availability(self):
        return self.quantity>0 # book is available
    
    def update_quantity(self, quantity):
        self.quantity += quantity #Changes the number of books


class User:

    def __init__(self,user_id, name):
        self.user_id=user_id
        self.name=name
        self.borrowed_books=[] # here we can list by appending how many books are borrow

        # 3 methods here
        ''''' borrow_book(book): Allows a user to borrow a book, if it's available.
              return_book(book): Allows a user to return a book they have borrowed.
              view_borrowed_books(): Displays a list of all the books borrowed by the user.
        '''
    def borrow_book(self,book):

        if book.check_availability():
            self.borrowed_books.append(book)
            book.update_quantity(-1)  # decreasing quantity of remaining books
            print(f"{self.name} has borrowed {book.title} ")
        else:
            print(" Books is not available right now ")

    def return_book(self, book):

        if book in self.borrow_book():
            self.borrow_book.remove(book)
            book.update_quantity(1)
            print(f"{self.name} has returned '{book.title}'")
        else:
            print(f"{self.name} does not have '{book.title}' borrowed.")

    def view_borrowed_books(self):

        if self.borrowed_books: #the list has at least one book, this is True.


            ''''
             first, print the users name: eg:  "Alice's Borrowed Books:"

              Then, go one by one through the list (for book in self.borrowed_books)

              Print the title of each book with a dash - in front. 

               Check if the user borrowed any books.
               If yes → list them one by one.
                If no → show a message saying no books.
            '''
               
            print(f"{self.name} has borrowed a book")
            for book in self.borrowed_books:
                print(f" - {book.title}")

class Library:
   # add_book(book):, register_user(user), search_book_by_title(title),
   # list_books(): and add_new_book():
    def __init__(self):
        self.books=[] # list to store all books in the library
        self.users=[] # List to store all users of the library

    def add_book(self,book):

        self.books.append(book)

    def register_user(self,user):  # Takes a User object as input.
        # register new user and no duplicate user

        if any(current_user.user_id == user.user_id for current_user in self.users):
            print("Same username exist already!!!")
            return
        self.users.append(user) # add user to self.users list
        print(f"New user {user.name} is successfully added")


    def search_book_by_title(self,title):
        found_books = [] #initally empy, if will be added and display
        # Go through every book in the library
        for book in self.books:
        # Convert both the search title and
         #  book title to lowercase for case-insensitive search
            if title.lower() in book.title.lower():
                found_books.append(book)

        return found_books
    
    def list_book(self):

        if self.books:
            print("Books are in library: ")
            for book in self.books:
                book.display_book_info()
        else:
            print("No books available in Library")

    def add_new_book(self):

    # Step 1: Get book ID
        book_id = int(input("Enter book ID: "))

    # Step 2: Check if the book ID already exists
        book_exists = False
        for book in self.books:
         if book.book_id == book_id:
            book_exists = True
            break

        if book_exists:
         print("Book with the same ID already exists!")
         return

        # Step 3: Get other book details
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        quantity = int(input("Enter the quantity of books: "))

        # Step 4: Create a new Book object and add it to the library
        new_book = Book(book_id, title, author, quantity)
        self.add_book(new_book)
        print("Book added successfully!")
        new_book.display_book_info()


def main():
    ''''
The main function acts as the entry point of the program, where the library system is initialized, 
books and users are added, and a menu-driven interface allows interaction with the system.

'''

    


    library = Library()
    # # Adding some books to the library

    book1 = Book(1, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 5)
    book2 = Book(2, "The Hobbit", "J.R.R. Tolkien", 3)
    book3 = Book(3, "1984", "George Orwell", 2)


    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Registering users
    user1 = User(1, "sandesh")
    user2 = User(2, "kapil")
        
    library.register_user(user1)
    library.register_user(user2)

    #Menu
    while True:
            print("1. list the books")
            print("2. add books")
            print("3. Search for a book by title")
            print("4. Borrow a book")
            print("5. Return a book")
            print("6. View borrowed books")
            print("7. Add new User")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                library.list_book()

            elif choice == '2':
                library.add_new_book()

            elif choice == '3':
                title = input("Enter the book title to search: ")
                found_books = library.search_book_by_title(title)
                if  found_books:
                    for book in found_books:
                        book.display_book_info()
                else:
                    print(f"No books found with the title '{title}'.")

            elif choice == '4':
                user_id = int(input("Enter your user ID: "))
                book_id = int(input("Enter the book ID to borrow: "))

                user = next((u for u in library.users if u.user_id == user_id), None)
                book = next((b for b in library.books if b.book_id == book_id), None)
                if user and book:
                    user.borrow_book(book)
                else:
                    print("Invalid user or book ID.")
            
            elif choice == '5':
                user_id = int(input("Enter your user ID: "))
                book_id = int(input("Enter the book ID to return: "))
                user = next((u for u in library.users if u.user_id == user_id), None)
                book = next((b for b in library.books if b.book_id == book_id), None)
                if user and book:
                    user.return_book(book)
                else:
                    print("Invalid user or book ID.")

            elif choice == '6':
                user_id = int(input("Enter your user ID: "))
                user = next((u for u in library.users if u.user_id == user_id), None)
                if user:
                    user.view_borrowed_books()
                else:
                    print("Invalid user ID.")

            elif choice == '7':
                id = int(input("Enter user id: "))
                name = input("Enter user's name: ")
                user = User(id, name)
                library.register_user(user)

            elif choice == '8':
                print("Exiting the system. Goodbye!")
                break

            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":

    main()