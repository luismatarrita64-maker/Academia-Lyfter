numbers = ['1', '2', '3', '4']


for index in range(len(numbers)):
   
    if index == 0:
        first = numbers[index]

    elif index == len(numbers) - 1:
        last = numbers[index]
      
        numbers[0] = last
        numbers[index] = first

print(numbers)
