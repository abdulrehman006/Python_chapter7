"""
Calculate Student GPA of each semester per course on based of marks and credit-hours.
"""

class Subject:
    def __init__(self, name, credit_hours, mark):
        self.name = name
        self.credit_hours = credit_hours
        self.mark = mark

    def __str__(self):
        return "Name: " + self.name + ", marks: " + str(self.mark)


class Semester:
    def __init__(self, name):
        self.name = name
        self.subjects = []

    def add_subject(self, subject):
        print(subject)
        self.subjects.append(subject)

    def __str__(self):
        return "Name: " + self.name + ", subjects: " + str(self.subjects)


class Student:
    def __init__(self, name):
        self.name = name
        self.semesters = []

    def add_semester(self, semester):
        self.semesters.append(semester)

    def calculate_gpa(self):
        total_credits = 0
        total_marks = 0
        for semster in self.semesters:
            for subjct in semster.subjects:
                total_credits += subjct.credit_hours
                total_marks += subjct.mark * subjct.credit_hours
        return total_marks / total_credits


name = input("Enter your name: ")
student = Student(name)
semester_name = input("Enter semester name: ")
semester = Semester(semester_name)
while -1:
    print("Press 0 for adding subject")
    print("Press 1 for adding semester")
    print("Press -1 for Exit")
    opt = int(input())
    match opt:
        case 0:
            print("subject")
            subject_name = input("Enter subject name : ")
            credit_hours = int(input("Enter credit hours: "))
            mark = float(input("Enter mark: "))
            subject = Subject(subject_name, credit_hours, mark)
            semester.add_subject(subject)
        case 1:
            student.add_semester(semester)
            semester_name = input("Enter semester name: ")
            semester = Semester(semester_name)
        case -1:
            print("exit")
            break
        case _:
            print("press valid number")

student.add_semester(semester)
gpa = student.calculate_gpa()
print("GPA: ", gpa)