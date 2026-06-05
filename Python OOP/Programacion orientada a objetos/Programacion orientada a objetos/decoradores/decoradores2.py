#Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números,
#y arroje una excepción de no ser así.

def decorator(func):
    def wrapper(*args, **kwargs):


        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError(f"the parameter  {arg} is not a number")

        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise ValueError(f"the parameter  {key} with value {value} is not a number")


        result = func(*args, **kwargs)

        return result
    return wrapper