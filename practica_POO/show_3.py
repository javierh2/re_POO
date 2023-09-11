class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __repr__(self):
        return f"{self.nombre} (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})"

    def __add__(self, otro_pj):
        nuevo_pj = self.nombre + "-" + otro_pj.nombre
        nueva_f = round(((self.fuerza + otro_pj.fuerza)/2)**2)
        nueva_v = round(((self.velocidad + otro_pj.velocidad)/2)**2)
        return Personaje(nuevo_pj, nueva_f, nueva_v)


Goku = Personaje("Goku", 100, 100)
Vegeta = Personaje("Vegeta", 99, 99)
print(Goku)
print(Vegeta)

fusion = Goku + Vegeta
print(fusion)
