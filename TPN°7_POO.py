"""punto 1
Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área 
del rectángulo."""

# class Rectángulo():
#     def __init__(self,base,altura):
#         self.base=base
#         self.altura=altura
#     def Area_del_Rectángulo(self):
#         Area=self.base*self.altura
#         print(f"El Área del rectangulo es {Area}")

# base=int(input("ingrese la base o ancho del rectángulo: "))
# altura=int(input("ingrese la altura del rectángulo: "))

# rectangulo=Rectángulo(base,altura)

# rectangulo.Area_del_Rectángulo()

"""punto 2
Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina. La clase debe contener 
como miembros: 
o Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número). 
o Un atributo para el estado (lleno o vacío). 
o Un atributo n, que indica la cantidad máxima de cebadas. 
o Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una 
excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste! 
o Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, se 
debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío! 
o Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. En ese caso la cantidad 
de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso: 
“Advertencia: el mate está lavado.” pero no se debe lanzar una excepción."""

# class Mate():
#     def __init__(self):
#         self.C_de_Cebadas=15
#         self.Estado_del_Mate=True
#         self.C_Maximas_Cebadas=15
    
#     def cebar(self):
#         if self.Estado_del_Mate:
#             print("Llenaste el mate con agua")
#             self.Estado_del_Mate=False
#         else:
#             print("¡Cuidado! ¡Te quemaste!")

#     def beber(self):
#         if self.Estado_del_Mate==False:
#             print("bbsshshsss")
#             self.Estado_del_Mate=True
#             self.C_de_Cebadas=self.C_de_Cebadas-1
#             if self.C_de_Cebadas==0:
#                 print("Advertencia: el mate está lavado")
#         else:
#             print("¡El mate está vacío!")

# mate=Mate()

# mate.cebar()
# mate.beber()

"""punto 3 
Botella y Sacacorchos 
 Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega). 
 Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, o None si está 
destapada. 
 Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque el corcho y se guarde 
una referencia al corcho sacado. Debe lanzar una excepción en el caso en que la botella ya esté destapada, o si el 
sacacorchos ya contiene un corcho. 
 Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el caso en el que no haya 
un corcho."""

# class Corcho():
#        def __init__(self,bodega):
#         self.bodega=bodega

# class Botella():
#     def __init__(self,corcho=True):
#         self.corcho=corcho

# class Sacacorchos(Botella):
#     def __init__(self,corcho):
#         super().__init__(corcho)

#     def Destapar(self):
#         if corcho==True:
#             print("El corcho fue sacado")
#             corcho=False
#         elif corcho==False:
#             print("¡La botella no tiene corcho!")
        
#     def Limpiar_El_Sacacorcho(self):
#             pass

# saca=Sacacorchos()
# saca.Destapar()

"""punto 4
Una heladería es un tipo especial de restaurante. Cree una clase Restaurante, cuyo método __init__() guarde dos atributos: 
restaurante_nombre y tipo_comida. Cree un método describir_restaurante() que muestre estas piezas de información, y un 
método abrir_restaurante() que muestre un mensaje indicando que el restaurante ahora está abierto. Luego cree una clase 
Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado sabores que almacene una lista de los 
sabores de helado disponibles. Escriba también un método que muestre estos valores, cree una instancia de la clase y llame 
al método."""

# class Restaurante():
#     def __init__(self,restaurante_nombre,tipo_comida):
#         self.restaurante_nombre=restaurante_nombre
#         self.tipo_comida=tipo_comida

#     def describir_restaurante(self):
#         print(f"Bienvenidos al restaurante {self.restaurante_nombre}.")
#         print("----------------------------------------------------------")
#         print("donde el tipo de comida es:")
#         print(self.tipo_comida)

#     def abrir_restaurante(self):
#         print("El restaurante esta abierto:")

# class Heladeria(Restaurante):
#     def __init__(self,restaurante_nombre,tipo_comida,sabores="chocolate\nvainilla\nfrutilla"):
#         super().__init__(restaurante_nombre,tipo_comida)
#         self.sabores=sabores

#     def lista_sabores(self):
#         print("la lista de sabores es:")
#         print(self.sabores)

# hel=Heladeria("heladeria de helados","helados")
# hel.abrir_restaurante()
# hel.describir_restaurante()
# hel.lista_sabores()

"""punto 5
Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, y los métodos recibir_ataque, que 
reduzca la vida según una cantidad recibida y lance una excepción si la vida pasa a ser menor o igual que cero, y mover 
que reciba una dirección y se mueva en esa dirección la cantidad indicada por velocidad. 
 Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método atacar, que reciba otro 
personaje, al que le debe hacer el daño indicado por el atributo ataque. 
 Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método cosechar, que 
devuelva la cantidad cosechada"""



