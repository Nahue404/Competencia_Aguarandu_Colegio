#La pizzeria Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza
#aparecen a continuación.
#Ingredientes vegetarianos: Pímiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en funcion de su respuesta le muestre un ménu
#con los ingredientes disponibles para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
#Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
 
print("Bienvenido a la pizzeria Bella Napoli!")
print("Que tipo de pizza quieres?")
print("(1) Vegetariana y (2) no vegetariana")
print("ejemplo: 1 o 2")
Tp=int(input("Ingrese tipo de Pizza:"))#Tipo de Pizza
#Deciciones de que tipo de Pizza y ingredientes
if Tp == 1:
	print("Los ingredientes que puedes poner a la pizza son:")
	print("(1)Pimiento y (2)Tofu")
	I=int(input("Solo puedes ingresar un ingrediente:"))#Ingredientes
	if I == 1:
		print("La pizza es Vegetariana y lleva de ingredientes mozarella, tomate y Pimiento")
	else:
		print("La pizza es Vegetariana y lleva de ingredientes mozarella, tomate y Tofu")
else:
	print("Los ingredientes que puedes poner a la pizza son:")
	print("(1)Peperoni, (2)Jamón, (3)Salmón")
	I=int(input("Solo puedes ingresar un ingrediente:"))#Ingredientes
	if I == 1:
		print("La pizza no es Vegetariana y lleva de ingredientes mozarella, tomate y Peperoni")
	elif I == 2:
		print("La pizza no es Vegetariana y lleva de ingredientes mozarella, tomate y Jamón")
	else:
		print("La pizza no es Vegetariana y lleva de ingredientes mozarella, tomate y Salmón")

print("Gracias por utilizar los servicios de Pizzeria Bella Napoli!")