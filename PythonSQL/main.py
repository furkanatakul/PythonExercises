import os
import sqlite3
def createDatabase():
    if os.path.exists("students.db"):
        os.remove("students.db")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    return conn, cursor

def createTables(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    age INTEGER,
    email VARCHAR UNIQUE,
    city TEXT     
    )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        courseName VARCHAR(255) NOT NULL,
        instructor TEXT,
        credits INTEGER     
        )
        ''')

def insertSampleData(cursor):

    students = [
        (1, 'Alice Johnson', 20, 'alice@gmail.com', 'New York'),
        (2, 'Bob Smith', 25, 'bob.smith@yahoo.com', 'Los Angeles'),
        (3, 'Charlie Brown', 22, 'charlie.brown@hotmail.com', 'Chicago'),
        (4, 'Diana Miller', 28, 'diana.miller@gmail.com', 'Houston'),
        (5, 'Ethan Davis', 19, 'ethan.davis@yahoo.com', 'Phoenix'),
        (6, 'Fiona Clark', 24, 'fiona.clark@gmail.com', 'Philadelphia'),
        (7, 'George Lewis', 30, 'george.lewis@outlook.com', 'San Antonio'),
        (8, 'Hannah Hall', 21, 'hannah.hall@gmail.com', 'San Diego'),
        (9, 'Ian Wilson', 23, 'ian.wilson@hotmail.com', 'Dallas'),
        (10, 'Julia Taylor', 26, 'julia.taylor@yahoo.com', 'San Jose'),
        (11, 'Kevin Anderson', 27, 'kevin.anderson@gmail.com', 'Austin'),
        (12, 'Laura Martin', 29, 'laura.martin@outlook.com', 'Jacksonville'),
        (13, 'Michael Lee', 31, 'michael.lee@gmail.com', 'San Francisco'),
        (14, 'Natalie Perez', 22, 'natalie.perez@yahoo.com', 'Columbus'),
        (15, 'Oliver Harris', 20, 'oliver.harris@hotmail.com', 'Fort Worth'),
        (16, 'Paula Scott', 24, 'paula.scott@gmail.com', 'Charlotte'),
        (17, 'Quentin Adams', 25, 'quentin.adams@yahoo.com', 'Indianapolis'),
        (18, 'Rachel Evans', 28, 'rachel.evans@gmail.com', 'Seattle'),
        (19, 'Samuel Turner', 26, 'samuel.turner@outlook.com', 'Denver'),
        (20, 'Tina Walker', 23, 'tina.walker@gmail.com', 'Washington'),
        (21, 'Umar Young', 21, 'umar.young@yahoo.com', 'Boston'),
        (22, 'Victoria Hill', 27, 'victoria.hill@gmail.com', 'El Paso'),
        (23, 'William King', 30, 'william.king@outlook.com', 'Nashville'),
        (24, 'Xavier Wright', 22, 'xavier.wright@gmail.com', 'Detroit'),
        (25, 'Yasmine Lopez', 19, 'yasmine.lopez@yahoo.com', 'Baltimore')
    ]

    cursor.executemany("INSERT INTO Students VALUES (?,?,?,?,?)", students)

    courses = [
        ('Introduction to Programming', 'John Smith', 4),
        ('Data Structures and Algorithms', 'Emily Johnson', 5),
        ('Database Systems', 'Michael Brown', 4),
        ('Operating Systems', 'Sarah Davis', 4),
        ('Computer Networks', 'Robert Wilson', 4),
        ('Machine Learning', 'Sophia Martinez', 5),
        ('Artificial Intelligence', 'David Anderson', 5),
        ('Web Development', 'Linda Thompson', 3),
        ('Mobile App Development', 'James White', 3),
        ('Software Engineering', 'Patricia Garcia', 4),
        ('Cyber Security', 'William Martinez', 4),
        ('Cloud Computing', 'Elizabeth Taylor', 3),
        ('Data Science', 'Thomas Lee', 5),
        ('Computer Graphics', 'Barbara Harris', 3),
        ('Human Computer Interaction', 'Christopher Clark', 3)
    ]

    cursor.executemany("INSERT INTO Courses (courseName, instructor, credits) VALUES (?,?,?)", courses)

def basicSQLOperations(cursor):
    # SELECT ALL
    cursor.execute("SELECT * FROM Students")
    for (a,b,c,d,e) in cursor.fetchall():
        print(e)

    # Select Columns
    cursor.execute("SELECT name,age FROM Students")
    print(cursor.fetchall())

    #WHERE Clause
    cursor.execute("SELECT name FROM Students WHERE age <=25")
    print(cursor.fetchall())

    #Order By
    cursor.execute("SELECT * FROM Courses ORDER BY credits DESC")
    print(cursor.fetchall())

def SQLdeleteInsertOperations(conn, cursor):
    #Insert
    cursor.execute("INSERT INTO Students (name, age, email, city) Values ('Ali', 25, 'ali@gmail.com', 'Adana')")
    conn.commit()

    #Update
    cursor.execute("UPDATE Students SET name = 'Ali', age = 25 WHERE name = 'Ali'")
    conn.commit()

    # Delete
    cursor.execute("DELETE FROM Students WHERE id=26")
    conn.commit()

def someFunctions(cursor):
    # Count:
    cursor.execute("SELECT COUNT(*) FROM Students")
    print(cursor.fetchall()[0][0])

    # Average:
    cursor.execute("SELECT AVG(age) FROM Students")
    print(cursor.fetchall()[0][0])

    # Max-Min:
    cursor.execute("SELECT MAX(age), MIN(age) FROM Students")
    print(cursor.fetchall()[0])

    # GROUP BY:
    cursor.execute("SELECT age, COUNT(*) FROM Students GROUP BY age ORDER BY COUNT(*) DESC" )
    print(cursor.fetchall())

def questions():
    '''
    Basit
    1) Bütün kursların bilgilerini getirin
    2) Sadece eğitmenlerin ismini ve ders ismi bilgilerini getirin
    3) Sadece 21 yaşındaki öğrencileri getirin
    4) Sadece Chicago'da yaşayan öğrencileri getirin
    5) Sadece 'Dr. Anderson' tarafından verilen dersleri getirin
    6) Sadece ismi 'A' ile başlayan öğrencileri getirin
    7) Sadece 3 ve üzeri kredi olan dersleri getirin

    Detaylı
    1) Öğrencileri alphabetic şekilde dizerek getirin
    2) 20 yaşından büyük öğrencileri, ismine göre sıralayarak getirin
    3) Sadece 'New York' veya 'Chicago' da yaşayan öğrencileri getirin
    4) Sadece 'New York' ta yaşamayan öğrencileri getirin
