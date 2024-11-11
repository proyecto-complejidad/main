from Librerias import *
from dijkstra import dijkstra
from kruskal import kruskal_mst
from tkintermapview import TkinterMapView

class Controlador:
    def __init__(self, root):
        self.centros_salud = self.cargar_centros_salud()
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Mapa con CustomTkinter y Dijkstra")
        self.grafo = self.construir_grafo(self.centros_salud)
        
        self.configurar_interfaz()

    def calcular_distancia(self, lat1, lon1, lat2, lon2):
        return math.sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)
    
    def construir_grafo(self, centros_salud):
        grafo = {}
        for centro_a in centros_salud:
            for centro_b in centros_salud:
                if centro_a != centro_b:
                    dist = self.calcular_distancia(
                        centro_a['lat'], centro_a['lon'],
                        centro_b['lat'], centro_b['lon']
                    )
                    if centro_a['nombre'] not in grafo:
                        grafo[centro_a['nombre']] = []
                    grafo[centro_a['nombre']].append((dist, centro_b['nombre']))
        return grafo
    
    def obtener_nodo_inicio(self, nombre, lat, lon):
        nodo_inicio = {
            "name": nombre,
            "lat": lat,
            "lon": lon
        }
        return nodo_inicio
    
    def obtener_nodo_final(self, nombre_final):
        for centro in self.centros_salud:
            if centro["nombre"].lower() == nombre_final.lower():
                return centro
        return None

    def aplicar_dijkstra(self, nombre_inicio, lat_inicio, lon_inicio, nombre_final): 
        inicio = self.obtener_nodo_inicio(nombre_inicio, lat_inicio, lon_inicio)
        final = self.obtener_nodo_final(nombre_final)

        if not inicio:
            print("¡El nodo de inicio es obligatorio!")
            return

        if not final:
            print("¡El nodo de destino debe ser ingresado!")
            return

        if inicio["nombre"] not in self.grafo:
            self.grafo[inicio["nombre"]] = []

            for centro in self.centros_salud:
                distancia = self.calcular_distancia(inicio["lat"], inicio["lon"], centro['lat'], centro['lon'])
                self.grafo[inicio["nombre"]].append((distancia, centro["nombre"]))

        ruta, distancia = dijkstra(self.grafo, inicio["nombre"], final["nombre"])
        distancia *= 10

        return ruta, distancia

    def aplicar_kruskal(self, nombre_inicio, lat_inicio, lon_inicio, nombre_final):
        inicio = self.obtener_nodo_inicio(nombre_inicio, lat_inicio, lon_inicio)
        final = self.obtener_nodo_final(nombre_final)

        if not inicio:
            print("¡El nodo de inicio es obligatorio!")
            return

        if not final:
            print("¡El nodo de destino debe ser ingresado!")
            return

        if inicio["nombre"] not in self.grafo:
            self.grafo[inicio["nombre"]] = []

            for centro in self.centros_salud:
                distancia = self.calcular_distancia(inicio["lat"], inicio["lon"], centro['lat'], centro['lon'])
                self.grafo[inicio["nombre"]].append((distancia, centro["nombre"]))

        if final["nombre"] not in self.grafo:
            self.grafo[final["nombre"]] = []

        subset_centros = random.sample(self.centros_salud, 500) if len(self.centros_salud) > 500 else self.centros_salud
        subset_centros.append({'name': 'inicio', 'lat': inicio["lat"], 'lon': inicio["lon"]})
        mst_edges, total_distancia = kruskal_mst(subset_centros)
        
        print("Aristas del MST (Conexiones):")
        for u, v, dist in mst_edges:
            print(f"{self.centros_salud[u]['nombre']} --> {self.centros_salud[v]['nombre']} : {dist:.2f} unidades de distancia")

        print(f"Total de distancia: {total_distancia}")
        return mst_edges, total_distancia


    def cargar_centros_salud(self):  # leer el .csv
        centros_salud = []
        with open("centros_salud.csv", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter='|')
            print("Encabezados encontrados:", reader.fieldnames)
            for row in reader:
                try:
                    lat_str = row["x_gis"].replace(',', '.').replace('.', '', row["x_gis"].count('.') - 1)
                    lon_str = row["y_gis"].replace(',', '.').replace('.', '', row["y_gis"].count('.') - 1)
                    
                    lat = float(lat_str)
                    lon = float(lon_str)

                    if -90 <= lat <= 90 and -180 <= lon <= 180:
                        centros_salud.append({
                            "departamento": row["Departamento"].strip(),
                            "provincia": row["Provincia"].strip(),
                            "distrito": row["Distrito"].strip(),
                            "nombre": row["Nombre"].strip(),
                            "telefono": row["Telefono"].strip(),
                            "lat": lat,
                            "lon": lon
                        })
                    else:
                        print(f"Coordenadas inválidas para {row['Nombre']}: lat={lat}, lon={lon}")
                except ValueError as e:
                    print(f"Error en las coordenadas para {row['Nombre']}: {e}")
        return centros_salud
    
    def buscar_centro_salud(self):  # implementación para buscar los centros de salud
        buscador = self.cargar_centros_salud()
        centro_a_buscar = self.buscar_centrito.get()
        for c in buscador:
            if c["nombre"].lower() == centro_a_buscar.lower():
                print(f"El centro de salud {centro_a_buscar} existe.")
                print(f"Los datos del centro son: {c}")
                return c
            
        print(f"El centro de salud {centro_a_buscar} no existe.")
