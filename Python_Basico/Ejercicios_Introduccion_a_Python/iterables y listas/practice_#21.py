numbers = []   # Empty list to store the numbers
counter = 0    # Counter

while True:
    num = int(input("Enter one number : "))  # ask for the number
    numbers.append(num) # add it to the list
    counter += 1 # sum counter

    if counter == 10: # if counter = 10 exit

        break

# show full list
print("the enter numbers is : ", numbers)

# show the largest number
print("the largest number is :", max(numbers))