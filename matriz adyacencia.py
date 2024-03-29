class GrafoMatrizAdyacencia :
    
    def __init__(self, num_vertices ):
        self.num_vertices = num_vertices
        self.matriz = [[0]*num_vertices for _ in range (num_vertices)]

    def agregar_aristas(self,origen,destino):
        self.matriz[origen][destino ] = 1

        #cuando los grafos no son dirigidos sse puede hacer lo siguiente 

        self.matriz[destino ][origen] = 1


    def imprimir_matriz_adyacencia(self):

        for fila in self.matriz:
            print(fila)
#instanciar clase GrafoMtrizAdyacencia
            
grafo=GrafoMatrizAdyacencia(10)

#agregamos las aristas al grafo


grafo.agregar_aristas(1,2)
grafo.agregar_aristas(1,4)
grafo.agregar_aristas(2,3)
grafo.agregar_aristas(2,5)
grafo.agregar_aristas(3,2)
grafo.agregar_aristas(3,4)
grafo.agregar_aristas(4,1)
grafo.agregar_aristas(4,5)
grafo.agregar_aristas(5,2)
grafo.agregar_aristas(5,4)

#grafo.agregar_aristas(0,1)
#grafo.agregar_aristas(0,2)
#grafo.agregar_aristas(1)
#grafo.agregar_aristas()

grafo.imprimir_matriz_adyacencia()



