__author__ = 'MATILDE DIAZ GARCIA'

from MemoriaDinamica import *
FERRETERIA = ['BOMBA DE GAS','MANGUERA', 'TORNILLO', 'CLAVOS', 'FOCOS']
COSTO = [1500, 300, 50, 10, 20]


listas = MemoriaDinamica(FERRETERIA)
listas.imprimirLista()
listas.ordenarLista()
listas.imprimirLista()
listas.agregarelementoarray('TUBOS')
listas.imprimirLista()
lista2 = MemoriaDinamica(COSTO)
lista2.imprimirLista()
lista2.agregarelementoarray(35)
lista2.imprimirLista()
