class Restaurante():
    def __init__(self,restaurante_nombre,tipo_comida):
        self.restaurante_nombre=restaurante_nombre
        self.tipo_comida=tipo_comida

    def describir_restaurante(self):
        print(f"Bienvenidos al restaurante {self.restaurante_nombre}.")
        print("----------------------------------------------------------")
        print("donde el tipo de comida es:")
        print(self.tipo_comida)

    def abrir_restaurante(self):
        print("El restaurante esta abierto:")

class Heladeria(Restaurante):
    def __init__(self,restaurante_nombre,tipo_comida,sabores="chocolate\nvainilla\nfrutilla"):
        super().__init__(restaurante_nombre,tipo_comida)
        self.sabores=sabores

    def lista_sabores(self):
        print("la lista de sabores es:")
        print(self.sabores)
