import random

secret_number = random.randint(1, 10)

riddle = 0

while riddle != secret_number:
    riddle =  int(input("enter one number from 1 to 10 :"))
if (riddle == secret_number):
    print("correct")