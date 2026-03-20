my_list = [10, 20, 30, 40, 50]
total = 0

for number in my_list :
    total += number

average = total/len(my_list)
print(f"total average is : {average}")

for number in my_list :
    if number > 30 :
        print("older_average :",number)
        