class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = int(edad)

    def dar_datos(self):
        print(f"la pesona se llama {self.nombre} y tiene {self.edad} años")


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def dar_grado(self):
        print(f"{self.nombre} cursa el {self.grado} grado")


Juan = Persona("Juan", 35)
Juan.dar_datos()

Javier = Estudiante("Javo", 30, "segundo")
Javier.dar_grado()

print("_____________________________________________________________________")


class Animal:
    def comer(self):
        print("Este animal está comiendo")


class Mamifero(Animal):
    def amamanta(self):
        print("Este animal está amamantando")


class Ave(Animal):
    def vuela(self):
        print("Este animal está volando")


class Murcielago(Mamifero, Ave):
    pass


murcielago = Murcielago()
murcielago.amamanta()
murcielago.comer()
murcielago.vuela()
print(Murcielago.mro())
