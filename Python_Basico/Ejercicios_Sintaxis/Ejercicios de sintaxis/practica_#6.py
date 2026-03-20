name = str(input("enter your name : "))
age = int(input("enter your age : "))

if (age < 2) :
    print(f"hello{name}  you are a baby" ) 
elif (age < 11):
    print(f"hello {name}  you are a kid" ) 
elif (age < 13) :
    print(f"Hello {name}  you are a pre-teen" ) 
elif (age < 18) :
    print(f"Hello {name}  you are a teen" ) 
elif (age < 30) :
    print(f"Hello {name}  you are a young adult" ) 
elif (age < 50) :
    print(f"Hello {name}  you are a adult" ) 
else :
    print(f"Hello {name} you are a older adult" )




