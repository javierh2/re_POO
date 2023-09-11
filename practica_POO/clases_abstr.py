from abc import ABC, abstractclassmethod


class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractclassmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola me llamo {self.nombre} soy {self.sexo} y tengo {self.edad} años")


class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"estoy estudiando: {self.actividad}")


class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"estoy trabajando de: {self.actividad}")


Javo = Estudiante("Javo", 30, "He", "Dev")
Juan = Trabajador("Juan", 35, "He", "Ing")

Javo.hacer_actividad()
Juan.presentarse()
Juan.hacer_actividad()
