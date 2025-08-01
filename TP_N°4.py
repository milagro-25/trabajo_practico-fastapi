"""POO: "Algoritmia y Estructura"


Ejercicio 1: "Fuerza de Manos"

Descripción:
Se modelará un sistema en el que una persona tiene dos manos, cada una con una capacidad de carga máxima. Además, la persona posee una fuerza total, que representa el peso máximo que puede levantar combinando ambas manos.

El objetivo es determinar si una persona puede levantar un objeto de determinado peso usando una o ambas manos.

Requisitos del programa:

Crear una clase Mano

Debe tener un atributo para almacenar el peso máximo que puede sostener.
Debe contener un método para verificar si una mano puede sostener un objeto por sí sola.
Crear una clase Persona

Debe tener dos manos.
Debe tener un atributo que represente su fuerza total (peso máximo que puede levantar sumando ambas manos).
Debe incluir un método que reciba un peso y determine si la persona puede levantarlo con una sola mano o con ambas.
Casos de prueba esperados:

Una persona con suficiente fuerza total y con manos capaces de sostener el objeto, debe poder levantarlo.
Si el objeto es demasiado pesado para una sola mano pero no para ambas juntas, debe levantarlo con ambas manos.
Si el objeto excede la fuerza total de la persona, no podrá levantarlo.
Pista:
Usar POO para estructurar bien las clases y sus relaciones. Definir métodos que permitan tomar decisiones sobre si el objeto puede levantarse o no.
"""

# class Mano():
#     def __init__(self,capacidad_maxima):
#         self.capacidad_maxima = capacidad_maxima

#     def puede_sostener(self, peso):
#         return self.capacidad_maxima >= peso

# class Persona():
#     def __init__(self, fuerza_total, capacidad_mano_izquierda, capacidad_mano_derecha):
#         self.mano_izquierda = Mano(capacidad_mano_izquierda)
#         self.mano_derecha = Mano(capacidad_mano_derecha)
#         self.fuerza_total = fuerza_total

#     def puede_levantar(self, peso):
#         if peso <= self.fuerza_total:
#             if self.mano_izquierda.puede_sostener(peso) or self.mano_derecha.puede_sostener(peso):
#                 if self.mano_izquierda.puede_sostener(peso) and self.mano_derecha.puede_sostener(peso):
#                     return "Puede levantar con una mano"
#                 elif self.mano_izquierda.puede_sostener(peso) or self.mano_derecha.puede_sostener(peso):
#                     return "Puede levantar con una o ambas manos"
                
#             elif (self.mano_izquierda.capacidad_maxima + self.mano_derecha.capacidad_maxima) >= peso:
#                 return "Puede levantar con ambas manos"
#             else:
#                 return "No puede levantar"
#         else:
#             return "No puede levantar"

# persona = Persona(150,50,90)

# peso=int(input("ingrese el numero de kg a levantar(solo ingrese el numero): "))
# print(persona.puede_levantar(peso))

"""
Ejercicio 2: "Sistema de Compra y Envío de Productos"

Descripción:
Se requiere un sistema de compra y venta de productos, donde los usuarios puedan elegir entre diferentes métodos de entrega.

Cada tipo de servicio de entrega tiene sus propias características, como el costo del envío y el tiempo estimado de entrega.

Objetivo:
Diseñar un sistema flexible donde, si en el futuro se agregan nuevos métodos de entrega, no sea necesario modificar el código existente.

Requisitos del programa:

Crear una clase Producto

Debe contener atributos como nombre y precio.
Crear una clase Pedido    

Debe permitir asociar un producto con un método de envío.
Debe poder calcular el costo total sumando el precio del producto y el costo del envío.
Debe poder mostrar el tiempo estimado de entrega según el tipo de envío seleccionado.
Debe implementar un método especial (__str__) que dé formato legible al pedido para su almacenamiento.
Persistencia de datos:

Se debe usar un método estático para registrar los pedidos en un archivo externo.

Puede ser un archivo .txt o .json (a elección del programador).

El método debe recibir un pedido y guardar sus datos utilizando el __str__ o convertirlos a formato adecuado para JSON.


Diferentes tipos de envío

Crear al menos tres métodos de entrega distintos, por ejemplo:
Envío estándar: Económico, pero demora más.
Envío express: Más caro, pero entrega rápida.
Envío personalizado: Puede tener un costo variable dependiendo de la distancia.
Casos de prueba esperados:

Un usuario debe poder elegir el tipo de envío.
El sistema debe calcular el costo total correctamente.
Si en el futuro se agregan nuevos métodos de envío, el código debe seguir funcionando sin cambios.
Pista:
Organizar el código usando clases y herencia para estructurar los distintos tipos de envío. Asegurar que el sistema sea escalable, permitiendo agregar más opciones sin alterar las clases existentes."""

