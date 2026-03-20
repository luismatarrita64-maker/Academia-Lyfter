def number_of_vowels(word):
    counter = 0
    vowels = ['a','e','i','o','u']
    for letter in word:
        if letter in vowels :
            counter += 1
    return counter
word = input('enter the word :')
result = number_of_vowels(word)
print('the number of vowels is', result)
