numbers = (input("Enter several numbers separated by spaces :"))
list_of_numbers = list(map(int , numbers.split()))

num_to_count = int(input("what number to count ?"))

counter = list_of_numbers.count(num_to_count)
print(f"the list of numbers is : {list_of_numbers}")

print(f"the number {num_to_count} is repeat {counter}")
    