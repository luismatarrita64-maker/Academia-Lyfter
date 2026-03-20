price = int(input("enter  price : "))


if (price < 100) :
    discount = 100 * 0.02
    
else :
   discount = 100 * 0.10

final_price  = price - discount

print("The discount applied is", discount)
print("the final price with discount is the :",final_price)

