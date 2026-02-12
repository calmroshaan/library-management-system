import mysql.connector as myconn
my_db = myconn.connect(
    host = "localhost",
    user = "root",
    password = "HurryUp#26",
    database = "testdb"
)
mycursor = my_db.cursor()
# **************************************SHOW DATABASES*******************************
# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)
# mycursor.execute("CREATE TABLE students(name VARCHAR(50), age INTEGER(10))")
# mycursor.execute("INSERT INTO students(name, age) VALUES ('Ali', 20), ('Dawood', 18)")
# my_db.commit()
# **************************************SHOW TABLES*******************************
# mycursor.execute("SHOW TABLES")
# for tb in mycursor:
#     print(tb)
# ************************************INSETING DATA INTO TABLE********************************************
# sql_formula_student_table = "INSERT INTO students(name, age) VALUES (%s, %s)"
# student1 = ("Ali", 21)
# student2 = ("Dawood", 19)
# mycursor.execute(sql_formula_student_table, student1)
# mycursor.execute(sql_formula_student_table, student2)
# my_db.commit()

# student3to10 = [
#     ("Fatima", 19),
#     ("Ahmed", 22),
#     ("Ayesha", 20),
#     ("Hassan", 18),
#     ("Zainab", 23),
#     ("Usman", 19),
#     ("Maryam", 21),
#     ("Bilal", 20),
# ]
# mycursor.executemany(sql_formula_student_table, student3to10)
# my_db.commit()
# ************************************FETCHING AND SEEING DATA FROM TABLE********************************************
mycursor.execute("SELECT * FROM students WHERE age = 20")
result = mycursor.fetchall()
print(result)
# for row in result:
#     print(row)