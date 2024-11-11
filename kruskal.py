import math

def calcular_distancia(lat1, lon1, lat2, lon2):
    return math.sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)

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
    
    # Crear todas las aristas con distancias entre los centros de salud
    for i in range(n):
        for j in range(i + 1, n):
            dist = calcular_distancia(
                centros_salud[i]['lat'], centros_salud[i]['lon'],
                centros_salud[j]['lat'], centros_salud[j]['lon']
            )
            edges.append((dist, i, j))

    # Ordenar las aristas por distancia
    edges.sort()
    
    # Aplicar el algoritmo de Kruskal
    uf = UnionFind(n)
    mst_edges = []
    for dist, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_edges.append((u, v, dist))
            if len(mst_edges) == n - 1:
                break
    
    # Debuggeo en consola de las conexiones del MST
    print("Conexiones del MST (debug):")
    for u, v, dist in mst_edges:
        print(f"{centros_salud[u]['nombre']} -- {centros_salud[v]['nombre']} : {dist:.2f} unidades de distancia")

    # Mostrar el MST en el mapa, si el map_widget está presente
    if map_widget:
        map_widget.delete_all_marker()
        for u, v, dist in mst_edges:
            lat1, lon1 = centros_salud[u]['lat'], centros_salud[u]['lon']
            lat2, lon2 = centros_salud[v]['lat'], centros_salud[v]['lon']
            map_widget.set_path([(lat1, lon1), (lat2, lon2)])

    return mst_edges
