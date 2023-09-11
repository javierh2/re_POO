class Car():
    def __init__(self):
        self._estado = "apagado"

    def encender(self):
        self._estado = "encendido"
        print("el auto está ON")

    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("me voy en auto")


mi_auto = Car()
mi_auto.conducir()
