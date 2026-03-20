def capital_letter(text):
    lower = 0 
    capital = 0 

    for letter in text :
        if letter.isupper():
            capital += 1

        elif letter.islower():
            lower +=1

    print(f"letter capital is : {capital}")
    print(f"the number of lower letter is : {lower}")

capital_letter('Hello Word , My name is Felipe')

    
