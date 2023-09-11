class Gato():
    def sonido(self):
        return "Miau"


class Perro():
    def sonido(self):
        return "Guau"


def hacer_sonido(mascota):
    print(mascota.sonido())


gato_1 = Gato()
perro_1 = Perro()

print(gato_1.sonido())
print(perro_1.sonido())

hacer_sonido(gato_1)
