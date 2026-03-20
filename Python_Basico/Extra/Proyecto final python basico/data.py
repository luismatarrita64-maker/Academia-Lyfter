import csv

def export_data(students_list):
    file_path = "students.csv"
    headers = ['full name', 'section', 'spanish note', 'english note', 'social_studies note', 'science note']

    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            writer = csv.DictWriter(file, headers)
            writer.writeheader()
            writer.writerows(students_list)
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
                student = {
                    'full name': row['full name'],
                    'section': row['section'],
                    'spanish note': int(row['spanish note']),
                    'english note': int(row['english note']),
                    'social_studies note': int(row['social_studies note']),
                    'science note': int(row['science note'])
                }
                students_list.append(student)
        print("Data imported successfully from students.csv")
    except FileNotFoundError:
        print("No CSV file found. Please export data first.")
