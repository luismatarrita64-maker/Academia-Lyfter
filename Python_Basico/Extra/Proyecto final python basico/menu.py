import actions
import data

def students_menu(students_list):
    while True:
        print("===== MAIN MENU =====")
        print("1. Enter student")
        print("2. View all students")
        print("3. View top 3")
        print("4. View overall average")
        print("5. Export data")
        print("6. Import data ")
        print("7. EXIT")

        option = input("Select an option: ")
        if not option.isdigit():
            print("Error: the option must be a number")
            continue
        option = int(option)

        if option < 1 or option > 7:
            print("Error: invalid option")
            continue
        
        elif option == 1:
            actions.add_student(students_list)
        
        elif option == 2:
            actions.view_students(students_list)
        
        elif option == 3:
            actions.view_top_3(students_list)

        elif option ==4:
            actions.view_all_average(students_list)

        elif option ==5:
            data.export_data(students_list)

        elif option ==6:
            data.import_data(students_list)

        elif option == 7:
            print("Exiting program...")
            break  
