from mylibrary.library import Library

library = Library()


def menu():
    while True:
        print("--- Library Management Software ---")
        print("1. Add a book")
        print("2. Delete the book")
        print("3. Search")
        print("4. Show all books")
        print("5. Exit")

        choice = input("Select (1/2/3/4/5): ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")

            library.add_book(title, author)

        elif choice == "2":
            title = input("Title for deletion: ")

            library.remove_book(title)

        elif choice == "3":
            title = input("Title for search: ")

            library.search_book(title)

        elif choice == "4":
            library.show_books()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    menu()