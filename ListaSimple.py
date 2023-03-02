class Nodo:
    def __init__(self, dato, x, y):
        self.siguiente = None
        self.dato = dato
        self.x = x
        self.y = y
    

class ListaSimple:
    def __init__(self):
        self.primero = None
        self.tamaño = 0

    def insertar(self, dato, x, y):
        nuevonodo = Nodo(dato, x, y)
        if self.tamaño == 0:
            self.primero = nuevonodo
        else:
            nodoactual = self.primero
            while nodoactual.siguiente != None:
                nodoactual = nodoactual.siguiente
            nodoactual.siguiente = nuevonodo
        self.tamaño+=1

    def recorrerLista(self):
        #lista = []
        actual = self.primero
        while actual != None:
            #lista.append(actual.dato)
            print(actual.dato + ", "+actual.x+ ", " + actual.y)
            actual = actual.siguiente 
        #return print(lista)

    def tamañolista(self):
        print(self.tamaño)   



"""
lista1 = ListaSimple()
lista1.insertar("Gerson")
lista1.insertar("David")
lista1.insertar("Otoniel")
#print(lista1.tamaño)
lista1.recorrerLista()
"""
