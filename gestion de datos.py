"""punto 1
Hacer un programa que gestiones datos para una escuela. 
El programa tiene que ser capaz de:
a) Llevar un registro de todos los datos de alumnos de la escuela (Nombre, 
Apellido, fecha de nacimiento, DNI, Nombre de Tutor, registro de todas las 
notas, cantidad de faltas, cantidad de amonestaciones recibidas. 
Recomendación: Para llevar un registro de estos dato se puede 
utilizar un diccionario estructurado de la siguiente manera: 
{ 
“Alumnos” : [alumno1,alumno2,alumno3 ] 
} 
Donde cada alumno es otro diccionario estructurado de la  
siguiente forma: 
{ 
“Nombre”: nombre de alumno, 
“Apellido” : apellido de alumno, 
“DNI” : DNI de alumno 
“Fecha de nacimiento”, fecha de nacimiento de alumno, 
“Tutor” : nombre y apellido de tutor, 
“Notas” : todas las notas del alumno, 
“Faltas” : cantidad de faltas, 
“amonestaciones” : cantidad de amonestaciones 
} 
En esta estructura: 
Datos  = { 
“Alumnos” : [alumno1,alumno2,alumno3 ] 
} 
Para acceder por ejemplo al numero de DNI del tercer alumno 
podríamos hacer algo así: 
Datos[“Alumnos”][2][“DNI”] 
Este es un ejemplo de estructura, se puede cambiar 
completamente o hacer algunos cambios sobre el para mejorar el 
orden (si lo consideran necesario) 
b) Mostrar los datos de cada alumno 
c) Modificar los datos de los alumnos 
d) Agregar alumnos 
e) Expulsar alumnos.
 """

# alumnos={
#     "lucas":{
#         "Nombre":"LUCAS",
#         "Apellido":"LOPEZ",
#         "DNI":45.667912,
#         "Fecha de nacimiento":"23/10/2007",
#         "Tutor":"JUAN GUTIERRES",
#         "Notas":[7,10,8], 
#         "Faltas":3,
#         "Amonestaciones":0} 
#     ,"federico":{
#         "Nombre":"FEDERICO",
#         "Apellido":"SOTO",
#         "DNI":44.798861,
#         "Fecha de nacimiento":"11/4/2008",
#         "Tutor":"BELINDA TELLO",
#         "Notas":[10,9,10], 
#         "Faltas":0,
#         "Amonestaciones":0}
#     ,"pedro":{
#         "Nombre":"PEDRO", 
#         "Apellido":"PAEZ",
#         "DNI":45.055027,
#         "Fecha de nacimiento":"20/6/2007",
#         "Tutor":"ALVARO RAMOS",
#         "Notas":[8,7,5], 
#         "Faltas":2,
#         "Amonestaciones":0}
#     ,"melany":{
#         "Nombre":"MELANY", 
#         "Apellido":"LIZARRAGA",
#         "DNI":45.967017,
#         "Fecha de nacimiento":"26/9/2007",
#         "Tutor":"MELODY LIZARRAGA",
#         "Notas":[3,6,4], 
#         "Faltas":25,
#         "Amonestaciones":9}
#     ,"brenda":{
#         "Nombre":"BRENDA", 
#         "Apellido":"OCAMPOS",
#         "DNI":44.238952,
#         "Fecha de nacimiento":"15/9/2008",
#         "Tutor":"ESTEBAN OCAMPOS",
#         "Notas":[3,6,8], 
#         "Faltas":4,
#         "Amonestaciones":2}
# }

# def lista():
#     print("Estos son los alumnos que estan en la lista: ")
#     for llave in alumnos:
#         print(llave)

# def opciones():
#     seleccion=0
#     while seleccion!=5:
#         print("------------------------------------------------------------------------------------------")
#         print(">-Bienvenido al programa de gestion de la escuela-<")
#         lista()
#         print("-Elija una de las siguentes opsiones para mas informacion: ")
#         print("------------------------------------------------------------------------")
#         print("1. mostrar los datos de un alumno")
#         print("2. agregar a un alumno")
#         print("3. expulsar a un alumno")
#         print("4. modificar los datos de un alumno")
#         print("5. salir")
#         seleccion=int(input("-Ingrese su eleccion: "))
#         if seleccion==1:
#             ver_los_datos_de_los_alumnos()
#         elif seleccion==2:
#             agregar()
#         elif seleccion==3:
#             expulsar()
#         elif seleccion==4:
#             modificar()
#         else :
#             salir()
            
# def ver_los_datos_de_los_alumnos():
#     nombre=input("ingrese el nombre del alumno al cual quiera ver sus datos: ")
#     print(alumnos[nombre])

# def expulsar():
#     expulsado=input("ingrese el nombre del alumno al que quiera expulsar: ")
#     del alumnos[expulsado]
#     print(f"listo...{expulsado} fue expulsado")
#     print("la lista fue actualizada: ")
#     for llave in alumnos:
#         print(llave)

# def agregar():
#     agregado=input("ingrese el nombre del alumno al que quiera agregar a la lista: ")
#     alumnos=[agregado]
#     print(f"{agregado} fue agregada a la lista")

# def modificar():
#     print("modificando.....ERROR......lo sentimos hubo un problema no sera posible realizar esta opción...")

# def salir():
#     print("gracias por utilizar el programa")

# opciones()



