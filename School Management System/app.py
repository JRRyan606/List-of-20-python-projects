import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem
import sqlite3

class SchoolManagementApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('School Management System')
        self.setGeometry(100, 100, 800, 600)

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.first_name_input = QLineEdit()
        self.last_name_input = QLineEdit()
        self.birthdate_input = QLineEdit()
        self.email_input = QLineEdit()

        add_student_button = QPushButton('Add Student')
        add_student_button.clicked.connect(self.add_student)

        self.student_table = QTableWidget()
        self.student_table.setColumnCount(5)
        self.student_table.setHorizontalHeaderLabels(['ID', 'First Name', 'Last Name', 'Birthdate', 'Email'])

        layout.addWidget(QLabel('Student Information:'))
        layout.addWidget(self.first_name_input)
        layout.addWidget(self.last_name_input)
        layout.addWidget(self.birthdate_input)
        layout.addWidget(self.email_input)
        layout.addWidget(add_student_button)
        layout.addWidget(QLabel('Student List:'))
        layout.addWidget(self.student_table)

        central_widget.setLayout(layout)

    def add_student(self):
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        birthdate = self.birthdate_input.text()
        email = self.email_input.text()

        if first_name and last_name and birthdate and email:
            conn = sqlite3.connect('school.db')
            cursor = conn.cursor()

            cursor.execute('INSERT INTO students (first_name, last_name, birthdate, email) VALUES (?, ?, ?, ?)',
                           (first_name, last_name, birthdate, email))

            conn.commit()
            conn.close()

            self.display_students()
            self.clear_inputs()

    def display_students(self):
        conn = sqlite3.connect('school.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM students')
        students = cursor.fetchall()

        self.student_table.setRowCount(0)

        for row_num, student in enumerate(students):
            self.student_table.insertRow(row_num)
            for col_num, data in enumerate(student):
                self.student_table.setItem(row_num, col_num, QTableWidgetItem(str(data)))

        conn.close()

    def clear_inputs(self):
        self.first_name_input.clear()
        self.last_name_input.clear()
        self.birthdate_input.clear()
        self.email_input.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SchoolManagementApp()
    window.show()
    sys.exit(app.exec())
