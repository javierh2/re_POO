class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print(f"{self.nombre} está hablando")


class Empleado(Persona):
    # Herencia
    def __init__(self, nombre, edad, nacionalidad, trabajo, sueldo):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.sueldo = sueldo


class Jefe(Persona):
    # Herencia
    def __init__(self, nombre, edad, nacionalidad, rol, empresa):
        super().__init__(nombre, edad, nacionalidad)
        self.rol = rol
        self.empresa = empresa


class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        print(f"Mi habilidad es {self.habilidad}")


class EmpleadoArtista(Persona, Artista):
    # Herencia multiple
    def __init__(self, nombre, edad, nacionalidad, habilidad, trabajo, sueldo):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.trabajo = trabajo
        self.sueldo = sueldo

    def presentarse(self):
        return f"{super().mostrar_habilidad()}"


Rober = Empleado("Rober", 30, "Arg", "Dev", 250000)
John = Jefe("John", 50, "Br", "Boss", "Meta")
print(Rober.edad)
print(Rober.trabajo)
print(Rober.sueldo)
print(f"John trabaja en {John.empresa}")
Rober.hablar()
John.hablar()
print("___________________________________________")
Javo = EmpleadoArtista("Javo", 30, "Arg", "Programar", "Jr", 300000)
# print(Javo.mostrar_habilidad())  si le coloco el RETURN
Javo.hablar()
Javo.mostrar_habilidad()
Javo.presentarse()
