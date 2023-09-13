import sqlite3

# Create a SQLite database connection
conn = sqlite3.connect('student.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a Students table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    roll_number TEXT,
    department TEXT,
    batch TEXT
)
''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database 'student.db' has been created.")
