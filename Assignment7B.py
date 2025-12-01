class Book:
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f'You borrowed "{self.title}".')
        else:
            print(f'Error: "{self.title}" is already borrowed.')

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f'You returned "{self.title}".')
        else:
            print(f'Error: "{self.title}" was not borrowed.')

    def display_info(self, index):
        status = "Available" if not self.is_borrowed else "Borrowed"
        print(f"{index} - {self.title} ({status})")


class Library:
    def __init__(self):
        self.books = [Book("Python Basics"), Book("Intro to AI")]

    def show_books(self):
        print("Books in Library:")
        for i, book in enumerate(self.books):
            book.display_info(i)

    def borrow_book(self):
        self.show_books()
        try:
            index = int(input("Select a book to borrow: "))
            self.books[index].borrow()
        except (ValueError, IndexError):
            print("Error: Invalid selection.")

    def return_book(self):
        self.show_books()
        try:
            index = int(input("Select a book to return: "))
            self.books[index].return_book()
        except (ValueError, IndexError):
            print("Error: Invalid selection.")

    def add_book(self):
        title = input("Enter the title of the new book: ")
        self.books.append(Book(title))
        print(f'"{title}" has been added to the library!')


def main():
    library = Library()
    while True:
        print("[Owl Library]")
        print("1. View Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Add Book")
        print("5. Exit")
        choice = input("> ")
        if choice == "1":
            library.show_books()
        elif choice == "2":
            library.borrow_book()
        elif choice == "3":
            library.return_book()
        elif choice == "4":
            library.add_book()
        elif choice == "5":
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()