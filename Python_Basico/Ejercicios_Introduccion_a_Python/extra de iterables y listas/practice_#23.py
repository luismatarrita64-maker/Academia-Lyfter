my_list = [3, 6, 1, -2, 0]
has_negative_or_zero = False
for numbers in my_list:
    if numbers <= 0 :
        print("we have at least one negative number or zero")
        has_negative_or_zero = True
        break
if not has_negative_or_zero  :
            print("all numbers is positive")
