#Cree un decorador que haga print de los parámetros y retorno de la función que decore.

#sintaxis del decorador
def decorator(func):
    def wrapper(*args, **kwargs):

        #codigo antes de ejecutar la funcion original
        print(f"Parameter: {args}, {kwargs}")

        #resultado de la función original
        result = func(*args, **kwargs)

        #codigo despues de ejecutar la función original
        print(f"return: {result}")


        return result
    return wrapper