import customtkinter
import tkintermapview

from Librerias import *
from Controlador import *

# Configurar el tamaño de la ventana
anchoVentana = 900
altoVentana = 600

# controlador global
controlador = Controlador()

lati = 0
loni = 0

# Clase de la aplicacion general
class Aplicacion(customtkinter.CTk):
    def __init__(self):
        # Configuracion para la app (customtkinter)
        super().__init__()
        self.title("MediK")
        self.geometry(f"{anchoVentana}x{altoVentana}")

        self.container = customtkinter.CTkFrame(self, corner_radius=0, bg_color="#050a30")
        self.container.pack(fill="both", expand=True)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Codigo para iterar entre todos los frames
        for FR in (FMenuPrincipal, FCreditos, FInstrucciones, FElegirUbicacion, FElegirDistribucion, FElegirBotica,FMostrarArbolExpansionMinima, FMostrarCaminoMinimo, FMostrarRutaCorta): # Poner todos los frames en el for
            frame = FR(self.container, self)
            self.frames[FR] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(FMenuPrincipal)

    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()


# - - - - - - - - - - - - - - - - - - - - - -
# - F R A M E   M E N U   P R I N C I P A L -
# - - - - - - - - - - - - - - - - - - - - - -
# Este frame será el primero en mostrarse al iniciar el programa
class FMenuPrincipal(customtkinter.CTkFrame):
    # Inicializador para el menu inicio
    def __init__(self, parent, controller):
        controlador.crear_grafo_og()
        super().__init__(parent)
        self.controller = controller

        self.f_menu_principal = customtkinter.CTkFrame(self)
        self.f_menu_principal.grid(row=0, column=0, sticky="nsew")

        self.f_menu_principal.grid_rowconfigure(2, weight=1)
        self.f_menu_principal.grid_columnconfigure(0, weight=1)
        self.f_menu_principal.grid_columnconfigure(1, weight=1)

        # Imagen de fondo del menu inicio
        bg_menu_inicio1 = Image.open("Assets/fondo_menu_principal.png")
        bg_menu_inicio2 = customtkinter.CTkImage(
            light_image=bg_menu_inicio1.resize((anchoVentana, altoVentana)),
            dark_image=bg_menu_inicio1.resize((anchoVentana, altoVentana)),
            size=(anchoVentana, altoVentana)
        )
        bg_menu_inicio3 = customtkinter.CTkLabel(self.f_menu_principal, text="", image=bg_menu_inicio2)
        bg_menu_inicio3.image = bg_menu_inicio2
        bg_menu_inicio3.pack(fill="both", expand=True)

        # Tamaño para los botones
        btn_size_width = 190
        btn_size_height = 70

        # Boton para empezar el programa
        btn_iniciar_im = Image.open("Assets/btn_comenzar_programa.png")
        btn_iniciar_resize = btn_iniciar_im
        btn_iniciar_ctk = (customtkinter.CTkImage(
            light_image=btn_iniciar_resize.resize((btn_size_width, btn_size_height)),
            dark_image=btn_iniciar_resize.resize((btn_size_width, btn_size_height)),
            size=(btn_size_width, btn_size_height))
        )

        self.btn_iniciar_button = customtkinter.CTkButton(
            self,
            width=btn_size_width,
            height=btn_size_height,
            image=btn_iniciar_ctk,
            bg_color="#f1f0f1",
            fg_color="#f1f0f1",
            hover_color="#f1f0f1",
            text="",
            command=lambda: controller.show_frame(FElegirUbicacion) # mostrar el frame al precionar el boton
        )
        self.btn_iniciar_button.place(relx=0.25, rely=0.6, anchor="center")

        # Boton para mostrar los creditos
        btn_creditos_im = Image.open("Assets/btn_creditos.png")
        btn_creditos_resize = btn_creditos_im
        btn_creditos_ctk = (customtkinter.CTkImage(
            light_image=btn_creditos_resize.resize((btn_size_width, btn_size_height)),
            dark_image=btn_creditos_resize.resize((btn_size_width, btn_size_height)),
            size=(btn_size_width, btn_size_height)
        )
        )
        self.creditos_button = customtkinter.CTkButton(
            self,
            width=btn_size_width,
            height=btn_size_height,
            image=btn_creditos_ctk,
            bg_color="#f1f0f1",
            fg_color="#f1f0f1",
            hover_color="#f1f0f1",
            text="",
            command=lambda: controller.show_frame(FCreditos)
        )
        self.creditos_button.place(relx=0.5, rely=0.6, anchor="center")

        # Boton para mostrar las instrucciones
        btn_instrucciones_im = Image.open("Assets/btn_instrucciones.png")
        btn_instrucciones_resize = btn_instrucciones_im
        btn_instrucciones_ctk = (customtkinter.CTkImage(
            light_image=btn_instrucciones_resize.resize((btn_size_width, btn_size_height)),
            dark_image=btn_instrucciones_resize.resize((btn_size_width, btn_size_height)),
            size=(btn_size_width, btn_size_height))
        )

        self.btn_instrucciones_button = customtkinter.CTkButton(
            self,
            width=btn_size_width,
            height=btn_size_height,
            image=btn_instrucciones_ctk,
            bg_color="#f1f0f1",
            fg_color="#f1f0f1",
            hover_color="#f1f0f1",
            text="",
            command=lambda: controller.show_frame(FInstrucciones)  # mostrar el frame al precionar el boton
        )
        self.btn_instrucciones_button.place(relx=0.75, rely=0.6, anchor="center")


