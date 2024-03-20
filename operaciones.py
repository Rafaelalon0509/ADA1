
class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
arbol.insertar(12)
arbol.insertar(17)

print("Busqueda: ",arbol.buscar(7))
print("Busqueda: ", arbol.buscar(20))

print("Eliminando nodo 10...")
arbol.eliminar(10)
print("Busqueda: ", arbol.buscar(10))