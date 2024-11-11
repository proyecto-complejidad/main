# kruskal.py
from Librerias import *

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal_mst(centros_salud, map_widget=None):
    edges = []
    n = len(centros_salud)
    
    from controlador import Controlador
    controlador = Controlador(None)
    
    for i in range(n):
        for j in range(i + 1, n):
            dist = controlador.calcular_distancia(
                centros_salud[i]['lat'], centros_salud[i]['lon'],
                centros_salud[j]['lat'], centros_salud[j]['lon']
            )
            edges.append((dist, i, j))

    edges.sort()
    
    uf = UnionFind(n)
    mst_edges = []
    total_distancia = 0
    for dist, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_edges.append((u, v, dist))
            total_distancia += dist
            print(total_distancia)
            if len(mst_edges) == n - 1:
                break
    
    if map_widget:
        map_widget.delete_all_marker()
        for u, v, dist in mst_edges:
            lat1, lon1 = centros_salud[u]['lat'], centros_salud[u]['lon']
            lat2, lon2 = centros_salud[v]['lat'], centros_salud[v]['lon']
            map_widget.set_path([(lat1, lon1), (lat2, lon2)])
    
    return mst_edges, total_distancia
