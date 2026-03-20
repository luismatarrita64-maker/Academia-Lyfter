def add_student(students_list):

    print("Enter your full name : ")
    full_name = input()

    print("Enter the section : ")
    section = input()

    while True :
        spanish = input("Enter the spanish note : ")
        if not spanish.isdigit():
            print("Error: the option must be a number")
            continue
        spanish = int(spanish)
        if spanish < 0 or spanish > 100:
            print("Error: invalid option")
            continue
        break

    while True :
        english = input("Enter the english note : ")
        if not english.isdigit():
            print("Error: the option must be a number")
            continue
        english = int(english)
        if english < 0 or english > 100:
            print("Error: invalid option")
            continue
        break
    
    while True :
        social_studies = input("Enter the social studies note : ")
        if not social_studies.isdigit():
            print("Error: the option must be a number")
            continue
        social_studies = int(social_studies)
        if social_studies < 0 or social_studies > 100:
            print("Error: invalid option")
            continue  
        break  


    while True :
        science = input("Enter the science note : ")
        if not science.isdigit():
            print("Error: the option must be a number")
            continue
        science = int(science)
        if science < 0 or science > 100:
            print("Error: invalid option")
            continue
        break


    student_dictionary = {
    'full name' : full_name,
    'section': section,
    'spanish note' : spanish,
    'english note' : english,
    'social_studies note' : social_studies,
    'science note' : science

    }

    students_list.append(student_dictionary)
    

def view_students(students_list):
    if not students_list :
        print("There are no students yet")
        return

    for dic in students_list:
        
        print(dic)


def view_top_3(students_list):
    
    if not students_list:
        print("There are no students yet")
        return

    
    sorted_students = sorted(
        students_list, 
        key=lambda student: (
            student['spanish note'] +
            student['english note'] +
            student['social_studies note'] +
            student['science note']
        ) / 4, 
        reverse=True
    )

    
    top3 = sorted_students[:3]

    
    print("\n===== TOP 3 STUDENTS =====")
    for i, student in enumerate(top3, start=1):
        average = (
            student['spanish note'] +
            student['english note'] +
            student['social_studies note'] +
            student['science note']
        ) / 4
        print(f"{i}. {student['full name']}, Section {student['section']}, Average: {average:.2f}")
    print("==========================\n")



def view_all_average(students_list):        
    if not students_list:
        print("There are no students yet")
        return

    total_average = 0
    for student in students_list:
        student_average = (
            student['spanish note'] +
            student['english note'] +
            student['social_studies note'] +
            student['science note']) / 4
        total_average += student_average

    overall_average = total_average / len(students_list)

    
    print(f"\nOverall average of all students: {overall_average:.2f}\n")