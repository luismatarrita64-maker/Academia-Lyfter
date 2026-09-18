#Cree una clase de User
#Tenga un atributo de date_of_birth.
#Tenga un property de age.
#Luego cree un decorador para funciones que acepten un User como parámetro 
# que se encargue de revisar si el User es mayor de edad 
# y arroje una excepción de no ser así.

from datetime import date

class User:

    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        year = today.year - self.date_of_birth.year
        
        birthday_this_year = (today.month , today.day)
        birthday = (self.date_of_birth.month,self.date_of_birth.day)

        if birthday > birthday_this_year:
            year -= 1

        return  year

def check_age(func):
            def wrapper(user, *args, **kwargs):
                if user.age < 18:
                    raise ValueError(f"the user is a minor , have {user.age} years")
                return func(user, *args, **kwargs)
            return wrapper

@check_age
def ingresar_sitio(user):
    print(f"welcome, have {user.age} years")


# PRUEBAS
user1 = User(date(2000, 1, 1))  # is older
user2 = User(date(2016, 1, 1))  # is minor

ingresar_sitio(user1) 
ingresar_sitio(user2)