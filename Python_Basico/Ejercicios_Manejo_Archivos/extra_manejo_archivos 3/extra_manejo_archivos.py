def convert_to_uppercase(message, capital_letters):
    with open("message.txt", 'r') as file:
        message = file.read()

    message = message.upper()
    print(message)

    with open('capital_letters.txt','w') as file :
        for line in message:
            file.write(line)

convert_to_uppercase("message.txt","capital_letters.txt")
