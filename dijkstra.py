# dijkstra.py
from Librerias import *

def calcular_distancia(lat1, lon1, lat2, lon2):
    return math.sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)

def construir_grafo(centros_salud):
    grafo = {}
    for centro_a in centros_salud:
        for centro_b in centros_salud:
            if centro_a != centro_b:
                dist = calcular_distancia(
                    centro_a['lat'], centro_a['lon'],
                    centro_b['lat'], centro_b['lon']
                )
                if centro_a['nombre'] not in grafo:
                    grafo[centro_a['nombre']] = []
                grafo[centro_a['nombre']].append((dist, centro_b['nombre']))
    return grafo

def dijkstra(grafo, inicio, fin):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    heap = [(0, inicio)]
    caminos = {inicio: None}

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
