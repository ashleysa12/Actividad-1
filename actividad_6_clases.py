# Reto 3
class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname


class Parents:
    def __init__(self, mother, father):
        self.mother = mother
        self.father = father


class House:
    def __init__(self, model, state):
        self.model = model
        self.state = state


class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color


class Div(object):
    def __init__(self, num, den):
        self.num = num
        self.den = den


user = Person(input("Introduzca su nombre: "),
              input("Introduzca su apellido: "))

print()
parents = Parents(input("Introduzca el nombre de su mamá: "),
                  input("Introduzca el nombre de su papá: "))

house = House("Apartamento", "Caracas")

print()
car = Car(input("Introduzca la marca de su carro: "),
          input("Introduzca el modelo de su carro: "),
          input("Introduzca el color de su carro: "))

numbers = Div(10, 5)
div = numbers.num / numbers.den

print()
print("Bienvenid@", user.name, user.lastname, "!")
print()
print("Las caracteristicas del carro que usted ingreso son: ")
print("Color:", car.color)
print("Marca:", car.brand)
print("Modelo:", car.model)
print()
print(user.name, "vives en un(a)", house.model, "en el estado", house.state)
print()
print(user.name, "tu papá se llama", parents.father,
      "y tu mamá", parents.mother)
print()
print("La división de", numbers.num, "entre", numbers.den, "da:", div)
