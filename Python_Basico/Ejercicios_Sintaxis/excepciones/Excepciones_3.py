def sum_of_values(list):
    result = []
    for element in my_list :
        try:
            number = float(element)
            result.append(number)
            print(f"{element} ➜  summed correctly")
        except ValueError:
            print(f"The element could not be converted : {element}")

    return result
my_list = ['10', 'apple', '5.5', '3', 'n/a']
result = sum_of_values(list)
add = sum(result)
print(result)
print("Total of the sum is :",add)