# class Producto:
#     def __init__(self, nombre, precio):
#         self.nombre = nombre
#         self.precio = precio

#     def __str__(self):
#         return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}"

# class Envio:
#     def __init__(self, tipo):
#         self.tipo = tipo

#     def costo_envio(self):
#         raise NotImplementedError("Este método debe ser implementado por las subclases")

#     def tiempo_entrega(self):
#         raise NotImplementedError("Este método debe ser implementado por las subclases")

#     def __str__(self):
#         return f"Tipo de envío: {self.tipo}, Costo: ${self.costo_envio():.2f}, Tiempo: {self.tiempo_entrega()}"

# class EnvioEstandar(Envio):
#     def __init__(self):
#         super().__init__("Estándar")

#     def costo_envio(self):
#         return 5.00

#     def tiempo_entrega(self):
#         return "3-5 días hábiles"

# class EnvioExpress(Envio):
#     def __init__(self):
#         super().__init__("Express")

#     def costo_envio(self):
#         return 15.00

#     def tiempo_entrega(self):
#         return "1-2 días hábiles"

# class EnvioPersonalizado(Envio):
#     def __init__(self, distancia):
#         super().__init__("Personalizado")
#         self.distancia = distancia

#     def costo_envio(self):
#         return self.distancia * 0.50

#     def tiempo_entrega(self):
#         return f"{self.distancia // 100 + 1} días hábiles"

# class Pedido:
#     def __init__(self, producto, envio):
#         self.producto = producto
#         self.envio = envio

#     def costo_total(self):
#         return self.producto.precio + self.envio.costo_envio()

#     def __str__(self):
#         return f"{self.producto}\n{self.envio}\nCosto Total: ${self.costo_total():.2f}"

#     @staticmethod
#     def registrar_pedido(pedido, archivo="pedidos.txt"):
#         with open(archivo, "a") as f:
#             f.write(str(pedido) + "\n---\n")

# print("1-Envío estándar: Económico, pero demora más.")
# print("2-Envío express: Más caro, pero entrega rápida.")
# print("3-Envío personalizado: Puede tener un costo variable dependiendo de la distancia.")
# eleccion=input("ingrese una de las siguientes opciones para seleccionar la forma de envio del producto: ")
# envio = eleccion

# if eleccion == "1":
#     envio=EnvioEstandar()
# elif eleccion == "2":
#     envio=EnvioExpress()
# elif eleccion == "3":
#     envio=EnvioPersonalizado(500)
# else:
#     print("elijio una opcion no disponible")

# producto1 = Producto("Camiseta", 20.00)
# pedido1 = Pedido(producto1, envio)
# print(pedido1)
# Pedido.registrar_pedido(pedido1)

# def cargar_pedidos(archivo="pedidos.txt"):
#     try:
#         with open(archivo, "r") as f:
#             contenido = f.read()
#             pedidos = contenido.split("---\n")
#             for pedido_str in pedidos:
#                 if pedido_str.strip():
#                     print(pedido_str.strip())
#                     print("----")
#     except FileNotFoundError:
#         print("No hay pedidos registrados.")

# cargar_pedidos()
