#Simular de lanzador de monedas: Crea un programa que simule lanzar una moneda hasta que el usuario elija parar
#Genera aleatoriamente "cara" o "cruz", al final del juego debe mostrar cuantas veces salió cara y cuántas cruz.
from random import randint

def lanzadordemonedas():#Nuestra funcion
    print("Simulador de lanzamiento de moneda")#Para el titulo del simulador
    a,cara,cruz=0,0,0#Asignación múltiple
    while True:#Vamos a poder para el bucle cuando cerramos nuestra función
        tiro=randint(0,1)#Nuestra modulo random va importar radint que va generar numeros al azar de 0 al 1
        a= int(input("ingrese 1 para lanzar la moneda o 0 para terminar el juego: "))
        if a == 1:#Esta condición dice que si queremos lanzar la moneda
            if tiro == 0:#Esta condicion dice que si randint nos genera un número 0 imprima cara
                print("Cara!")
                cara+=1#Almacena el en el contador de cara
            elif tiro == 1:#Esta condición nos ayuda a saber a cuando randint genera 1 y es cruz
                print("Cruz")
                cruz+=1#Almacena el en el contador de cruz
        elif a ==0:#Esta condición dice que si no queremos lanzar la moneda
            print("Fin del juego!\nCaras:", cara, "Cruces:", cruz,)#Nos imprimira cuantas veces salio cara y cruz 
                                 #y el \n es para hacer espacio o tabulación
            return#Para llamar y almacenar valores en a, cara, cruz
lanzadordemonedas()#Cerramos nuestra funcion por ende cerramos nuestro bucle