# - - - - - - - - - - - - - - - -
# - F R A M E   C R E D I T O S -
# - - - - - - - - - - - - - - - -
# Este frame será para mostrar los creditos
class FCreditos(customtkinter.CTkFrame):
    # Inicializador para el frame de creditos
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.credits_frame = customtkinter.CTkFrame(self)
        self.credits_frame.grid(row=0, column=0, sticky="nsew")

        self.credits_frame.grid_rowconfigure(2, weight=1)
        self.credits_frame.grid_columnconfigure(0, weight=1)
        self.credits_frame.grid_columnconfigure(1, weight=1)

        ### Imagen de fondo del frame Creditos
        bg_creditos1 = Image.open("Assets/fondo_creditos.png")
        bg_creditos2 = customtkinter.CTkImage(
            light_image=bg_creditos1.resize((anchoVentana, altoVentana)),
            dark_image=bg_creditos1.resize((anchoVentana, altoVentana)),
            size=(anchoVentana, altoVentana)
        )

        bg_creditos3 = customtkinter.CTkLabel(self.credits_frame, text="", image=bg_creditos2)
        bg_creditos3.image = bg_creditos2
        bg_creditos3.pack(fill="both", expand=True)

        ### Tamaño para los botones
        btn_size_width = 160
        btn_size_height = 60

        # Boton para regresar al menu
        btn_volver_im = Image.open("Assets/btn_volver.png")
        btn_volver_resize = btn_volver_im
        btn_volver_ctk = (customtkinter.CTkImage(
            light_image=btn_volver_resize.resize((btn_size_width, btn_size_height)),
            dark_image=btn_volver_resize.resize((btn_size_width, btn_size_height)),
            size=(btn_size_width, btn_size_height)
        )
        )
        self.volver_button = customtkinter.CTkButton(
            self,
            width=btn_size_width,
            height=btn_size_height,
            image=btn_volver_ctk,
            bg_color="#f1f0f1",
            fg_color="#f1f0f1",
            hover_color="#f1f0f1",
            text="",
            command=lambda: controller.show_frame(FMenuPrincipal)
        )
        self.volver_button.place(relx=0.5, rely=0.9, anchor="center")


