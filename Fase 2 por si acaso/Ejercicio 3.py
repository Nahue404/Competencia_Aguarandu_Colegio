#Cuenta la cantidad de vocales en forma independientes 
#que se encuentren dentro de un texto introducido por el usuario.
#Considerar mayusculas y minusculas.
Palabra=input("Ingrese una palabra: ")
Palabra=Palabra.lower()
Cont= 0
for elem in Palabra:
    if elem in "aeiou":
        Cont += 1

print("Hay", Cont, "vocales en tu oración")
