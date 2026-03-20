my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

pares = []
for number in my_list:
    if number % 2 == 0:
        pares.append(number)

print("original list :",my_list)
print("list without odd:",pares)