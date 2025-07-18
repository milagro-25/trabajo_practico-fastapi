"""Ejercicio 1: Calculadora de Descuentos
 Crea una función que calcule el precio final de un producto después de aplicar 
un descuento.
 Requisitos:
 La función debe recibir el precio original y el porcentaje de descuento.
 Debe retornar el c después del descuento.
 Incluye un docstring que describa la función, sus parámetros y el valor de 
retorno"""

# def calculadora():

#     """
#     Calcula el precio final de un producto después de aplicar un descuento.

#     Esta función solicita al usuario el precio original del producto y el porcentaje de descuento a aplicar.
#     Luego, calcula y muestra el precio final con el descuento aplicado.

#     """

#     precio_original=int(input("ingrese el precio para hacer el descuento: $"))
#     porcentaje_descuento=int(input(f"ingrese el numero del porcentaje para hacer el descuento: %"))
#     precio_final=(precio_original*porcentaje_descuento)/100
#     print(f"El precio final del descuento es de {precio_final}%")

# calculadora()


"""Ejercicio 2: Conversión de Temperaturas
 Crea una función que convierta temperaturas de Celsius a Fahrenheit o 
viceversa.
 Requisitos:
 La función debe recibir la temperatura, la unidad de origen y la unidad de 
destino.
 Debe retornar la temperatura convertida.
 Incluye ejemplos de uso en el docstring."""

# def conversión_temperaturas():

#     """
#     Convierte temperaturas entre grados Celsius y Fahrenheit.

#     Esta función solicita al usuario la temperatura y las unidades de origen y destino,
#     luego realiza la conversión y muestra el resultado.

#     Ejemplo:
#     Si el usuario ingresa 40 como temperatura, °C como unidad de origen y °F como unidad de destino,
#     la función calculará 40 * 9/5 + 32 = 104 y mostrará "La respuesta es: 104°F".
#     """

#     temperatura=int(input("ingrese el numero de la temperatura: "))
#     unidad_de_origen=input("ingrese la unidad de origen: ")
#     unidad_de_destino=input("ingrese la unidad de destino: ")
    
#     if unidad_de_origen== "°C" and unidad_de_destino == "°F":
#         respuesta=int(temperatura*9/5)
#         respuesta=respuesta+32
#         print(f"La respuesta es: {respuesta}{unidad_de_destino}")

#     elif unidad_de_origen == "°F" and unidad_de_destino == "°C":
#         respuesta=int(temperatura-32)
#         respuesta=respuesta/(9/5)
#         print(f"La respuesta es: {respuesta}{unidad_de_destino}")

#     else:
#         print("No se pudo procesar la informacion")
#         pass

# conversión_temperaturas()

""" Ejercicio 3: Verificación de Palíndromos
 Escribe una función que determine si una palabra o frase es un palíndromo.
 Requisitos:
 La función debe recibir una cadena de texto.
 Debe retornar 
True si es un palíndromo y 
False en caso contrario."""

# def palindromo(texto):
    
#     """
#     La funcion verifica si una palabra o frase es un palíndromo.

#     Args:
#       texto: La cadena de texto a verificar.

#     Returns:
#       True si es un palíndromo, False en caso contrario.
#     """

#     texto = texto.lower()  # Convertir a minúsculas para ignorar mayúsculas/minúsculas
#     texto_sin_espacios = texto.replace(" ", "")  # Eliminar espacios
#     texto_analizado=texto_sin_espacios == texto_sin_espacios[::-1]
#     if texto_analizado == True:
#         texto_analizado="es palíndromo = True"
#         print(f"El texto {texto}: {texto_analizado}")
#     else:
#         texto_analizado="no es palíndromo = False"
#         print(f"El texto {texto}: {texto_analizado}")

# texto=input("ingrese un texto para determinar si es palíndromo o no: ")
# palindromo(texto)

""" Ejercicio 4: Análisis de Texto
Crea una función que cuente la cantidad de palabras y caracteres en un texto.
 Requisitos:
 La función debe recibir una cadena de texto.
 Debe retornar un diccionario con la cantidad de palabras y caracteres.
 Documenta claramente la estructura del diccionario en el docstring."""

# def analizar_texto(texto):

#     """
#     La funcion analiza un texto y devuelve un diccionario con la cantidad de palabras y caracteres.

#     Args:
#     texto: La cadena de texto a analizar.

#     Returns:
#     Un diccionario con la siguiente estructura:
#     {
#         "palabras": int,  # Número de palabras en el texto
#         "caracteres": int # Número de caracteres en el texto (incluyendo espacios)
#     }
#     """
#     palabras=texto.split()
#     num_palabras=len(palabras)
#     num_caracteres=len(texto)
#     analizis={"palabras": num_palabras, "caracteres": num_caracteres}
#     print(analizis)

# texto=str(input("ingrese un texto o frase para contar la cantidad de palabras y letas: ")) 
# analizar_texto(texto)

"""Ejercicio 5: Generador de Números Primos
 Escribe una función que genere una lista de números primos hasta un número 
dado.
 Requisitos:
 La función debe recibir un número entero positivo.
 Debe retornar una lista con todos los números primos hasta ese número.
 Incluye en el docstring una explicación sobre qué es un número primo."""

# def es_primo(numero):

#     """
#     Esta funcion verifica si un número es primo o no.

#     Un número primo es un número natural mayor que 1 que tiene
#     exactamente dos divisores distintos: 1 y el propio número.

#     """

#     if numero <=1:
#         return False
#     for divisor in range(2,numero):
#         if numero%divisor==0:
#             return False
#     return True

# def listaprimos(numero1,numero2):

