# Hughes Izah Ps ID: 2310365


import csv
from datetime import datetime


class Student:
    def __init__(self, student_id, last_name, first_name, major, gpa, graduation_date, disciplinary_action):
        self.student_id = student_id
        self.last_name = last_name
        self.first_name = first_name
        self.major = major
        self.gpa = gpa
        self.graduation_date = graduation_date
        self.disciplinary_action = disciplinary_action

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.first_name} {self.last_name}, GPA: {self.gpa}"


def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data


def parse_data(students_data, gpas_data, graduation_dates_data):
    students = []
    for student_row in students_data:
        student_id, last_name, first_name, major, *disciplinary_action = student_row
        student_gpa = next((float(row[1]) for row in gpas_data if row[0] == student_id), None)
        graduation_date_str = next((row[1] for row in graduation_dates_data if row[0] == student_id), None)
        graduation_date = datetime.strptime(graduation_date_str, '%m/%d/%Y') if graduation_date_str else None
        disciplinary_action = disciplinary_action[0] if disciplinary_action else None
        if student_gpa is not None and graduation_date is not None:
            students.append(Student(student_id, last_name, first_name, major.strip(), student_gpa, graduation_date, disciplinary_action))
    return students


def find_students(students, major, gpa):
    within_01_students = []
    within_025_students = []
    current_date = datetime.now()
    for student in students:
        if student.major.lower() == major.lower() and not student.graduation_date < current_date and not student.disciplinary_action:
            if abs(student.gpa - gpa) <= 0.10001:
                within_01_students.append(student)
            elif abs(student.gpa - gpa) <= 0.250001:
                within_025_students.append(student)
    if not within_01_students and not within_025_students:
        # Find the closest student by GPA within the requested major
        closest_student = min((s for s in students if s.major.lower() == major.lower() and not s.graduation_date < current_date and not s.disciplinary_action),
                              key=lambda x: abs(x.gpa - gpa), default=None)
        if closest_student:
            within_025_students.append(closest_student)
    return within_01_students, within_025_students


def main():
    students_data = read_csv('StudentsMajorsList-3.csv')
    gpas_data = read_csv('GPAList-1.csv')
    graduation_dates_data = read_csv('GraduationDatesList-1.csv')

    students = parse_data(students_data, gpas_data, graduation_dates_data)

    while True:
        query = input("Enter major and GPA or 'q' to quit: ")
        if query.lower() == 'q':
            break
        query_parts = query.split()
        try:
            major = ' '.join(query_parts[:-1])
            gpa = float(query_parts[-1])
            if len(query_parts) < 2:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter major and GPA separated by space.")
            continue

        within_01_students, within_025_students = find_students(students, major, gpa)

        if not within_01_students and not within_025_students:
            print("No student")
        else:
            print("student(s):")
            for student in within_01_students:
                print(student)
            print("You may consider:")
            for student in within_025_students:
                print(student)
