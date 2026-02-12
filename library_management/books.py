from database import create_connection, close_connection

def add_book(title, author, isbn, total_copies):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO books (title, author, isbn, total_copies, available_copies) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (title, author, isbn, total_copies, total_copies))
            conn.commit()
            print(f"Book '{title}' added successfully!")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            close_connection(conn)

def view_all_books():
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM books"
            cursor.execute(query)
            books = cursor.fetchall()
            
            if books:
                print("\n--- All Books ---")
                for book in books:
                    print(f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]} | ISBN: {book[3]} | Total: {book[4]} | Available: {book[5]}")
            else:
                print("No books found.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            close_connection(conn)

def search_books(search_term):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM books WHERE title LIKE %s OR author LIKE %s"
            cursor.execute(query, (f"%{search_term}%", f"%{search_term}%"))
            books = cursor.fetchall()
            
            if books:
                print("\n--- Search Results ---")
                for book in books:
                    print(f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]} | ISBN: {book[3]} | Total: {book[4]} | Available: {book[5]}")
            else:
                print("No books found matching your search.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            close_connection(conn)