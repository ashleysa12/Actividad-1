# Reto 1, programa 1
student = (28116251, 25771632, 6251892, 29407774)
print("Las cédulas de los estuadiantes son: ", student)
print()

newlist = list(student)
newlist.append(6251892)
print("Se agrego un nuevo alumno, la lista queda de la siguiente manera,: ",
       newlist)
print()

newlist.remove(29407774)
print("Se retiro un alumno, la lista queda de la siguiente manera,: ",
       newlist)
print()

student = tuple(newlist)
print("La tupla tiene", len(student), "elementos")
print()

element = int(input("Introduzca la cedula que quiera buscar: "))
print("La busqueda es: ", element in student)

print("La palabra introducida aparece: ", student.count(element))
print()

tuple_2 = ("Ashley")
print("La tupla unitaria tiene un elemento llamado", tuple_2)
