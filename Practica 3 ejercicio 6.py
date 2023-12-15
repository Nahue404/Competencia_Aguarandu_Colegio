#Crea una función calculadora(x, y, op) que va recibir como
#parametros dos números y qué operación realizar: suma, resta,
#multiplicación o división. Controla que las operaciónes ingresadas sean
#válidas.Utiliza esta función en un bucle while y en cada repetición
#del bucle le dices al usuario que ingrese 0 si quiere algo,o 1 para 
#terminar el juego.
def calculadora(x, y, op):#Nuestra función
    
    if op not in '+-/*':#Usamos not in para comparar varios valores str ingresados
        return 'Operacion invalida, las operaciones soportadas son: "+, -, *, /"!'#utilizamos return ya que esto esta dentro de la función
    if op == '+':
        return(str(x) + '' + op + '' + str(y) + '=' + str(x + y))#Útilizamos str ya que no va resolver si no imprimir 
    if op == '-':
        return(str(x) + '' + op + '' + str(y) + '=' + str(x - y))
    if op == '*':
        return(str(x) + '' + op + '' + str(y) + '=' + str(x * y))
    if op == '/':
        return(str(x) + '' + op + '' + str(y) + '=' + str(x / y))
                
while True:
    e= int(input("Ingresa 0 para calcular algo, 1 para terminar el programa:"))
                
    if e == 0:#Almacenamos los datos para que podamos resolver dentro de la función
        x= int(input("x: "))
        y= int(input("y: "))
        op=input("operación: ")
        print (calculadora(x,y,op))
                    
    elif e == 1:
        print("Adios!")
        break#Cerramos nuestro bucle
