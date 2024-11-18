from Librerias import *
from Kruskal import UnionFind
from Dijkstra import construir_grafo, dijkstra_

cantidad_nodos = 10

class Controlador:
    def __init__(self):
        self.booleano = False
        self.grafo_og = []
        self.centros_salud = []
        self.lati = 0
        self.loni = 0
        self.grafo_kruskal = []
        self.distancia_kruskal = 0
        self.dij_lat = 0
        self.dij_lon = 0
        self.dij_nombre = 0
        self.dij_dis = 0
        self.dij_cam = 0

    def crear_grafo_og(self):
        i = 0
        with open("centros_salud.csv", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter='|')
            for row in reader:
                try:
                    lat_str = row["x_gis"].replace(',', '.').replace('.', '', row["x_gis"].count('.') - 1)
                    lon_str = row["y_gis"].replace(',', '.').replace('.', '', row["y_gis"].count('.') - 1)
                    lat = float(lat_str)
                    lon = float(lon_str)

                    self.centros_salud.append([])
                    self.centros_salud[i].append(row["Nombre"].strip())
                    self.centros_salud[i].append(lat)
                    self.centros_salud[i].append(lon)
                    i += 1
                except ValueError as e:
                    print(f"Error en las coordenadas para {row['Nombre']}: {e}")


        for i in range(cantidad_nodos):
            for j in range(i, cantidad_nodos):
                suma = (abs(self.centros_salud[i][1] - self.centros_salud[j][1])*abs(self.centros_salud[i][1] - self.centros_salud[j][1])) + (abs(self.centros_salud[i][2] - self.centros_salud[j][2])*abs(self.centros_salud[i][2] - self.centros_salud[j][2]))
                dist = math.sqrt(suma)*100
                dist = round(dist, 4)
                self.grafo_og.append((self.centros_salud[i][0], self.centros_salud[j][0], dist))

    def insertar_nuevo_nodo(self, nombre, lat, lon):
        self.lati = lat
        self.loni = lon
        for i in range(cantidad_nodos):
            sumalat = abs(self.centros_salud[i][1] - lat)
            sumalon = abs(self.centros_salud[i][2] - lon)
            suma = (sumalat*sumalat) + (sumalon*sumalon)
            dist = math.sqrt(suma)*100
            dist = round(dist, 4)
            self.grafo_og.append((nombre, self.centros_salud[i][0], dist))

    def kruskal(self):
        nodos = sorted(set(u for edge in self.grafo_og for u in edge[:2]))
        node_map = {nodo: idx for idx, nodo in enumerate(nodos)}
        n = len(nodos)
        uf = UnionFind(n)

        mst_edges = []
        total_cost = 0

        edges = [(node_map[u], node_map[v], weight) for u, v, weight in self.grafo_og]
        edges.sort(key=lambda x: x[2])

        for u, v, weight in edges:
            if uf.find(u) != uf.find(v):
                uf.union(u, v)
                mst_edges.append((u, v, weight))
                total_cost += weight

        self.grafo_kruskal = mst_edges
        self.distancia_kruskal = total_cost

        MST = nx.Graph()
        for u, v, weight in mst_edges:
            MST.add_edge(u, v, weight=weight)

        pos = nx.spring_layout(MST, scale=2)
        fig, ax = plt.subplots(figsize=(6, 8), dpi=300)
        nx.draw(MST, pos, with_labels=True, node_color='lightgreen', node_size=700, font_size=10, font_weight='bold',
                ax=ax)
        nx.draw_networkx_edge_labels(MST, pos,
                                     edge_labels={(u, v): f"{d['weight']}" for u, v, d in MST.edges(data=True)}, ax=ax)

        plt.title("Árbol de Expansión Mínima")
        plt.savefig("grafo_mst_maximized.png", format="png", bbox_inches='tight', pad_inches=0.1)
        plt.close()  # Cierra la figura para liberar memoria

    def dijsktra(self, nombre_botica):
        edges = self.grafo_og
        start = "Almacen"
        target = nombre_botica
        graph = {}
        for u, v, weight in edges:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append((v, weight))
            graph[v].append((u, weight))

        distances = {node: float('inf') for node in graph}
        distances[start] = 0

        previous_nodes = {node: None for node in graph}
        priority_queue = [(0, start)]  # (distancia, nodo)
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            if current_distance > distances[current_node]:
                continue
            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        def reconstruct_path(target):
            path = []
            current_node = target
            while current_node is not None:
                path.append(current_node)
                current_node = previous_nodes[current_node]
            return path  # Revertir para obtener el camino correcto

        # Obtener la distancia y la ruta al nodo objetivo
        shortest_distance = distances[target]
        shortest_path = reconstruct_path(target)

        print(self.dij_cam)
        self.dij_dis, self.dij_cam = shortest_distance, shortest_path

    def buscar_botica(self, nombre):
        with open("centros_salud.csv", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter='|')
            for row in reader:
                if row["Nombre"] == nombre:
                    self.dij_lon = row["x_gis"]
                    self.dij_lat = row["y_gis"]
                    return 1
        return 0

    def probar(self):
        for a in self.grafo_og:
            print(f"{a[0]}, {a[1]}, {a[2]}")
