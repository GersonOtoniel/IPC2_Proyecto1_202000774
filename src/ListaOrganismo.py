class Nodo:
    def __init__(self, nombre, codigo, letra):
        self.siguiente = None
        self.nombre = nombre
        self.codigo = codigo
        self.letra = letra


class ListaOrganismo:
    def __init__(self):
        self.primero = None
        self.tamaño = 0

    def insertar(self, nombre, codigo, letra):
        nuevo = Nodo(nombre, codigo, letra)

        if self.tamaño == 0:
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente != None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self.tamaño=+1

    def recorrerLista(self):
        actual = self.primero
        while actual != None:
            print(actual.codigo + ", " + actual.nombre + ", " + actual.letra)
            actual = actual.siguiente
