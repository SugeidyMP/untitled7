__author__ = 'sugeidy mejia'

from  memoriaDinamica import*

TiendaDeRopa = ['pantalones', 'blusas','lenceria', 'calcetines']
precios=['300','100','25','15']
descuento=['10%','78','90','34','90']

lista= memoriaDinamica(TiendaDeRopa)
lista.imprimirLista()
lista.agregarelementoarray('camisas')
lista.imprimirLista()
lista.ordenarLista()
lista.imprimirLista()
lista.eliminarElemento('calcetines')
lista.imprimirLista()
lista.eliminarNElementos(1)
lista.imprimirLista()

lista1=memoriaDinamica(precios)
lista1.imprimirLista()
lista1.agregarelementoarray(150)
lista1.imprimirLista()

lista1.agregarelementoarray(200)
lista1.imprimirLista()

lista2=memoriaDinamica(descuento)
lista2.imprimirLista()
lista2.agregarelementoarray('30')
lista2.imprimirLista()
lista2.insertarNPosicion(3,'50')
lista2.imprimirLista()










