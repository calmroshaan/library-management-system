from books import add_book, view_all_books, search_books
from members import add_member, view_all_members, search_member
from borrow import borrow_book, return_book, view_borrowed_books

def main_menu():
    while True:
        print("\n=== Library Management System ===")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Books")
        print("4. Add Member")
        print("5. View All Members")
        print("6. Search Member")
        print("7. Borrow Book")
        print("8. Return Book")
        print("9. View Borrowed Books")
        print("10. Exit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            total_copies = int(input("Enter total copies: "))
            add_book(title, author, isbn, total_copies)
            
        elif choice == "2":
            view_all_books()
            
        elif choice == "3":
            search_term = input("Enter title or author to search: ")
            search_books(search_term)
            
        elif choice == "4":
            name = input("Enter member name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            add_member(name, email, phone)
            
        elif choice == "5":
            view_all_members()
            
        elif choice == "6":
            search_term = input("Enter name or email to search: ")
            search_member(search_term)
            
        elif choice == "7":
            book_id = int(input("Enter book ID: "))
            member_id = int(input("Enter member ID: "))
            borrow_book(book_id, member_id)
            
        elif choice == "8":
            borrow_id = int(input("Enter borrow ID: "))
            return_book(borrow_id)
            
        elif choice == "9":
            view_borrowed_books()
            
        elif choice == "10":
            print("Exiting... Goodbye!")
            break
            
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()