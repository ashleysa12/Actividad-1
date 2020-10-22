# Reto 1
print("Reto #1:")
def funcion1():
	print("Esta es")
	print("la primera función")
	print("del primer reto")

def funcion2():
	x = 10
	y = 5
	z = 1
	print(x, "+(", 5, "*", z, ")=", x + y * z)

def funcion3():
	print("Las siguientes funciones")
	print("se declaran con parametros")

def funcion4(x):
	y = x * 3 * 2 * 1
	print("El factorial de", x, "es:", y)

def funcion5(x, y, z):
	resultado = x ** z - y
	return resultado


funcion1()
print()
funcion2()
print()
funcion3()
print()
funcion4(4)
print()
print("(-5)^2 - 10=", funcion5(-5, 10, 2))
print()


# Reto 2
print("Reto #2:")
nombre=["Isa", "Luis", "Humberto", "Ashley"]
parentesco=["Hija", "Padre", "Hijo", "Madre"]
cedulas=["6.251.892", "25.771.632", "28.116.251", "6.940.249"]
cumpleano=["19/10", "05/07", "05/01", "31/07"]
signo=["Cancer", "Leo", "Capricornio", "Libra"]

print(nombre)
print(parentesco)
print(cedulas)
print(cumpleano)
print(signo)
print()

print("La sra.", nombre[0], "es mi", parentesco[3])
print(cedulas[1], "es la cedula de su", parentesco[2])
print()

print(signo[:2])
print(cumpleano[1:3])