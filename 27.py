class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina

    def describir_restaurante(self):
        print(f"el restaurante {self.nombre_restaurante} es de tipo {self.tipo_cocina}")

    def abrir_restaurante(self):
        print(self.nombre_restaurante, "abrió")

restaurante = Restaurante("Shokudo", "Japonés")
restaurante.describir_restaurante()
restaurante.abrir_restaurante()

class PuestoDeHelados(Restaurante):
    def __init__(self, nombre, *sabores):
        super().__init__(nombre, "Heladería")
        self.sabores = sabores
    def mostrar_sabores(self):
        for i in self.sabores:
            print(i)

heladería = PuestoDeHelados("Freddo", "Frutilla", "Vainilla", "Chocolate")
heladería.mostrar_sabores()
