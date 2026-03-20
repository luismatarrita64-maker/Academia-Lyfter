import csv


#function for the write csv
def write_csv_file(file_path, data, headers):
    with open(file_path, 'w', encoding='utf-8', newline = '') as file:
        writer = csv.DictWriter(file, headers , delimiter='\t')
        writer.writeheader()
        writer.writerows(data)


#function to enter the games
def menu_games():
	games_list = []
	headers = ('name', 'gender', 'developer', 'classification')

	print("Games Registration")

	n = int(input('Enter the number of the games : '))

	for i in range(n):
		print(f"Video Game {i+1}")
		
		name = input('enter the name : ')
		gender = input('enter the gender : ')
		developer = input('enter the developer : ')
		classification = input('enter the classification : ')

		game = {'name' : name,
			'gender'  : gender,
			'developer' : developer,
			'classification': classification,}

		games_list.append(game)

	write_csv_file('Games1.csv', games_list, headers)
	print('CSV created correctly')


menu_games()
