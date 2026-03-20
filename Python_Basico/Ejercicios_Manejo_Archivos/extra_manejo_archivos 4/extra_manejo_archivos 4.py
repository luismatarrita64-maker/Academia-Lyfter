def new_registration():
    new_line = input('enter a new text :')

    with open("final_line.txt", 'a')as file :
        file.write(f"new line :\n{new_line} \n")

    return

new_registration()

