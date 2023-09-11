class Movil:
    # metodo constructor
    def __init__(self, marca, modelo, camara):
        # definiendo atributos
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    # definiendo metodos
    def llamar(self):
        print(f"Movil {self.marca} {self.modelo} en tono de llamada")

    def colgar(self):
        print(f"Movil {self.marca} sin tono")


# Instancias de Clases
movil1 = Movil("Nokia", "1100", "0MP")
movil2 = Movil("Iphone", "15 PRO", "48MP")
movil3 = Movil("Motorola", "E44", "20MP")

# Utilizando metodos de la clase en cada objeto creado
movil1.llamar()
movil1.colgar()

movil2.llamar()
movil2.colgar()
