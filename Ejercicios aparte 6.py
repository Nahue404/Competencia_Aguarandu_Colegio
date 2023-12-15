#Desafio pide al usuario el tamaño para dos listas, 
#luego pide que rellene ambas listas con numeros cualquiera. 
#Luego crea una lista que contenga los numeros que exitan en las dos lista anteriores:
T=int(input("Ingrese el tamaño para la lista A y B: "))
A=[]
B=[]
for elem in range(0, T):
    E=input("Ingrese el elementos de tu lista A: ")
    A.append(E)
print("Lista A=", A)
for elem in range(0, T):
    E=input("Ingrese el elemento de tu lista B: ")
    B.append(E)
print("Lista B=", B)

C= set (A) & set (B)

print("Los elemento existentes entre las dos listas son:", C)


