#Escribe un programa para hallar los numeros 
#que son divisibles por 7 y multiplos de 5, en un rango 
#de 1500 y 2700 (inclusivo). Guardar lor numeros dentro 
#de una lista llamada "numeros".
números=[]

for numeros in range(1500,2701):
    if (numeros%7==0) and (numeros%5==0):
        números.append(numeros)
print(números)
