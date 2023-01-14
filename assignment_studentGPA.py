"""
Calculate Student GPA of each semester per course on based of marks and credit-hours.
"""


class Subject:
    def __init__(self, name, credit_hours, mark):
        self.name = name
        self.credit_hours = credit_hours
        self.mark = mark

    def calculate_grade(self):
        grade = ""
        if self.mark >= 90:
            grade = 4
        elif self.mark >= 80:
            grade = 3.5
        elif self.mark >= 70:
            grade = 3
        elif self.mark >= 60:
            grade = 2.5
        elif self.mark >= 50:
            grade = 2
        elif self.mark >= 40:
            grade = 1.5
        else:
            grade = 0
        return grade

    def __str__(self):
        return "Name: " + self.name + ", Grade: " + str(self.calculate_grade())


class Semester:
    def __init__(self, name):
        self.name = name
        self.subjects = []

    def add_subject(self, subject):
        print(subject)
        self.subjects.append(subject)

    def semester_gpa(self):
        total_credits = 0
        total_marks = 0
        for subject in self.subjects:
            total_credits += subject.credit_hours
            total_marks += subject.calculate_grade() * subject.credit_hours
        return total_marks / total_credits

    def __str__(self):
        return "Name: " + self.name + ", subjects: " + str(self.subjects)


class Student:
    def __init__(self, name):
        self.name = name
        self.semesters = []

    def add_semester(self, semester):
        self.semesters.append(semester)

    def calculate_gpa(self):
        total_gpa = 0
        for semster in self.semesters:
            total_gpa += semster.semester_gpa()
        return total_gpa / len(self.semesters)


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
print("CGPA: ", gpa)