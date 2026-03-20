import csv

def search_by_classification(file_path):
    classification_to_find = input("Enter the classification to search : ")
    classification_to_find = classification_to_find.upper()

    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        found = False

        for row in reader:
            if row["classification"] == classification_to_find:
                found = True
                for key, value in row.items():
                    print(f"{key}: {value}")
                


        if not found:
            print("No found games with this classification .")

search_by_classification('games1.csv')

