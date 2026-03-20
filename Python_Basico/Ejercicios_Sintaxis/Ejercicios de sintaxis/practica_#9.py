n = int(input("How many grades does the student have? "))
approved_counter = 0
counter_disapproved = 0
total_add = 0
approved_sum = 0
unapproved_sum = 0


for i  in range(n) :
    note = int(input("enter note : "))
    total_add += note
    if note >= 70 :
        approved_counter = approved_counter + 1
        approved_sum += note
    else :
        counter_disapproved += 1
        unapproved_sum+= note

total_average = total_add / n
if approved_counter > 0 :
    average_passed = approved_sum / approved_counter
else :
    average_passed = 0
if counter_disapproved > 0:
    average_failed = unapproved_sum / counter_disapproved
else :
    average_failed = 0

print("\n--- Results ---")
print("Approved notes:", approved_counter)
print("Failing grades:", counter_disapproved)
print("total average :", total_average)
print("average passed", average_passed)
print("average failed :",average_failed) 