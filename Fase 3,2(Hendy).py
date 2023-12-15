#Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra 
#que contiene y su frecuencia. Escribir otra funcion que reciba el diccionario generado 
#con la funcion que reciba el diccionario generado con la funcion anterior y devuelva una tupla 
#con la palabra más repetida y su frecuencia.

def contar_frecuencia_palabras(cadena):
    # Dividir la cadena en palabras
    palabras = cadena.split()

    # Crear un diccionario para almacenar la frecuencia de cada palabra
    frecuencia_palabras = {}
    
    # Contar la frecuencia de cada palabra
    for palabra in palabras:
        # Eliminar posibles signos de puntuación alrededor de la palabra
        palabra = palabra.strip('.,!?()[]{}":;')

        # Convertir la palabra a minúsculas para evitar contar la misma palabra en mayúsculas y minúsculas como diferentes
        palabra = palabra.lower()

        # Incrementar la frecuencia de la palabra en el diccionario
        frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1

    return frecuencia_palabras

def palabra_mas_repetida(diccionario_frecuencia):
    # Encontrar la palabra con la frecuencia máxima
    palabra_max_frecuencia = max(diccionario_frecuencia, key=diccionario_frecuencia.get)
    
    # Obtener la frecuencia de la palabra máxima
    frecuencia_max = diccionario_frecuencia[palabra_max_frecuencia]

    return (palabra_max_frecuencia, frecuencia_max)

# Ejemplo de uso
cadena_ejemplo = "Esta es una cadena de ejemplo. Esta cadena contiene palabras repetidas, palabras únicas y algunas palabras con signos de puntuación."
diccionario_frecuencia = contar_frecuencia_palabras(cadena_ejemplo)
palabra_max_frecuencia = palabra_mas_repetida(diccionario_frecuencia)

print("Diccionario de frecuencias:", diccionario_frecuencia)
print("Palabra más repetida:", palabra_max_frecuencia)