'''
def answers(cursor):
    cursor.execute("SELECT * FROM Courses")
    print(cursor.fetchall())
    cursor.execute("SELECT courseName FROM Courses")
    print(cursor.fetchall())
    cursor.execute("SELECT name FROM Students WHERE age=21")
    print(cursor.fetchall())
    cursor.execute("SELECT name FROM Students WHERE city='Chicago'")
    print(cursor.fetchall())
    cursor.execute("SELECT courseName FROM Courses WHERE instructor='William Martinez'")
    print(cursor.fetchall())
    cursor.execute("SELECT name FROM Students WHERE name LIKE 'a%'")
    print(cursor.fetchall())
    cursor.execute("SELECT courseName FROM Courses WHERE credits >= 3")
    print(cursor.fetchall())
    cursor.execute("SELECT name FROM Students ORDER BY name")
    print(cursor.fetchall())
    cursor.execute("SELECT name,age FROM Students WHERE age >20 ORDER BY name")
    print(cursor.fetchall())
    cursor.execute("SELECT name FROM Students WHERE city IN ('New York', 'Chicago')")
    print(cursor.fetchall())
    cursor.execute("SELECT name FROM Students WHERE city = 'New York'")
    print(cursor.fetchall())


def main():
    conn, cursor = createDatabase()
    try:
        createTables(cursor)
        insertSampleData(cursor)
        basicSQLOperations(cursor)
        SQLdeleteInsertOperations(conn, cursor)
        someFunctions(cursor)
        answers(cursor)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

if __name__ == "__main__":
    main()

