class MiClase:
    def __init__(self):
        self._atributo_privado = "Valor"
        self.__atributo_Muy_privado = "Mucho Valor"

    def __hablar(self):
        print("hola , soy un method privado")


objeto = MiClase()
print(objeto._atributo_privado)

# print(objeto.__atributo_Muy_privado)
# print(objeto.__hablar())
