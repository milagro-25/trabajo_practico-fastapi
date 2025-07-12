"""punto 1
 Crea una función que reciba una lista de números y la ordene de menor a 
mayor. La función debe devolver la lista ordenada Debe usar set)."""

# def lista_de_numeros(numeros):
 
#   conjunto_de_N = set(numeros)  # Convertir la lista a un set para eliminar duplicados
#   lista_ordenada = sorted(conjunto_de_N)  # Convertir el set a una lista y ordenar
#   return lista_ordenada

# numeros = [3,2,1,6]
# print(f"lista de numeros: {numeros}")
# numeros_ordenados = lista_de_numeros(numeros)
# print(f"lista de numeros ordenada{numeros_ordenados}")

"""punto 2
Crea un programa que permita crear un conjunto desde cero y después me 
permita eliminar un elemento de un conjunto si está presente en el conjunto."""

# def modificador_de_conjunto():

#     conjunto = set() 

#     while True:
#         elemento = input("Ingrese un elemento para agregar al conjunto (ingrese: 'fin' para terminar de agregar elementos): ")
#         if elemento == 'fin':
#             break
#         conjunto.add(elemento)
#     print(f"Conjunto creado: {conjunto}")
    
#     if conjunto:
#         elemento_a_eliminar = input("Ingrese un elemento para eliminar del conjunto: ")
#         if elemento_a_eliminar in conjunto:
#             conjunto.remove(elemento_a_eliminar)
#             print(f"Elemento '{elemento_a_eliminar}' eliminado.")
#         else:
#             print(f"El elemento '{elemento_a_eliminar}' no se encuentra en el conjunto.")
#     else:
#         print("El conjunto está vacío, no se puede eliminar ningún elemento.")
        
# modificador_de_conjunto()

"""punto 3
 Dados dos conjuntos de números, escribe un programa  para encontrar los 
números que faltan en el segundo conjunto en comparación con el primero y 
viceversa."""

# def comparar_los_conjuntos(conjunto1, conjunto2):

#     diferencia_1 = conjunto1 - conjunto2
#     diferencia_2 = conjunto2 - conjunto1
#     return diferencia_1, diferencia_2

# conjunto_1 = {1, 2, 3, 4, 5,6,88}
# conjunto_2 = {4, 5, 6,5,7,50, 7, 8}
# faltantes_a, faltantes_b = comparar_los_conjuntos(conjunto_1, conjunto_2)
# print(f"Números en A pero no en B: {faltantes_a}")
# print(f"Números en B pero no en A: {faltantes_b}")

"""punto4
Escriba un programa en Python para eliminar todos los duplicados de una 
lista de cadenas dada y devolver una lista de cadenas  únicas. """

# def eliminar_duplicados_con_orden(lista_cadenas):
 
#     elementos_vistos = set()
#     lista_sin_duplicados = []
#     for elemento in lista_cadenas:
#         if elemento not in elementos_vistos:
#             lista_sin_duplicados.append(elemento)
#             elementos_vistos.add(elemento)
#     return lista_sin_duplicados

# lista_cadenas = ["a","b","c","c","d"]
# print(f"con duplicado: {lista_cadenas}")
# lista_sin_duplicados = eliminar_duplicados_con_orden(lista_cadenas)
# print(f"sin duplicados: {lista_sin_duplicados}")

"""punto 5
Crea una función llamada 
factorial que reciba un número entero positivo y 
devuelva su factorial. Ejemplo: 
factorial(4) debe devolver 24."""

# def factorial():
#     numero = int(input("ingrese un numero para ver su factorial: "))
#     factorial = 1
#     if factorial != 0:
#         for i in range(1,numero+1):
#             factorial=factorial*i
#     print(f"factorial: {factorial}")

# factorial()
 
"""punto 6
Crea una función llamada 
fibonacci(n) que reciba como parámetro un número 
entero n y devuelva una lista con los primeros n números de la serie de 
Fibonacci. La serie de Fibonacci es una secuencia en la que cada número se 
obtiene sumando los dos anteriores. Comienza así: Ejemplo:
 fibonacci(5)
 # Salida esperada: [0, 1, 1, 2, 3]"""

# def fibonacci(numero):
#     for i in range(1,numero+1):
#         if numero != i:
#             numero=numero + i
#             return numero
#         else:
#             return numero

# numero= int(input("coloque un numero para obtener una serie de fibonacci: "))
# respuesta=fibonacci(numero)
# print(f"la fibonacci es: {respuesta}")

"""punto 7
Crea una función recursiva llamada 
suma_recursiva que reciba un número 
devuelva la suma de los primeros n números naturales. Ejemplo: 
suma_recursiva(5) debe devolver 15 (1+2+3+4+5)."""

# def suma_recursiva(numero):
  
#   if numero <= 1:
#     return numero
#   else:
#     return numero + suma_recursiva(numero - 1)

# numero = int(input("ingrese un numero para ver la suma de los primeros numeros naturales: "))
# resultado = suma_recursiva(numero)
# print(f"El resultado de la operacion es: {resultado}")

"""punto 8
Crea una clase 
Libro con los atributos 
titulo , 
autor y 
año_publicacion . Luego, crea 
una subclase llamada 
LibroDigital que tenga un atributo adicional"""

# class Libro ():
#     def __init__(self,titulo="desconocido",autor="desconocido",año_publicacion="desconocoido"):
#         self.titulo=titulo
#         self.autor=autor
#         self.año_publicacion=año_publicacion

#     def info_del_libro(self):
#         print("--------------Informacion del libro-------------")
#         print(f"el titulo del libro es: {self.titulo}")
#         print(f"el autor es: {self.autor}")
#         print(f"en que año se publico el libro: {self.año_publicacion}")

# libro=Libro("Angeles","marco antonio",1988)
# libro.info_del_libro()

# class LibroDigital(Libro):
#     def __init__(self,titulo="desconocido",autor="desconocido",año_publicacion="desconocoido",n_de_pag="desconocido"):
#         super().__init__(titulo,autor,año_publicacion)
#         self.n_de_pag=n_de_pag

#     def info_del_libro(self):
#         print("--------------Informacion del libro-------------")
#         print(f"el titulo del libro es: {self.titulo}")
#         print(f"el autor es: {self.autor}")
#         print(f"en que año se publico el libro: {self.año_publicacion}")
#         print(f"el numero de paginas es de: {self.n_de_pag}")

# libro_digit=LibroDigital(autor="link moldes",año_publicacion=2022,)
# libro_digit.info_del_libro()

"""punto 9
Dado un texto con información estructurada, escribí un programa que 
extraiga los datos usando slicing y los devuelva como un diccionario.
 A partir de un texto como el siguiente, la funcion deberia retornar el siguiente 
diccionario:
text = "Nombre: Juan Pérez | Edad: 30 | Ciudad: Salta"
 slicing_function(text) # {"nombre": "Juan Perez", "edad"  30, "ciudad": "Salta"}"""

