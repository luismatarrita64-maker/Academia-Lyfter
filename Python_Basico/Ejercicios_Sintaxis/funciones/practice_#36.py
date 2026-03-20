import math

def prime_numbers(list_of_numbers):
    primos = []
    
    for n in list_of_numbers:
        if n <= 1:
            continue  

        es_primo = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                es_primo = False
                break

        if es_primo:
            primos.append(n)
    
    return primos

# 👇
list_of_numbers = [1, 4, 6, 7, 13, 9, 67]
print(prime_numbers(list_of_numbers))

