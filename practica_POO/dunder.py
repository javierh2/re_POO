class Persona:
    # metodo constructur de objeto
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # metodo devolucion en cadena de texto
    def __str__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"

    # metodo reconstructor
    def __repr__(self):
        return f'Persona("{self.nombre}", {self.edad})'

    def __add__(self, otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre + otro.nombre, nuevo_valor)


Javo = Persona("Javo", 30)
# representacion = repr(Javo)
# resultado = eval(representacion)
# print(resultado)
Juan = Persona("Juan", 35)

nueva_persona = Javo + Juan
print(nueva_persona)
