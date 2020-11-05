# Reto 2: Teclado y Casting
client = str(input("Ingrese su nombre: "))
produc1 = float(input("Ingrese el precio del primer producto: "))
produc2 = float(input("Ingrese el precio del segundo producto: "))
produc3 = float(input("Ingrese el precio del tercer producto: "))

total = produc1 + produc2 + produc3
iva = total * 0.16
pay = total + iva
us = pay / 524000

print()
print("Primer producto .... ", produc1)
print("Segundo producto ... ", produc2)
print("Tercer producto .... ", produc3)
print("IVA (16%)       .... {0:.2f}".format(iva))
print("Total a pagar ------ {0:.2f}".format(pay))
print()
print("Hola ", client, ", deseas pagar en $?: ")
op = int(input("Si (1)    No(0)"))
print()

if (op == 1):
    print("El tipo de cambio es de 524.000")
    print("Debe pagar {0:.2f} = {0:.0f}$".format(us))
    print("Gracias por su compra!")
elif (op == 0):
    print("La cajera procedera a pasar su tarjeta")
    print("Gracias por su compra!")
else:
    print("Opción no permitida.")
