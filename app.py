import customtkinter as ctk
from tkintermapview import TkinterMapView
import csv
import random
from dijkstra import dijkstra, construir_grafo
from kruskal import kruskal_mst

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def cargar_centros_salud():
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

def buscar_ruta_mas_corta():
    inicio = entry_start.get()
    fin = entry_end.get()
    ruta, distancia = dijkstra(grafo, inicio, fin)
    distancia = distancia * 10  # Convertir a kilómetros
    label_result.configure(text=f"Ruta más corta: {' -> '.join(ruta)}\nDistancia total: {distancia:.2f} kilómetros")

def mostrar_mst():
    # Seleccionar 50 datos aleatorios de los centros de salud
    subset_centros = random.sample(centros_salud, 150) if len(centros_salud) > 50 else centros_salud
    kruskal_mst(subset_centros, map_widget)  # Mostrar MST en el mapa y debuggeo en consola
    label_result.configure(text="Árbol de expansión mínima generado y mostrado en el mapa con 50 centros de salud.")

root = ctk.CTk()
root.geometry("800x600")
root.title("Mapa con CustomTkinter y Dijkstra")

centros_salud = cargar_centros_salud()
grafo = construir_grafo(centros_salud)

top_frame = ctk.CTkFrame(root)
top_frame.pack(pady=10, fill="x")

entry_start = ctk.CTkEntry(top_frame, placeholder_text="Centro de salud inicial")
entry_start.pack(side="left", padx=10, pady=5)

entry_end = ctk.CTkEntry(top_frame, placeholder_text="Centro de salud destino")
entry_end.pack(side="left", padx=10, pady=5)

search_button = ctk.CTkButton(top_frame, text="Buscar Ruta", command=buscar_ruta_mas_corta)
search_button.pack(side="left", padx=10, pady=5)

label_result = ctk.CTkLabel(root, text="")
label_result.pack(pady=5)

mst_button = ctk.CTkButton(top_frame, text="Mostrar MST", command=mostrar_mst)
mst_button.pack(side="left", padx=10, pady=5)

map_frame = ctk.CTkFrame(root)
map_frame.pack(pady=10, fill="both", expand=True)

map_widget = TkinterMapView(map_frame, width=760, height=500, corner_radius=10)
map_widget.set_position(-12.0464, -77.0428)
map_widget.set_zoom(10)
map_widget.pack(fill="both", expand=True)

root.mainloop()
