class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f"el estudiante {self.nombre} está estudiando en {self.grado}....")


nombre = input("Nombre del estudiante: ")
edad = input(f"Edad del estudiante {nombre}: ")
grado = input(f"{nombre} cursa el grado: ")

estudiante1 = Estudiante(nombre, edad, grado)


print(f""""
      Datos del estudiante: \n
      Nombre: {estudiante1.nombre}\n
      Edad: {estudiante1.edad}\n
      Grado: {estudiante1.grado}\n
      """)

# estudiar = input()
# if estudiar.lower() == "estudiar":
#     estudiante1.estudiar()

while True:
    estudiar = input()
    if estudiar.lower() == "estudiar":
        estudiante1.estudiar()
        break
