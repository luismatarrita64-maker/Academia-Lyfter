import csv

def name_developer(file_path):
    all_games = input("enter the company name : ")
    all_games = all_games.lower()

    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        found = False

        for row in reader:
            if row["developer"] == all_games:
                found = True
                for key, value in row.items():
                    print(f"{key}: {value}")



        if not found:
            print("No found games with this classification .")

name_developer("games1.csv")