# Ensure all of the following requirements are implemented to practice OOP:
# - Adding a new book with all relevant details.
# - Allowing users to borrow a book, marking it as "Borrowed."
# - Allowing users to return a book, marking it as "Available."
# - Searching for a book by its unique identifier (ISBN or title) and displaying its details.
# - Displaying a list of all books with their unique identifiers.
# - Adding a new user with user details.
# - Viewing user details.
# - Displaying a list of all users.
# - Adding a new author with author details.
# - Viewing author details.
# - Displaying a list of all authors.
# - Adding a new genre with genre details.
# - Viewing genre details.
# - Displaying a list of all genres.
# - Quitting the application.

class Book_Operations:
    def __init__(self):
        self.library = []

    def book_menu(self):
        while True:
            try:
                choice = int(input("""
                Book Operations Menu:
                1. Add a new book
                2. Quit\n
                CHOICE: """))

                if choice not in range(1, 3):
                    raise ValueError("ERROR: Choice must be an integer value within range of 1-2!")

                return choice

            except ValueError as e:
                print("ERROR:", e)

    def add_book(self):
        while True:
            print("To add a new book, enter the following information:")
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            genre = input("Enter genre: ")
            publication_date = input("Enter publication date: ")
            availability_status = input("Enter availability status: ")

            self.library.append([title, author, isbn, genre, publication_date, availability_status])

            add_another_book = input("Would you like to add another book? (Y or N): ").upper()
            if add_another_book != 'Y':
                break

        print("BOOK ADDED!")

class User_Operations:
    def __init__(self, name, library):
        self.name = name
        self.library = library
        self.borrowed_books = []

    def borrow_book(self):
        book_title = input("Enter the title of the book you want to borrow: ")
        for book in self.library:
            if book[0].lower() == book_title.lower():
                book[-1] = "Unavailable".lower()
                print(f"{book_title.upper()} IS NOW CHECKED OUT!")
                return
        print("BOOK NOT FOUND!")

    def return_book(self):
        book_title = input("Enter the title of the book you want to return: ")
        for book in self.library:
            if book[0].lower() == book_title.lower():
                if book[-1] == "Unavailable".lower():
                    print("BOOK RETURNED!")
                    book[-1] = "Available".lower()
                    return
                else:
                    print("BOOK NOT BORROWED!")
                    return
        print("BOOK NOT IN SYSTEM!")

    def display_book(self):
        if not self.library:
            print("EMPTY LIBRARY!")
        else:
            for index, book in enumerate(self.library, 1):
                print(f"BOOK #{index}: {book}")

class Author_Operations:
    def __init__(self, library):
        self.library = library

    def update_author(self):
        author_name = input("Enter the name of the author you want to update: ")
        new_name = input("Enter the new name of the author: ")

        for book in self.library:
            if book[1].lower() == author_name.lower():
                book[1] = new_name
        print("Author name updated!")

class Genre_Operations:
    def __init__(self, library):
        self.library = library

    def update_genre(self):
        book_title = input("Enter the title of the book you want to update the genre for: ")
        new_genre = input("Enter the new genre for the book: ")

        for book in self.library:
            if book[0].lower() == book_title.lower():
                book[3] = new_genre
                print(f"GENRE UPDATED FOR {book_title}.")
                return
        print("BOOK NOT FOUND!")
