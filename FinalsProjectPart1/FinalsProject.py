"""Hughes Izah"""
"""2310365"""


import csv


class Student:
    def __init__(self, id, last_name, first_name, major, gpa, grad_date, disciplinary_action):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.major = major
        self.gpa = gpa
        self.grad_date = grad_date
        self.disciplinary_action = disciplinary_action


students = {}

with open('StudentsMajorsList.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        id = row[0]
        last_name = row[1]
        first_name = row[2]
        major = row[3]
        disciplinary_action = row[4] if len(row) > 4 else None
        students[id] = Student(id, last_name, first_name, major, None, None, disciplinary_action)

# Reading GPAList.csv and updating student GPA in the dictionary
with open('GPAList.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        id = row[0]
        gpa = float(row[1])
        students[id].gpa = gpa

# Reading GraduationDatesList.csv and updating student graduation date in the dictionary
with open('GraduationDatesList.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        id = row[0]
        grad_date = row[1]
        students[id].grad_date = grad_date

# Infinite loop to accept user queries
while True:
    query = input('Enter a major and GPA (or "q" to quit): ')
    if query == 'q':
        break
    major, gpa = query.split()
    gpa = float(gpa)
    found = False
    for student in students.values():
        if student.major == major and abs(student.gpa - gpa) <= 0.1 and not student.grad_date and not student.disciplinary_action:
            print(f'Student: {student.id}, {student.first_name}, {student.last_name}, {student.gpa}')
            found = True
    if not found:
        print('No students found for the given criteria.')
