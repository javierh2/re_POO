# def decorador(funcion):
#     def funcion_mod():
#         print("antes de la funcion")
#         funcion()
#         print("despues de la funcion")
#     return funcion_mod


# def saludo():
#     print("hola Dev")


# saludo_modificado = decorador(saludo)
# saludo_modificado()


print("version optima")


def decorador(funcion):
    def funcion_mod():
        print("antes de la funcion")
        funcion()
        print("despues de la funcion")
    return funcion_mod


@decorador()
def saludo():
    print("hola Dev")


saludo()
