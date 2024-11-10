import customtkinter as ctk
from tkintermapview import TkinterMapView
import requests

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def get_coordinates(place_name):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": place_name,
        "format": "json",
        "limit": 1
    }

    response = requests.get(url, params=params, headers={"User -Agent": "YourAppName"})

    if response.status_code == 200 and response.json():
        data = response.json()[0]
        lat, lon = float(data["lat"]), float(data["lon"])
        return lat, lon
    else:
        return None

def search_location():
    place_name = entry.get()
    coordinates = get_coordinates(place_name)
    if coordinates:
        map_widget.set_position(coordinates[0], coordinates[1])
        map_widget.set_zoom(10)
        label.configure(text=f"Found location: {place_name}")
    else:
        label.configure(text="Location not found. Try another place.")

def on_map_right_click(event):
    lat, lon = map_widget.get_position()
    map_widget.delete_all_marker()
    marker = map_widget.set_marker(lat, lon, text="Selected Location")

    label.configure(text=f"Coordinates: {lat}, {lon}")

root = ctk.CTk()
root.geometry("800x600")
root.title("Map with CustomTkinter and OpenStreetMap")

top_frame = ctk.CTkFrame(root)
top_frame.pack(pady=10, fill="x")

entry = ctk.CTkEntry(top_frame, placeholder_text="Enter a location (e.g., Lima, Peru)")
entry.pack(side="left", padx=10, pady=5, fill="x", expand=True)

search_button = ctk.CTkButton(top_frame, text="Search", command=search_location)
search_button.pack(side="left", padx=10, pady=5)

label = ctk.CTkLabel(root, text="")
label.pack(pady=5)

map_frame = ctk.CTkFrame(root)
map_frame.pack(pady=10, fill="both", expand=True)

map_widget = TkinterMapView(map_frame, width=760, height=500, corner_radius=10)
map_widget.set_position(-12.0464, -77.0428)
map_widget.set_zoom(10)
map_widget.pack(fill="both", expand=True)

map_widget.bind_all("<Button-3>", on_map_right_click)

root.mainloop()