# - - - - - - - - - - - - - - - - - - - - -
# - F R A M E   I N S T R U C C I O N E S -
# - - - - - - - - - - - - - - - - - - - - -
# Este frame será para mostrar las instrucciones
class FInstrucciones(customtkinter.CTkFrame):
    # Inicializador para el frame de instrucciones
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.credits_frame = customtkinter.CTkFrame(self)
        self.credits_frame.grid(row=0, column=0, sticky="nsew")

        self.credits_frame.grid_rowconfigure(2, weight=1)
        self.credits_frame.grid_columnconfigure(0, weight=1)
        self.credits_frame.grid_columnconfigure(1, weight=1)

        ### Imagen de fondo del frame Creditos
        bg_creditos1 = Image.open("Assets/fondo_instrucciones.png")
        bg_creditos2 = customtkinter.CTkImage(
            light_image=bg_creditos1.resize((anchoVentana, altoVentana)),
            dark_image=bg_creditos1.resize((anchoVentana, altoVentana)),
            size=(anchoVentana, altoVentana)
        )

        bg_creditos3 = customtkinter.CTkLabel(self.credits_frame, text="", image=bg_creditos2)
        bg_creditos3.image = bg_creditos2
        bg_creditos3.pack(fill="both", expand=True)

        ### Tamaño para los botones
        btn_size_width = 160
        btn_size_height = 60

        # Boton para regresar al menu
        btn_volver_im = Image.open("Assets/btn_volver.png")
        btn_volver_resize = btn_volver_im
        btn_volver_ctk = (customtkinter.CTkImage(
            light_image=btn_volver_resize.resize((btn_size_width, btn_size_height)),
            dark_image=btn_volver_resize.resize((btn_size_width, btn_size_height)),
            size=(btn_size_width, btn_size_height)
        )
        )
        self.volver_button = customtkinter.CTkButton(
            self,
            width=btn_size_width,
            height=btn_size_height,
            image=btn_volver_ctk,
            bg_color="#ccdffe",
            fg_color="#ccdffe",
            hover_color="#ccdffe",
            text="",
            command=lambda: controller.show_frame(FMenuPrincipal)
        )
        self.volver_button.place(relx=0.46, rely=0.47, anchor="center")


