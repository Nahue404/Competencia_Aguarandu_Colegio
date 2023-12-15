#Desafio vamos a jugar Ta Te Ti
#Vamos a crear un juego de ta te ti.
#Le pediras al usuario que ingresó, no
#lo complicaremos, tu tarea será solamente llenar
#una lista de listas con "X" o "O".
#Pista:Como estas creando una tabla de dos dimensiones
#Tendras que rellenar primero la lista anidad con tres
#elementos y cuando termines de hacer esto
#recien agregar la lista anidada a tu tabla
#esto lo puedes lograr facilmente con un bucle
#anidado para rellenar tu tabla ten en mente dos factores:
#1.La diferencia entre utilizar el metodo copy() y asignar directamente un valor de una lista
#2.Que al terminar de rellenar tu lista anidada, sus elementos van a seguir alli, asi
#que deberias vaciarlas para volver a rellenar para evitar tener elementos repetidos 

Lista=[]#la lista donde van estar las sublistas o listas anidada tambien llamado tabla
Sublista=[]#Donde se va almacenar las sublistas o lista anidada

for i in range (0,3):#hacemos un bucle que se va ejecutar x3 porque nuestra tabla del juego va ser 3x3 
#Va tener 3 elementos dentro de una lista de 3 sublista
    for j in range(0,3):
        movimiento= input("ingrese su jugada: ")#Donde almacenaremos nuestra jugada
        Sublista.append(movimiento)#agregamos la jugada a la sublista 
    Lista.append(Sublista.copy())#Luego agregamos nuestra sublista a la lista real
    Sublista.clear()#Luego limpiamos nuestra sublista para agregar la siguiente sublista

print("La tabla de ta te ti es:")

print(Lista)
for fila in Lista:#Ahora tenemos que ordenar nuestra tabla haciendo un espacio y salto de pagina 
    for elemento in fila:#Vamos a utilizar el print() y end=" "
        print(elemento, end=" ")
    print()
        
