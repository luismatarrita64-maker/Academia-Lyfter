number = int(input("enter one number from 1 to 10 :"))

print("table of ", number)

for i in range(1,13):
    result = number * i
    print(number,"x",i,"=", result)