time_seconds = int(input("enter the time in seconds : "))

if (time_seconds > 600 ):
    print("is largest")
elif (time_seconds == 600):
    print("is the same")
else :
    missing_seconds = 600 - time_seconds
    print("the missing seconds is the : ",missing_seconds)

