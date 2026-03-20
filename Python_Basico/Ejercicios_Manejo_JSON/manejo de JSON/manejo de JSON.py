import json

def add_pokemon(filename, new_pokemon):

    # 1. read archive
    with open(filename, "r") as file:
        data = json.load(file)   
    
    # 2. join new pokemon
    data.append(new_pokemon)
    
    # 3. save the updated file
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


name = input('enter the name :')
typ3 = input("enter the type : ")
hp = input('enter the hp :')
attack = input('enter the attack : ')
defense = input("enter the defense : ")
sp_attack = input('enter the sp attack : ')
sp_defense = input("enter the sp defense : ")
speed = input("enter the speed :")

new  = {
		"name": name,
		"type": typ3,
		"HP": hp,
		"Attack": attack,
		"Defense": defense,
		"Sp. Attack": sp_attack,
		"Sp. Defense": sp_defense ,
		"Speed": speed
	}

add_pokemon("pokemons.json", new)
