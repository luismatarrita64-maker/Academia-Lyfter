from student import Student

def add_student(students_list):
    print("Enter your full name : ")
    full_name = input()

    print("Enter the section : ")
    section = input()

    while True:
        spanish = input("Enter the spanish note : ")
        if spanish.isdigit() and 0 <= int(spanish) <= 100:
            spanish = int(spanish)
            break
        print("Error: invalid option")

    while True:
        english = input("Enter the english note : ")
        if english.isdigit() and 0 <= int(english) <= 100:
            english = int(english)
            break
        print("Error: invalid option")

    while True:
        social_studies = input("Enter the social studies note : ")
        if social_studies.isdigit() and 0 <= int(social_studies) <= 100:
            social_studies = int(social_studies)
            break
        print("Error: invalid option")

    while True:
        science = input("Enter the science note : ")
        if science.isdigit() and 0 <= int(science) <= 100:
            science = int(science)
            break
        print("Error: invalid option")

    student = Student(full_name, section, spanish, english, social_studies, science)
    students_list.append(student)
    print("Student saved!")


def view_students(students_list):
    if not students_list:
        print("There are no students yet")
        return

    for student in students_list:
        print(student)


def view_top_3(students_list):
    if not students_list:
        print("There are no students yet")
        return

    sorted_students = sorted(students_list, key=lambda s: s.average(), reverse=True)
    top3 = sorted_students[:3]

    print("TOP 3 STUDENTS ")
    for i, student in enumerate(top3, 1):
        print(f"{i}. {student.full_name}, Section {student.section}, Average: {student.average():.2f}")
    


def view_all_average(students_list):
    if not students_list:
        print("There are no students yet")
        return

    total = sum(student.average() for student in students_list)
    overall_average = total / len(students_list)

    print(f"\nOverall average of all students: {overall_average:.2f}\n")