class FElegirUbicacion(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.ele_ubi_frame = customtkinter.CTkFrame(self)
        self.ele_ubi_frame.grid(row=0, column=0, sticky="nsew")

        self.ele_ubi_frame.grid_rowconfigure(2, weight=1)
        self.ele_ubi_frame.grid_columnconfigure(0, weight=1)
        self.ele_ubi_frame.grid_columnconfigure(1, weight=1)

        imagen = Image.open("Assets/fondo_seleccionar_ubicacion.png")
        bg_imagen = customtkinter.CTkImage(light_image=imagen.resize((anchoVentana, altoVentana)),
                                           dark_image=imagen.resize((anchoVentana, altoVentana)),
                                           size=(anchoVentana, altoVentana))
        bg_imagen_l = customtkinter.CTkLabel(self.ele_ubi_frame, text="", image=bg_imagen)
        bg_imagen_l.image = bg_imagen
        bg_imagen_l.pack(fill="both", expand=True)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.lat = 0
        self.lon = 0

        entryx = customtkinter.CTkEntry(self, width=125, height=30, state="disabled")
        entryx.place(relx=0.13, rely=0.4, anchor="center")

        entryy = customtkinter.CTkEntry(self, width=125, height=30, state="disabled")
        entryy.place(relx=0.40, rely=0.4, anchor="center")

        self.map_frame = customtkinter.CTkFrame(self, width=405, height=600)
        self.map_frame.place(relx=0.775, rely=0.5, anchor="center")

        map_widget = tkintermapview.TkinterMapView(self.map_frame, width=405, height=600)
        map_widget.set_position(-12.0464, -77.0428)
        map_widget.set_zoom(10)
        map_widget.place(relx=0.5, rely=0.5, anchor="center")

        # Tamaño para los botones
        btn_size_width = 190
        btn_size_height = 70

        # Boton si se elige hacer la matriz aleatoria
        btn_sel_ubi_im = Image.open("Assets/btn_seleccionar_ubicacion.png")
        btn_sel_ubi_resize = btn_sel_ubi_im
        btn_sel_ubi_ctk = (customtkinter.CTkImage(
            light_image=btn_sel_ubi_resize.resize((btn_size_width, btn_size_height)),
            dark_image=btn_sel_ubi_resize.resize((btn_size_width, btn_size_height)),
            size=(btn_size_width, btn_size_height)
        )
        )

        def p_btn_ubi():
            controlador.insertar_nuevo_nodo("Almacen", self.lat, self.lon)
            controller.show_frame(FElegirDistribucion)

        self.btn_sel_ubi = customtkinter.CTkButton(
            self,
            state="disabled",
            width=btn_size_width,
            height=btn_size_height,
            image=btn_sel_ubi_ctk,
            bg_color="#ccdffe",
            fg_color="#ccdffe",
            hover_color="#ccdffe",
            text="",
            command= p_btn_ubi
        )
        self.btn_sel_ubi.place(relx =0.26, rely=0.6, anchor="center")

        polygon1 = map_widget.set_polygon(
            [(0, 0)],
            fill_color = "Green"
        )

        # Function to handle map right-click events
        def on_map_right_click(coordinates_tuple):
            self.lat, self.lon = coordinates_tuple
            controlador.lati = self.lat
            controlador.loni = self.lon
            entryx.configure(state="normal")
            entryx.insert(0, f"{self.lon}")
            entryx.configure(state="disabled")
            entryy.configure(state="normal")
            entryy.insert(0, f"{self.lat}")
            entryy.configure(state="disabled")
            map_widget.delete_all_marker()
            self.btn_sel_ubi.configure(state="normal")
            # Place a marker at the clicked position and store the marker object
            marker = map_widget.set_marker(self.lat, self.lon, text="Selected Location")

        def add_polygon_vertice(coords):
            if not controlador.booleano:
                polygon1.remove_position(0, 0)
                controlador.booleano = True

            polygon1.add_position(coords[0], coords[1])

        map_widget.add_left_click_map_command(on_map_right_click)
        map_widget.add_right_click_menu_command(label="Añadir Cerca", command=add_polygon_vertice, pass_coords=True)


class FElegirDistribucion(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.ele_dis_frame = customtkinter.CTkFrame(self)
        self.ele_dis_frame.grid(row=0, column=0, sticky="nsew")

        self.ele_dis_frame.grid_rowconfigure(2, weight=1)
        self.ele_dis_frame.grid_columnconfigure(0, weight=1)
        self.ele_dis_frame.grid_columnconfigure(1, weight=1)

        imagen = Image.open("Assets/fondo_elegir_distribucion.png")
        bg_imagen = customtkinter.CTkImage(light_image=imagen.resize((anchoVentana, altoVentana)),
                                           dark_image=imagen.resize((anchoVentana, altoVentana)),
                                           size=(anchoVentana, altoVentana))
        bg_imagen_l = customtkinter.CTkLabel(self.ele_dis_frame, text="", image=bg_imagen)
        bg_imagen_l.image = bg_imagen
        bg_imagen_l.pack(fill="both", expand=True)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Tamaño para los botones
        btn_size_width = 190
        btn_size_height = 70

        # Boton si se elige hacer la matriz aleatoria
        btn_una_sol_im = Image.open("Assets/btn_una_sola_botica.png")
        btn_una_sol_resize = btn_una_sol_im
        btn_una_sol_ctk = (customtkinter.CTkImage(
            light_image=btn_una_sol_resize.resize((btn_size_width, btn_size_height)),
            dark_image=btn_una_sol_resize.resize((btn_size_width, btn_size_height)),
            size=(btn_size_width, btn_size_height)
        )
        )

        self.btn_una_sol_button = customtkinter.CTkButton(
            self,
            width=btn_size_width,
            height=btn_size_height,
            image=btn_una_sol_ctk,
            bg_color="#ccdffe",
            fg_color="#ccdffe",
            hover_color="#ccdffe",
            text="",
            command=lambda: controller.show_frame(FElegirBotica)
        )
        self.btn_una_sol_button.place(relx=0.25, rely=0.6, anchor="center")

        # Boton si se elije hacer la matriz manual
        btn_todas_im = Image.open("Assets/btn_todas_las_boticas.png")
        btn_todas_resize = btn_todas_im
        btn_todas_ctk = (customtkinter.CTkImage(
            light_image=btn_todas_resize.resize((btn_size_width, btn_size_height)),
            dark_image=btn_todas_resize.resize((btn_size_width, btn_size_height)),
            size=(btn_size_width, btn_size_height)
        )
        )

        def ejecutar_kruskal():
            controlador.kruskal()
            controller.show_frame(FMostrarArbolExpansionMinima)

        self.btn_todas = customtkinter.CTkButton(
            self,
            width=btn_size_width,
            height=btn_size_height,
            image=btn_todas_ctk,
            bg_color="#ccdffe",
            fg_color="#ccdffe",
            hover_color="#ccdffe",
            text="",
            command=ejecutar_kruskal
        )
        self.btn_todas.place(relx=0.75, rely=0.6, anchor="center")


class FElegirBotica(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.ele_bot_frame = customtkinter.CTkFrame(self)
        self.ele_bot_frame.grid(row=0, column=0, sticky="nsew")

        self.ele_bot_frame.grid_rowconfigure(2, weight=1)
        self.ele_bot_frame.grid_columnconfigure(0, weight=1)
        self.ele_bot_frame.grid_columnconfigure(1, weight=1)

        imagen = Image.open("Assets/fondo_elegir_distribucion.png")
        bg_imagen = customtkinter.CTkImage(light_image=imagen.resize((anchoVentana, altoVentana)),
                                           dark_image=imagen.resize((anchoVentana, altoVentana)),
                                           size=(anchoVentana, altoVentana))
        bg_imagen_l = customtkinter.CTkLabel(self.ele_bot_frame, text="", image=bg_imagen)
        bg_imagen_l.image = bg_imagen
        bg_imagen_l.pack(fill="both", expand=True)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        entry_boti = customtkinter.CTkEntry(self, width=350, height=50)
        entry_boti.place(relx=0.5, rely=0.4, anchor="center")

        # Tamaño para los botones
        btn_size_width = 190
        btn_size_height = 70

        # Boton si se elige hacer la matriz aleatoria
        btn_bus_boti_im = Image.open("Assets/btn_buscar_botica.png")
        btn_bus_boti_resize = btn_bus_boti_im
        btn_bus_boti_ctk = customtkinter.CTkImage(
            light_image=btn_bus_boti_resize.resize((btn_size_width, btn_size_height)),
            dark_image=btn_bus_boti_resize.resize((btn_size_width, btn_size_height)),
            size=(btn_size_width, btn_size_height)
        )

        def btn_dijsktra():
            if controlador.buscar_botica(entry_boti.get()):
                controlador.dijsktra(entry_boti.get())
                controller.show_frame(FMostrarCaminoMinimo)
            else:
                pass

        self.btn_bus_boti_button = customtkinter.CTkButton(
            self,
            width=btn_size_width,
            height=btn_size_height,
            image=btn_bus_boti_ctk,
            bg_color="#ccdffe",
            fg_color="#ccdffe",
            hover_color="#ccdffe",
            text="",
            command=btn_dijsktra
        )
        self.btn_bus_boti_button.place(relx=0.5, rely=0.6, anchor="center")


class FMostrarCaminoMinimo(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.min_cam_frame = customtkinter.CTkFrame(self)
        self.min_cam_frame.grid(row=0, column=0, sticky="nsew")

        self.min_cam_frame.grid_rowconfigure(2, weight=1)
        self.min_cam_frame.grid_columnconfigure(0, weight=1)
        self.min_cam_frame.grid_columnconfigure(1, weight=1)

        imagen = Image.open("Assets/fondo_camino_mas_corto.png")
        bg_imagen = customtkinter.CTkImage(light_image=imagen.resize((anchoVentana, altoVentana)),
                                           dark_image=imagen.resize((anchoVentana, altoVentana)),
                                           size=(anchoVentana, altoVentana))
        bg_imagen_l = customtkinter.CTkLabel(self.min_cam_frame, text="", image=bg_imagen)
        bg_imagen_l.image = bg_imagen
        bg_imagen_l.pack(fill="both", expand=True)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Tamaño para los botones
        btn_size_width = 190
        btn_size_height = 70

        # Boton si se elige hacer la matriz aleatoria
        btn_kruskal_im = Image.open("Assets/btn_mostra_datos.png")
        btn_kruskal_resize = btn_kruskal_im
        btn_kruskal_ctk = customtkinter.CTkImage(
            light_image=btn_kruskal_resize.resize((btn_size_width, btn_size_height)),
            dark_image=btn_kruskal_resize.resize((btn_size_width, btn_size_height)),
            size=(btn_size_width, btn_size_height)
        )

        def btn_mostrardatos():
            distancia = round(controlador.distancia_kruskal, 5)

            entryl = customtkinter.CTkEntry(self, width=175, height=30)
            entryl.insert(0, f"{controlador.lati}")
            entryl.configure(state="disabled")
            entryl.place(relx=0.4, rely=0.36, anchor="center")

            entryl2 = customtkinter.CTkEntry(self, width=175, height=30)
            entryl2.insert(0, f"{controlador.loni}")
            entryl2.configure(state="disabled")
            entryl2.place(relx=0.4, rely=0.46, anchor="center")

            entryl3 = customtkinter.CTkEntry(self, width=175, height=30)
            entryl3.insert(0, f"{controlador.dij_lat}")
            entryl3.configure(state="disabled")
            entryl3.place(relx=0.80, rely=0.36, anchor="center")

            entryl4 = customtkinter.CTkEntry(self, width=175, height=30)
            entryl4.insert(0, f"{controlador.dij_lon}")
            entryl4.configure(state="disabled")
            entryl4.place(relx=0.80, rely=0.46, anchor="center")

            entryl5 = customtkinter.CTkEntry(self, width=175, height=30)
            entryl5.insert(0, f"{round(controlador.dij_dis, 3)} km")
            entryl5.configure(state="disabled")
            entryl5.place(relx=0.4, rely=0.77, anchor="center")

        self.btn_min_cam_button = customtkinter.CTkButton(
            self,
            width=btn_size_width,
            height=btn_size_height,
            image=btn_kruskal_ctk,
            bg_color="#ccdffe",
            fg_color="#ccdffe",
            hover_color="#ccdffe",
            text="",
            command=btn_mostrardatos
        )
        self.btn_min_cam_button.place(relx=0.75, rely=0.9, anchor="center")

        # Boton si se elige hacer la matriz aleatoria
        btn_rut_cor_im = Image.open("Assets/btn_mostrar_ruta_mas_corta.png")
        btn_rut_cor_resize = btn_rut_cor_im
        btn_rut_cor_ctk = customtkinter.CTkImage(
            light_image=btn_rut_cor_resize.resize((btn_size_width, btn_size_height)),
            dark_image=btn_rut_cor_resize.resize((btn_size_width, btn_size_height)),
            size=(btn_size_width, btn_size_height)
        )

        def f_mostrar_ruta_mas_corta():
            controller.show_frame(FMostrarRutaCorta)

        self.btn_rut_cor_button = customtkinter.CTkButton(
            self,
            width=btn_size_width,
            height=btn_size_height,
            image=btn_rut_cor_ctk,
            bg_color="#ccdffe",
            fg_color="#ccdffe",
            hover_color="#ccdffe",
            text="",
            command=f_mostrar_ruta_mas_corta
        )
        self.btn_rut_cor_button.place(relx=0.75, rely=0.75, anchor="center")

class FMostrarArbolExpansionMinima(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.kruskal_frame = customtkinter.CTkFrame(self)
        self.kruskal_frame.grid(row=0, column=0, sticky="nsew")

        self.kruskal_frame.grid_rowconfigure(2, weight=1)
        self.kruskal_frame.grid_columnconfigure(0, weight=1)
        self.kruskal_frame.grid_columnconfigure(1, weight=1)

        imagen = Image.open("Assets/fondo_mst.png")
        bg_imagen = customtkinter.CTkImage(light_image=imagen.resize((anchoVentana, altoVentana)),
                                           dark_image=imagen.resize((anchoVentana, altoVentana)),
                                           size=(anchoVentana, altoVentana))
        bg_imagen_l = customtkinter.CTkLabel(self.kruskal_frame, text="", image=bg_imagen)
        bg_imagen_l.image = bg_imagen
        bg_imagen_l.pack(fill="both", expand=True)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Tamaño para los botones
        btn_size_width = 190
        btn_size_height = 70

        # Boton si se elige hacer la matriz aleatoria
        btn_kruskal_im = Image.open("Assets/btn_mostra_datos.png")
        btn_kruskal_resize = btn_kruskal_im
        btn_kruskal_ctk = customtkinter.CTkImage(
            light_image=btn_kruskal_resize.resize((btn_size_width, btn_size_height)),
            dark_image=btn_kruskal_resize.resize((btn_size_width, btn_size_height)),
            size=(btn_size_width, btn_size_height)
        )

        def btn_mostrardatos():
            distancia = round(controlador.distancia_kruskal, 5)

            entryl = customtkinter.CTkEntry(self.kruskal_frame, width=200, height=40)
            entryl.insert(0, f"{controlador.lati}")
            entryl.configure(state="disabled")
            entryl.place(relx=0.28, rely=0.42, anchor="center")

            entryl2 = customtkinter.CTkEntry(self.kruskal_frame, width=200, height=40)
            entryl2.insert(0, f"{controlador.loni}")
            entryl2.configure(state="disabled")
            entryl2.place(relx=0.28, rely=0.52, anchor="center")

            label = customtkinter.CTkLabel(
                self.kruskal_frame,
                text=f"{distancia} km"
            )
            label.place(relx=0.25, rely=0.75, anchor="center")

            imagen = Image.open("grafo_mst_maximized.png")
            imagen_ctk = customtkinter.CTkImage(imagen, size=(400, 600))

            label_imagen = customtkinter.CTkLabel(self, image=imagen_ctk, text="")
            label_imagen.place(relx=0.72, rely=0.5, anchor="center")

        self.btn_kruskal_button = customtkinter.CTkButton(
            self,
            width=btn_size_width,
            height=btn_size_height,
            image=btn_kruskal_ctk,
            bg_color="#ccdffe",
            fg_color="#ccdffe",
            hover_color="#ccdffe",
            text="",
            command=btn_mostrardatos
        )
        self.btn_kruskal_button.place(relx=0.3, rely=0.87, anchor="center")


class FMostrarRutaCorta(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.ele_ubi_frame = customtkinter.CTkFrame(self)
        self.ele_ubi_frame.grid(row=0, column=0, sticky="nsew")

        self.ele_ubi_frame.grid_rowconfigure(2, weight=1)
        self.ele_ubi_frame.grid_columnconfigure(0, weight=1)
        self.ele_ubi_frame.grid_columnconfigure(1, weight=1)

        imagen = Image.open("Assets/fondo_grafico_camino_corto.png")
        bg_imagen = customtkinter.CTkImage(light_image=imagen.resize((anchoVentana, altoVentana)),
                                           dark_image=imagen.resize((anchoVentana, altoVentana)),
                                           size=(anchoVentana, altoVentana))
        bg_imagen_l = customtkinter.CTkLabel(self.ele_ubi_frame, text="", image=bg_imagen)
        bg_imagen_l.image = bg_imagen
        bg_imagen_l.pack(fill="both", expand=True)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.map_frame = customtkinter.CTkFrame(self, width=600, height=350)
        self.map_frame.place(relx=0.5, rely=0.55, anchor="center")

        map_widget = tkintermapview.TkinterMapView(self.map_frame, width=700, height=450)
        map_widget.set_position(-12.0464, -77.0428)
        map_widget.set_zoom(10)
        map_widget.place(relx=0.5, rely=0.57, anchor="center")

        # Tamaño para los botones
        btn_size_width = 190
        btn_size_height = 70

        # Boton si se elige hacer la matriz aleatoria
        btn_sel_ubi_im = Image.open("Assets/btn_seleccionar_ubicacion.png")
        btn_sel_ubi_resize = btn_sel_ubi_im
        btn_sel_ubi_ctk = (customtkinter.CTkImage(
            light_image=btn_sel_ubi_resize.resize((btn_size_width, btn_size_height)),
            dark_image=btn_sel_ubi_resize.resize((btn_size_width, btn_size_height)),
            size=(btn_size_width, btn_size_height)
        )
        )

        def p_boton_mpoli():
            print(f"({controlador.lati}, {controlador.loni}), ({controlador.dij_lat}, {controlador.dij_lon})")
            polygon1 = map_widget.set_polygon(
                [(float(controlador.lati), float(controlador.loni)), (float(controlador.dij_lat) - 0.05, float(controlador.dij_lon) - 0.02)],
            )
            polygon2 = map_widget.set_polygon(
                [(float(controlador.dij_lat) - 0.05, float(controlador.dij_lon) - 0.02), (float(controlador.dij_lat), float(controlador.dij_lon))]
            )
            marker = map_widget.set_marker(float(controlador.lati), float(controlador.loni), text="Selected Location")
            marker = map_widget.set_marker(float(controlador.dij_lat), float(controlador.dij_lon), text="Selected Location")

        self.btn_sel_ubi = customtkinter.CTkButton(
            self,
            width=btn_size_width,
            height=btn_size_height,
            image=btn_sel_ubi_ctk,
            bg_color="#ccdffe",
            fg_color="#ccdffe",
            hover_color="#ccdffe",
            text="",
            command= p_boton_mpoli
        )
        self.btn_sel_ubi.place(relx =0.5, rely=0.93, anchor="center")
