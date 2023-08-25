class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class User:
    def __init__(self, name):
        self.name = name
        self.books_borrowed = []

    def borrow_book(self, book):
        self.books_borrowed.append(book)

    def return_book(self, book):
        self.books_borrowed.remove(book)

def display_books(books):
    print("Available Books:")
    for i, book in enumerate(books, start=1):
        print(f"{i}. {book.title} by {book.author}")

def display_borrowed_books(user):
    print(f"{user.name}'s Borrowed Books:")
    for i, book in enumerate(user.books_borrowed, start=1):
        print(f"{i}. {book.title} by {book.author}")

def main():
    books = [
        Book("The Catcher in the Rye", "J.D. Salinger"),
        Book("To Kill a Mockingbird", "Harper Lee"),
        Book("1984", "George Orwell"),
        Book("Pride and Prejudice", "Jane Austen")
    ]

    users = [User("Alice"), User("Bob")]

    while True:
        print("\n1. Display available books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_books(books)
        elif choice == "2":
            display_books(books)
            user_choice = int(input("Enter the number of the book you want to borrow: ")) - 1
            selected_book = books[user_choice]
            display_borrowed_books(users[0])
            user_choice = int(input("Enter your user number: ")) - 1
            users[user_choice].borrow_book(selected_book)
            print("Book borrowed successfully!")
        elif choice == "3":
            user_choice = int(input("Enter your user number: ")) - 1
            display_borrowed_books(users[user_choice])
            book_choice = int(input("Enter the number of the book you want to return: ")) - 1
            returned_book = users[user_choice].books_borrowed[book_choice]
            users[user_choice].return_book(returned_book)
            print("Book returned successfully!")
        elif choice == "4":
            print("Exiting the library system.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