"""punto 6
Usuarios: Cree una clase Usuario. Cree también dos atributos nombre y apellido, así como otros atributos que típicamente 
se guardan en un perfil de usuario. Escriba un método describir_usuario() que muestre un resumen de la información del 
usuario. Escriba otro método saludar_usuario() que muestre un saludo personalizado al usuario. 
Cree varias instancias que representen distintos usuarios y llame ambos métodos para cada uno."""

# class Usuario():
#     def __init__(self,nombre,apellido,edad,genero):
#         self.nombre=nombre
#         self.apellido=apellido
#         self.edad=edad
#         self.genero=genero

#     def describir_usuario(self):
#         print(f"El nombre del usuario es: {self.nombre}")
#         print(f"El apellido del usuario es: {self.apellido}")
#         print(f"La edad del usuario es: {self.edad}")
#         print(f"El genero del usuario es: {self.genero}")
#         print("----------------------------------------------")

#     def saludar_usuario(self):
#         print(f"Hola {self.nombre} buenos dias, tardes, noches espero que estes bien!!")
#         print("----------------------------------------------")

# usuario_1=Usuario("Melany","Lizarraga",15,"Femenino")
# usuario_2=Usuario("Belinda","Matorras",16,"Femenino")
# usuario_3=Usuario("priscila","Ramos",15,"Femenino")

# usuario_1.describir_usuario()
# usuario_1.saludar_usuario()

# usuario_2.describir_usuario()
# usuario_2.saludar_usuario()

# usuario_3.describir_usuario()
# usuario_3.saludar_usuario()

"""punto 7
Admin: Un administrador es un tipo de usuario con privilegios especiales. Cree una clase Admin que herede de la clase 
Usuario del ejercicio anterior y agréguele un atributo privilegios que almacene una lista de strings tales como “puede 
postear en el foro”, “puede borrar un post”, “puede banear usuario”, etc. Escriba un método mostrar_privilegios() que 
muestre el conjunto de privilegios del administrador, cree una instancia de la clase y llame al método."""

# class Administrador(Usuario):
#     def __init__(self,nombre,apellido,edad,genero,privilegios="-puede postear en el foro\n-puede borrar un post\n-puede banear a un usuario"): 
#         super().__init__(nombre,apellido,edad,genero)
#         super().__init__(nombre,apellido,edad,genero)
#         self.privilegios=privilegios
#         self.privi=Privilegios()

#     def mostrar_privilegios(self):
#         print("Los privilegios del administrador son:")
#         print(self.privilegios)

# Admin=Administrador("Mamita","zambrana",65,"femenino")
# Admin_1=Administrador("maria luz","zambrana",24,"femenino")

# Admin.describir_usuario()
# Admin.saludar_usuario()
# Admin.mostrar_privilegios()

# Admin_1.mostrar_privilegios_1()

"""punto 8
Privilegios: Escriba una clase Privilegios. La clase debería tener un atributo, privilegios, que almacene una lista de strings 
con los privilegios de manera similar a la del ejercicio 7. Mueva el método mostrar_privilegios() de ese ejercicio a esta 
clase, y haga que una instancia de esta clase sea un atributo de la clase Admin. Cree una nueva instancia de Admin y use 
el método para mostrar privilegios."""

# class Privilegios():
#     def __init__(self,privilegios="-puede postear en el foro\n-puede borrar un post\n-puede banear a un usuario"):
#         self.privilegios=privilegios

#     def mostrar_privilegios_1(self):
#         print("Los privilegios del administrador son:")
#         print(self.privilegios)

# privi=Privilegios()
# privi.mostrar_privilegios_1()

"""punto 9
Restaurante importado: Escriba un programa que esté en otro archivo que la clase Restaurante del ejercicio 4, e impórtela 
al módulo actual. Cree una instancia de Restaurante y llame a alguno de sus métodos para asegurarse que la importación 
funcionó."""

# from restaurante import*
# res=Restaurante("El sol","-pizza\n-helado\n-hamburgesa")
# res.abrir_restaurante()
# res.describir_restaurante()
 
"""punto 10
(Opcional): Repita el ejercicio anterior pero esta vez importando la clase Heladeria. ¿Qué se necesita para que funcione la 
importación?"""

# from restaurante import*

# hel=Heladeria("heladeria de helados","helados")
# hel.abrir_restaurante()
# hel.describir_restaurante()
# hel.lista_sabores()

