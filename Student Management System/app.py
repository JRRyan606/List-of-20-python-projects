import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem
import sqlite3

class StudentManagementApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Student Management System')
        self.setGeometry(100, 100, 800, 600)

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.roll_number_input = QLineEdit()
        self.department_input = QLineEdit()
        self.batch_input = QLineEdit()

        add_button = QPushButton('Add Student')
        add_button.clicked.connect(self.add_student)

        self.student_table = QTableWidget()
        self.student_table.setColumnCount(5)
        self.student_table.setHorizontalHeaderLabels(['ID', 'Name', 'Roll Number', 'Department', 'Batch'])

        layout.addWidget(QLabel('Student Information:'))
        layout.addWidget(self.name_input)
        layout.addWidget(self.roll_number_input)
        layout.addWidget(self.department_input)
        layout.addWidget(self.batch_input)
        layout.addWidget(add_button)
        layout.addWidget(QLabel('Students List:'))
        layout.addWidget(self.student_table)

        central_widget.setLayout(layout)

    def add_student(self):
        name = self.name_input.text()
        roll_number = self.roll_number_input.text()
        department = self.department_input.text()
        batch = self.batch_input.text()

        if name and roll_number and department and batch:
            conn = sqlite3.connect('student.db')
            cursor = conn.cursor()

            cursor.execute('INSERT INTO students (name, roll_number, department, batch) VALUES (?, ?, ?, ?)',
                           (name, roll_number, department, batch))

            conn.commit()
            conn.close()

            self.display_students()
            self.clear_inputs()

    def display_students(self):
        conn = sqlite3.connect('student.db')
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
        self.name_input.clear()
        self.roll_number_input.clear()
        self.department_input.clear()
        self.batch_input.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StudentManagementApp()
    window.show()
    sys.exit(app.exec())
