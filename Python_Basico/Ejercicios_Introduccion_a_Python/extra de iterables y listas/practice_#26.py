words = []


for i in range(5):
    word = input(f"enter five word {i + 1} : ")
    words.append(word)

largest_words = []

for word in words:

    if len(word) > 4 :
        largest_words.append(word)

print("the words more larges is",largest_words)