class Persona:
    def __init__(self, nombre, edad):
        # definiendo atributos
        self._nombre = nombre
        self._edad = edad

    # ingreso al atributo privado
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, new_name):
        self._nombre = new_name


Javier = Persona("Javier", 30)
nombre = Javier.get_nombre()
print(nombre)
Javier.set_nombre("Javo JR.")
nombre = Javier.get_nombre()
print(nombre)