#     """
#     Genera una lista de números primos dentro de un rango dado.

#     parametros a utilizar:
#     numero1: El límite inferior del rango.
#     numero2: El límite superior del rango.

#   """
#     lista=[]
#     for numero in range(numero1,numero2+1):
#         if es_primo(numero):
#             lista.append(numero)
#     print(lista)

# print("ingrese un numero entero positivo para retornar todos los numeros primos hasta ese numero:")
# num=int(input("ingrese el numero: "))
# listaprimos(1,num)

""" Ejercicio 6: Gestión de Inventario
Crea una función que actualice el inventario de una tienda.
Requisitos:
La función debe recibir un diccionario representando el inventario y una 
lista de productos vendidos.
Debe actualizar las cantidades en el inventario y retornar el inventario 
actualizado.
Incluye en el docstring un ejemplo de entrada y salida"""

# def actualizar_inventario(inventario, productos_vendidos):

#     """
#     Actualiza el inventario de una tienda después de ventas.

#     Args:
#     inventario: Un diccionario donde las claves son nombres de productos
#                        y los valores son sus cantidades.
#     productos_vendidos: Una lista de nombres de productos vendidos.

#     Returns:
#     dict: El inventario actualizado con las cantidades restadas.
#     """ 

#     for producto in productos_vendidos:
#         if producto in inventario:
#             inventario[producto] -= 1
#             print(f"inventario actualizado: {inventario}")

# inventario = { "frutas":{"manzanas":10,"bananas": 10,"naranjas":10,"mandarinas":10},
#             "verduras":{"tomate":10,"papa":10,"cebolla":10,"zanahoria":10},
#             "carnes":{"milanesa":10,"asado":10,"hamburgesas":10,"salchichas":10},
#             "lacteos":{"leche":10,"queso cremoso":10,"yougur entero":10,"mantequilla":10},
#             "para el desayuno":{"cafe":10,"cocoa":10,"leche en polvo":10,"té":10}}
# print(inventario)
# for llave in inventario:
#     print(llave)
# nombre=input("ingrese el nombre del area para ver sus productos: ")
# print(inventario[nombre])
# productos_a_comprar =["bananas","mandarinas","asado"]
# print(f"va a comprar: {productos_a_comprar}")
# actualizar_inventario(inventario[nombre], productos_a_comprar)

"""Ejercicio 7: Validación de Contraseñas
 Escriba un programa de  Python para convertir una lista de string en una nueva 
lista con listas de caracteres utilizando map.
 Requisitos:
 input : ["hola","adios"]
 output: [["h","o","l","a"] , ["a","d","i","o","s"]]"""

# def convertir_a_listas_de_caracteres(lista_original):

#     """
#     Convierte una lista de cadenas en una nueva lista con listas de caracteres.
#     devuelve:
#     Una nueva lista donde cada elemento es una lista de caracteres de la cadena
#     correspondiente.
#     """
#     lista_convertida=list(map(list, lista_original))
#     print(f"Lista original: {lista_original}")
#     print(f"Lista convertida: {lista_convertida}")

# lista_original=["hola", "mundo"]
# convertir_a_listas_de_caracteres(lista_original)

"""Ejercicio 8: Cálculo de Estadísticas
Crea una función que calcule la media, mediana y moda de una lista de 
números.
Requisitos:
La función debe recibir una lista de números.
Debe retornar un diccionario con la media, mediana y moda.
Incluye en el docstring una explicación de cada estadística y un ejemplo de 
uso."""

# def calcular_estadisticas(lista_numeros):
    
#     """
#     Calcula la media, mediana y moda de una lista de números.

#     Args:
#     lista_numeros: Una lista de números.

#     # Para calcular la media: primero se suman todos los numeros 
#     # y luego se lo divide por la cantidad de numeros que habia en la lista
    
#     # Para calcular la mediana: primero se determina si la longitud de la lista es par o impar.
#     # Si la longitud es par, la mediana es el promedio de los dos valores centrales que se encuentren en el medio de la lista.
#     # Si la longitud es impar, la mediana es el valor que se encuentre en el medio de la lista.

#     # Para calcular la moda: Primero se crea un diccionario para almacenar la frecuencia de cada número en la lista.
#     # Luego se cuenta cuántas veces aparece cada número guardando esa información en el diccionario.
#     # por ultimo se busca el número con la mayor frecuencia siendo ese la moda.

#     # ejemplo
#     # si la lista es: [2,1,3,3,4,4,4]
#     # va a retornar: {'media': 3.0, 'mediana': 3, 'moda': 4}
#     """
#     # Media
#     media=sum(lista_numeros)/len(lista_numeros)

#     # Mediana
#     lista_ordenada=sorted(lista_numeros)
#     cantidad_numeros=len(lista_ordenada)
#     if cantidad_numeros % 2 == 0:
#         mediana = (lista_ordenada[cantidad_numeros//2 - 1] + lista_ordenada[cantidad_numeros//2]) / 2
#     else:
#         mediana = lista_ordenada[cantidad_numeros//2]

#     # Moda
#     frecuencias = {}
#     for numero in lista_numeros:
#         frecuencias[numero] = frecuencias.get(numero, 0) + 1

#     moda=None
#     max_frecuencia = 0
#     for numero, frecuencia in frecuencias.items():
#         if frecuencia > max_frecuencia:
#             moda = numero
#             max_frecuencia = frecuencia

#     estadistica={'media': media, 'mediana': mediana, 'moda': moda}
#     print(estadistica)

# lista_numeros=[2,1,3,3,4,4,4]
# calcular_estadisticas(lista_numeros)

