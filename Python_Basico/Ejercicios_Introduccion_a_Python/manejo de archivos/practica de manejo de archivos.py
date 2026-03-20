def open_and_print_file_per_line(superheroes):
	with open('superheroes.txt', 'r') as file:
		for line in file.readlines():
			print(line)

open_and_print_file_per_line('superheroes.txt') 

def sort_alphabetically(superheroes ,sort):
    with open("superheroes.txt" ,'r') as file:
        superheroes = file.readlines()

    superheroes.sort()
    print(superheroes)

    with open('sort.txt','w') as file :
        for line in superheroes:
            file.write(line + "\n")


sort_alphabetically("superheroes.txt", "sort.txt")