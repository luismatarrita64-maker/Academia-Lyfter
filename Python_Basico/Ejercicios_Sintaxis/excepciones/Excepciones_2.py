def convert_to_integer(list):
    result = []
    for element in list:
        try :
            number = int(element)
            result.append(number)
        except ValueError:
            print(f"The element could not be converted ➜  {element}")

    return result
list = ['4', 'hola', '10', '5.2']
result = convert_to_integer(list)
print(result)

