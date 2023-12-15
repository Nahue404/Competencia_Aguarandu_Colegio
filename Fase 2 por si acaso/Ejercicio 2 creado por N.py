#Ayuda al profe de historia 
#Crea un codigo que de algunas preguntas y evalua si son correctas 
#1. En que fecha se fundo Asunción?, 15 de agosto de 1537
#2. Quien descubrio Paraguay por tierra y por Agua?, Alejo Garcia y Sebastian Caboto
#3. Cuantas Guerras tuvo Paraguay?,2
#4. Cuales son, escribe en orden cronologico?, Guerra del Chaco y Guerra de la Triple Alianza
#5. Cuantos departamentos tiene el Paraguay?, 18 
#6. Cuantos presidentes tuvo el Paraguay hasta ahora?, 50
#Imprime cuantos puntos hizo el alumno y su nombre, sabiendo que cada pregunta valen 3 puntos excepto la 2 pregunta
#Que vale 5 puntos
Nota=0

print("Examen de Historia: ")
Nombre=input("Ingrese su nombre: ")
A=input("En que fecha se fundo Asunción?: ")
if A == "15 de Agosto de 1537":
        Nota += 3
print("ESCRIBIR SUS NOMBRES CON SUS INICIALES EN MAYUSCULAS Y SEPARANDO POR (Y)")
B= input("Quien descubrio Paraguay por tierra y por Agua?: ")
if B =="Alejo Garcia y Sebastian Caboto":
    Nota += 5
print("ESCRIBIR SOLO CON NUMEROS")
C= int(input("Cuantas Guerras tuvo Paraguay?: "))
if C == 2:
    Nota += 3
else:
    print("Muy bien")
print("ESCRIBIR SUS NOMBRES CON SUS INICIALES EN MAYUSCULAS Y SEPARANDO POR (Y)")
print("Ejemplo: Guerra de Tal y Tal")
D=input("Cuales son, escribe en orden cronologico?: ")
if D == "Guerra del Chaco y Guerra de la Triple Alianza":
    Nota += 3
print("ESCRIBIR SOLO CON NUMEROS")
E=input("Cuantos departamentos tiene el Paraguay?: ")
if E == 18:
    Nota += 3
print("ESCRIBIR SOLO CON NUMEROS")
F=input("Cuantos presidentes tuvo el Paraguay hasta ahora?:")
if F == 50:
    Nota += 3
else:
    print("Muy bien")
print("La nota de", Nombre," es", Nota,"de 20")
