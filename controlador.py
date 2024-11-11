from Librerias import *
from dijkstra import dijkstra, construir_grafo
from kruskal import kruskal_mst
import customtkinter as ctk
from tkintermapview import TkinterMapView

class Controlador:
    def __init__(self, root):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.centros_salud = self.cargar_centros_salud()
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Mapa con CustomTkinter y Dijkstra")
        
        self.map_widget = TkinterMapView(root, width=760, height=500, corner_radius=10)
        self.grafo = construir_grafo(self.centros_salud)
        
        self.configurar_interfaz()

    def configurar_interfaz(self):
        top_frame = ctk.CTkFrame(self.root)
        top_frame.pack(pady=10, fill="x")

        self.entry_start = ctk.CTkEntry(top_frame, placeholder_text="Centro de salud inicial")
        self.entry_start.pack(side="left", padx=10, pady=5)

        self.entry_end = ctk.CTkEntry(top_frame, placeholder_text="Centro de salud destino")
        self.entry_end.pack(side="left", padx=10, pady=5)

        search_button = ctk.CTkButton(top_frame, text="Buscar Ruta", command=self.aplicar_dijkstra)
        search_button.pack(side="left", padx=10, pady=5)

        self.label_result = ctk.CTkLabel(self.root, text="")
        self.label_result.pack(pady=5)

        mst_button = ctk.CTkButton(top_frame, text="Mostrar MST", command=self.aplicar_kruskal)
        mst_button.pack(side="left", padx=10, pady=5)

        map_frame = ctk.CTkFrame(self.root)
        map_frame.pack(pady=10, fill="both", expand=True)

        self.map_widget.set_position(-12.0464, -77.0428)
        self.map_widget.set_zoom(10)
        self.map_widget.pack(fill="both", expand=True)

    def aplicar_dijkstra(self):
        inicio = self.entry_start.get()
        fin = self.entry_end.get()

        ruta, distancia = dijkstra(self.grafo, inicio, fin)
        distancia *= 10

        self.label_result.configure(
            text=f"Ruta más corta: {' -> '.join(ruta)}\nDistancia total: {distancia:.2f} kilómetros"
        )

    def aplicar_kruskal(self):
        subset_centros = random.sample(self.centros_salud, 500) if len(self.centros_salud) > 500 else self.centros_salud
        kruskal_mst(subset_centros, self.map_widget)

        self.label_result.configure(
            text="Árbol de expansión mínima generado y mostrado en el mapa."
        )

    def cargar_centros_salud(self):
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
                            "nombre": row["Nombre"].strip(),
                            "lat": lat,
                            "lon": lon
                        })
                    else:
                        print(f"Coordenadas inválidas para {row['Nombre']}: lat={lat}, lon={lon}")
                except ValueError as e:
                    print(f"Error en las coordenadas para {row['Nombre']}: {e}")
        return centros_salud