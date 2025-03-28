"""punto 1
1) Hacer un programa que gestiones datos para una escuela. El programa tiene que ser capaz 
de: 
a) Llevar un registro de todos los datos de alumnos de la escuela (Nombre, Apellido, 
fecha de nacimiento, DNI, Nombre de Tutor, registro de todas las notas, cantidad de 
faltas, cantidad de amonestaciones recibidas. 
b) Mostrar los datos de cada alumno 
c) Modificar los datos de los alumnos 
d) Agregar alumnos 
e) Expulsar alumnos 
f)  Dar Persistencia a los Datos del programa mediante la implementación Archivos 
El trabajo practico se deberá subir a un repositorio de GitHub Publico, y se entregara 
únicamente la dirección del repositorio (No de la pagina)."""

alumnos={
    "lucas":{
        "Nombre":"LUCAS",
        "Apellido":"LOPEZ",
        "DNI":45.667912,
        "Fecha de nacimiento":"23/10/2007",
        "Tutor":"JUAN GUTIERRES",
        "Notas":[7,10,8], 
        "Faltas":3,
        "Amonestaciones":0}
    ,"federico":{
        "Nombre":"FEDERICO",
        "Apellido":"SOTO",
        "DNI":44.798861,
        "Fecha de nacimiento":"11/4/2008",
        "Tutor":"BELINDA TELLO",
        "Notas":[10,9,10], 
        "Faltas":0,
        "Amonestaciones":0}
    ,"pedro":{
        "Nombre":"PEDRO", 
        "Apellido":"PAEZ",
        "DNI":45.055027,
        "Fecha de nacimiento":"20/6/2007",
        "Tutor":"ALVARO RAMOS",
        "Notas":[8,7,5], 
        "Faltas":2,
        "Amonestaciones":0}
    ,"melany":{
        "Nombre":"MELANY", 
        "Apellido":"LIZARRAGA",
        "DNI":45.967017,
        "Fecha de nacimiento":"26/9/2007",
        "Tutor":"MELODY LIZARRAGA",
        "Notas":[3,6,4], 
        "Faltas":25,
        "Amonestaciones":9}
    ,"brenda":{
        "Nombre":"BRENDA", 
        "Apellido":"OCAMPOS",
        "DNI":44.238952,
        "Fecha de nacimiento":"15/9/2008",
        "Tutor":"ESTEBAN OCAMPOS",
        "Notas":[3,6,8], 
        "Faltas":4,
        "Amonestaciones":2}
}


def opciones():
    seleccion=0
    while seleccion!=6:
        print("------------------------------------------------------------------------------------------")
        print(">-Bienvenido/a al programa de gestion de la escuela-<")
        print("-Elija una de las siguentes opsiones para mas informacion: ")
        print("------------------------------------------------------------------------")
        print("1. ver la lista de los alumnos")
        print("2. mostrar los datos de un alumno/a")
        print("3. agregar a un alumno/a")
        print("4. expulsar a un alumno/a")
        print("5. modificar los datos de un alumno/a")
        print("6. salir")
        seleccion=int(input("-Ingrese su eleccion: "))
        if seleccion==1:
            lista()
        elif seleccion==2:
            ver_los_datos_de_los_alumnos()
        elif seleccion==3: 
            agregar()
        elif seleccion==4:
            expulsar()
        elif seleccion==5:
            modificar()
        else :
            salir()

def lista():
    print("Estos son los alumnos que estan en la lista: ")
    for llave in alumnos:
        print(llave)
    

def agregar():
    
    print("para agregar a un alumno/a a la lista tiene que...")
    print("ingrese los siguientes datos: ")
    Nombre=input("ingrese su nombre: ")
    Apellido=input("ingrese su apellido: ")
    DNI=input("ingrese su DNI: ")
    Fecha_De_Nacimiento=input("ingrese su fecha de nacimiento: ")
    Tutor=input("ingrese el nombre del tutor: ")
    Notas="nada"
    Faltas=0
    Amorestaciones=0
    agregado=[]
    agregado.extend([f"Nombre: {Nombre}, Apellido: {Apellido}, DNI: {DNI}, Fecha De Nacimiento: {Fecha_De_Nacimiento}, Tutor: {Tutor}, Notas: {Notas}, Faltas: {Faltas}, Amorestaciones: {Amorestaciones}"]) 
    alumnos[Nombre]=agregado
    print(f"listo...{Nombre} fue agregado/a a la lista...")
    print("la lista fue actualizada: ")
    for llave in alumnos:
        print(llave)
    archivo=open("archivo.txt","a")
    archivo.write("Nombre: ")
    archivo.write(Nombre)
    archivo.write(", Apellido: ")
    archivo.write(Apellido)
    archivo.write(", DNI: ")
    archivo.write(DNI)
    archivo.write(", Fecha se nacimiento: ")
    archivo.write(Fecha_De_Nacimiento)
    archivo.write(", Tutor: ")
    archivo.write(Tutor)
    archivo.write(", Notas: ")
    archivo.write(Notas)
    archivo.write(", Faltas: ")
    archivo.write(Faltas)
    archivo.write(", Amorestaciones: ")
    archivo.write(Amorestaciones)
    archivo.close()
    archivo=open("archivo.txt","r")
    agregado.extend("archivo.txt")
    archivo.close()


def ver_los_datos_de_los_alumnos():
    nombre=input("ingrese el nombre del alumno/a al cual quiera ver sus datos: ")
    print(alumnos[nombre])
    archivo=open("archivo.txt","r")
    archivo.readlines(nombre)
    print(archivo.readlines)
    archivo.close()

def expulsar():
    expulsado=input("ingrese el nombre del alumno/a al que quiera expulsar: ")
    del alumnos[expulsado]
    print(f"listo...{expulsado} fue expulsado/a...")
    print("la lista fue actualizada: ")
    for llave in alumnos:
        print(llave)

def modificar():
    print("modificando.....ERROR......lo sentimos hubo un problema no sera posible realizar esta opción...")

def salir():
    print(">-gracias por utilizar el programa de gestion de la escuela-<")

opciones()
