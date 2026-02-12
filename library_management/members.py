from database import create_connection, close_connection

def add_member(name, email, phone):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO members (name, email, phone) VALUES (%s, %s, %s)"
            cursor.execute(query, (name, email, phone))
            conn.commit()
            print(f"Member '{name}' registered successfully!")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            close_connection(conn)

def view_all_members():
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM members"
            cursor.execute(query)
            members = cursor.fetchall()
            
            if members:
                print("\n--- All Members ---")
                for member in members:
                    print(f"ID: {member[0]} | Name: {member[1]} | Email: {member[2]} | Phone: {member[3]} | Joined: {member[4]}")
            else:
                print("No members found.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            close_connection(conn)

def search_member(search_term):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM members WHERE name LIKE %s OR email LIKE %s"
            cursor.execute(query, (f"%{search_term}%", f"%{search_term}%"))
            members = cursor.fetchall()
            
            if members:
                print("\n--- Search Results ---")
                for member in members:
                    print(f"ID: {member[0]} | Name: {member[1]} | Email: {member[2]} | Phone: {member[3]} | Joined: {member[4]}")
            else:
                print("No members found matching your search.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            close_connection(conn)