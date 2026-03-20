import csv
from student import Student

def export_data(students_list):
    file_path = "students.csv"
    headers = ['full name', 'section', 'spanish note', 'english note', 'social_studies note', 'science note']

    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            writer = csv.DictWriter(file, headers)
            writer.writeheader()

            rows = [student.to_dict() for student in students_list]  
            writer.writerows(rows)

        print("Data exported successfully to students.csv")

    except Exception as e:
        print("Error exporting data:", e)


def import_data(students_list):
    file_path = "students.csv"

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            students_list.clear()

            for row in reader:
                student = Student.from_dict(row) 
                students_list.append(student)

        print("Data imported successfully from students.csv")

    except FileNotFoundError:
        print("No CSV file found. Please export data first.")