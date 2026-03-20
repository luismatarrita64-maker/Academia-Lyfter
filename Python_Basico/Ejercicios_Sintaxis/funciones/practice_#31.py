#def name():
    #my_name = 'john'

#name()


#print(my_name) 

#my_name' is not defined

number = 1 
def change():
    global number
    number = number + 5
    print("inside of de function", number)
    
change()
print('outside of de function', number)


a = 4
b = number
c = a + b
print (c)