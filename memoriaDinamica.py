__author__ = 'sugeidy mejia'

class memoriaDinamica:
    __lista = []

    def __init__(self, list):
       self.__lista = list

    def agregarelementoarray(self, elemento):
        self.__lista.append(elemento)

    def ordenarLista(self):
       self.__lista.sort()

    def eliminarNElementos(self, num):
       self.__lista.pop(num)

    def eliminarElemento(self, elemento):
       self.__lista.remove(elemento)

    def insertarNPosicion(self, num, elemento):
       self.__lista.insert(num, elemento)

    def imprimirLista(self):
       print (self.__lista)
