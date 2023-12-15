#Desafio pide al usuario el tamaño para dos listas, 
#luego pide que rellene ambas listas con numeros 
#cualquiera. Luego crea una lista que contenga los 
#numeros que exitan en las dos lista anteriores:
a=[]
b=[]

Tl=int(input("Ingrese el tamaño para las listas a y b:"))

for e in range(1,Tl):
    EA=int(input("Ingrese los números para tu lista:"))
    a.append(EA)

print("Elementos para la lista b")
for e in range(1,Tl):
    EA=int(input("Ingrese los números para tu lista:"))
    b.append(EA)

print("Lista A= ", a)
print("Lista b= ", b)

