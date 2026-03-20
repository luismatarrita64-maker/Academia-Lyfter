def text_character(text,character):
    counter = 0
    for letter in text :
        if letter == character :
            counter += 1
    return counter
text = input('enter the text :')
character = input('enter the character to search :')


amount = text_character(text,character)
print(f"has been found : {amount} character")

