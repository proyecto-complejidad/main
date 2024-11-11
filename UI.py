from Librerias import *


# Configurar el tamaño de la ventana
anchoVentana = 900
altoVentana = 600


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
        for FR in (FMenuPrincipal, FCreditos, FInstrucciones, FElegirUbicacion): # Poner todos los frames en el for
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
        self.volver_button.place(relx=0.52, rely=0.25, anchor="center")


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
            bg_color="#f1f0f1",
            fg_color="#f1f0f1",
            hover_color="#f1f0f1",
            text="",
            command=lambda: controller.show_frame(FMenuPrincipal)
        )
        self.volver_button.place(relx=0.52, rely=0.25, anchor="center")


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

        entryx =customtkinter.CTkEntry(self, width=125, height=30, state="disabled")
        entryx.place(relx=0.13, rely=0.4, anchor="center")

        entryy = customtkinter.CTkEntry(self, width=125, height=30, state="disabled")
        entryy.place(relx=0.40, rely=0.4, anchor="center")

        self.map_frame = customtkinter.CTkFrame(self, width=405, height=600)
        self.map_frame.place(relx=0.775, rely=0.5, anchor="center")

        map_widget = tkintermapview.TkinterMapView(self.map_frame, width=405, height=600)
        map_widget.set_position(-12.0464, -77.0428)
        map_widget.set_zoom(10)
        map_widget.place(relx=0.5, rely=0.5, anchor="center")

        # Function to handle map right-click events
        def on_map_right_click(coordinates_tuple):
            lat, lon = coordinates_tuple
            entryx.configure(state="normal")
            entryx.insert(0, f"{lon}")
            entryx.configure(state="disabled")
            entryy.configure(state="normal")
            entryy.insert(0, f"{lat}")
            entryy.configure(state="disabled")
            map_widget.delete_all_marker()
            # Place a marker at the clicked position and store the marker object
            marker = map_widget.set_marker(lat, lon, text="Selected Location")

        map_widget.add_left_click_map_command(on_map_right_click)

class FElegirDistribucion(customtkinter.CTkFrame):
    pass

class FElegirBotica(customtkinter.CTkFrame):
    pass

class FMostrarCaminoMinimo(customtkinter.CTkFrame):
    pass

class FMostrarArbolExpansionMinima(customtkinter.CTkFrame):
    pass