class Persona:
    def __init__(self, nombre, edad):
        # definiendo atributos
        self.__nombre = nombre
        self._edad = edad

    # propiedad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, new_name):
        self.__nombre = new_name

    @nombre.deleter
    def nombre(self):
        del self.__nombre


Javier = Persona("Javier", 30)
nombre = Javier.nombre
print(nombre)

Javier.nombre = "Javo jr."
nombre = Javier.nombre
print(nombre)

del Javier.nombre

nombre = Javier.nombre
print(nombre)
