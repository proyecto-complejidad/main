# dijkstra.py
from Librerias import *

def dijkstra(grafo, inicio, fin):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    heap = [(0, inicio)]
    caminos = {inicio: None}

    from controlador import Controlador
    controlador = Controlador(None)

    while heap:
        distancia_actual, nodo_actual = heapq.heappop(heap)
        if nodo_actual == fin:
            break
        for peso, vecino in grafo.get(nodo_actual, []):
            nueva_distancia = distancia_actual + peso
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                caminos[vecino] = nodo_actual
                heapq.heappush(heap, (nueva_distancia, vecino))

    ruta = []
    while fin:
        ruta.append(fin)
        fin = caminos[fin]
    return ruta[::-1], distancias[ruta[0]]
