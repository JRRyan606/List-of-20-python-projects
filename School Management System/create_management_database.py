import sqlite3

# Create a SQLite database connection
conn = sqlite3.connect('school.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create tables for students, courses, and enrollments
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    birthdate TEXT,
    email TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY,
    course_code TEXT,
    course_name TEXT,
    instructor TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS enrollments (
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students (id),
    FOREIGN KEY (course_id) REFERENCES courses (id)
)
''')

# Commit changes and close the connection
conn.commit()
conn.close()
