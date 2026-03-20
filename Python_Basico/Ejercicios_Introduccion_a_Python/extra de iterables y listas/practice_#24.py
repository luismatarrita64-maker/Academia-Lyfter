my_list = [9, -1, 0, 2, -3]

smallest = my_list[0]

for number in my_list:
    if number < smallest:
        smallest = number # We'll update if we find a smaller one.

print("the smallest number is ", smallest)

