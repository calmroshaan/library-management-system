from database import create_connection, close_connection
from datetime import date

def borrow_book(book_id, member_id):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            
            # Check if book is available
            cursor.execute("SELECT available_copies FROM books WHERE book_id = %s", (book_id,))
            result = cursor.fetchone()
            
            if result and result[0] > 0:
                # Insert borrow record
                query = "INSERT INTO borrowed_books (book_id, member_id) VALUES (%s, %s)"
                cursor.execute(query, (book_id, member_id))
                
                # Decrease available copies
                update_query = "UPDATE books SET available_copies = available_copies - 1 WHERE book_id = %s"
                cursor.execute(update_query, (book_id,))
                
                conn.commit()
                print("Book borrowed successfully!")
            else:
                print("Book not available or doesn't exist.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            close_connection(conn)

def return_book(borrow_id):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            
            # Check if book is already returned
            cursor.execute("SELECT book_id, return_date FROM borrowed_books WHERE borrow_id = %s", (borrow_id,))
            result = cursor.fetchone()
            
            if result and result[1] is None:  # return_date is NULL
                book_id = result[0]
                
                # Update return date
                update_borrow = "UPDATE borrowed_books SET return_date = %s WHERE borrow_id = %s"
                cursor.execute(update_borrow, (date.today(), borrow_id))
                
                # Increase available copies
                update_books = "UPDATE books SET available_copies = available_copies + 1 WHERE book_id = %s"
                cursor.execute(update_books, (book_id,))
                
                conn.commit()
                print("Book returned successfully!")
            else:
                print("Invalid borrow ID or book already returned.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            close_connection(conn)

def view_borrowed_books():
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
            SELECT bb.borrow_id, b.title, m.name, bb.borrow_date, bb.return_date
            FROM borrowed_books bb
            JOIN books b ON bb.book_id = b.book_id
            JOIN members m ON bb.member_id = m.member_id
            """
            cursor.execute(query)
            records = cursor.fetchall()
            
            if records:
                print("\n--- Borrowed Books ---")
                for record in records:
                    status = "Returned" if record[4] else "Not Returned"
                    print(f"Borrow ID: {record[0]} | Book: {record[1]} | Member: {record[2]} | Borrowed: {record[3]} | Status: {status}")
            else:
                print("No borrowed books.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            close_connection(conn)