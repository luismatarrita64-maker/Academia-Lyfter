def information():
    name = (input("Enter your name :"))
    if name.isdigit():
        print('The name it cannot be a number' )
        return
    
        
    try:
            
        age = int(input('Enter your age :'))
    except ValueError:
            print("Invalid age , age can't be a word")
            return

    print(f"Hello {name} , your age is {age}")

information()