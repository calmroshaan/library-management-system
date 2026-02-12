# Library Management System

A command-line application to manage library operations including books, members, and borrowing records.

## Features

- **Book Management**: Add, view, and search books
- **Member Management**: Register members and maintain records
- **Borrowing System**: Track book borrowing and returns
- **Real-time Availability**: Automatic updates of book availability

## Technologies Used

- **Python 3.x**: Core programming language
- **MySQL**: Database management
- **mysql-connector-python**: Database connectivity

## Database Schema

### Tables:
- `books`: Stores book information and availability
- `members`: Manages library member details
- `borrowed_books`: Tracks borrowing history and returns

## Setup Instructions

1. **Clone the repository**
```bash
   git clone https://github.com/calmroshaan/library-management-system.git
   cd library-management-system
```

2. **Install MySQL and create database**
```sql
   CREATE DATABASE library_db;
```

3. **Run the SQL schema** (create tables as per `database.py`)

4. **Install required packages**
```bash
   pip install mysql-connector-python
```

5. **Update database credentials** in `database.py`:
```python
   user='your_username'
   password='your_password'
```

6. **Run the application**
```bash
   python main.py
```

## Usage

The application provides a menu-driven interface with the following options:
- Add and manage books
- Register and search members
- Borrow and return books
- View all records and borrowing history

## Project Structure
```
library-management-system/
├── main.py          # Main application menu
├── database.py      # Database connection
├── books.py         # Book operations
├── members.py       # Member operations
├── borrow.py        # Borrowing operations
└── README.md        # Project documentation
```

## Future Enhancements

- Add due date tracking and late fees
- Implement book reservation system
- Generate reports and statistics
- Add GUI interface

## Author

Built as a learning project to practice Python, MySQL, and Git/GitHub.