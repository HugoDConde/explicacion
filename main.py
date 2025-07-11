from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import askokcancel
from tkinter.colorchooser import askcolor
from pyautogui import size
from threading import Thread
from time import sleep
from keyboard import is_pressed
from os import system
import imageio
from PIL import Image, ImageTk
from tkfontchooser import askfont
from PIL import ImageGrab

x, y = size()
state = "boton1"
oldstate = "boton2"
activado = True
images = 0
destacado_color = "yellow"
fuente_enlaces = "Calibri 20 italic"
fondo_enlaces = "white"
color_letra_enlaces = "blue"
color_poligono = "black"
color_flechas = "black"
grueso_flechas = 3
fuente_texto = "Calibri 20 bold"
color_dibujar = "black"
ancho_dibujar = 2


# Functions
def stream(vid, label):
    video = imageio.get_reader(vid)
    for image in video.iter_data():
        frame_image = ImageTk.PhotoImage(Image.fromarray(image))
        label.config(image=frame_image)
        label.image = frame_image
        ventana.protocol("WM_DELETE_WINDOW", salir)
        if not activado:
            break


def crear_punto(event):
    if is_pressed(' '):
        if state == 'boton1':
            canvas.create_line(event.x, event.y, event.x+1, event.y+1, fill=color_dibujar, width=ancho_dibujar)
            canvas.create_line(event.x+1, event.y, event.x+2, event.y+1, fill=color_dibujar, width=ancho_dibujar)
            canvas.create_line(event.x, event.y+1, event.x+1, event.y+2, fill=color_dibujar, width=ancho_dibujar)
            canvas.create_line(event.x-1, event.y, event.x, event.y+1, fill=color_dibujar, width=ancho_dibujar)
            canvas.create_line(event.x, event.y-1, event.x+1, event.y, fill=color_dibujar, width=ancho_dibujar)
    elif is_pressed('-'):
        canvas.create_line(0, 0, x, y, width=x, fill=canvas["background"])
    elif is_pressed('supr'):
        canvas.create_line(event.x, event.y, event.y+1, event.y+1, width=5, fill="white")
        canvas.create_line(event.x+1, event.y, event.x+2, event.y+1, width=5, fill="white")
        canvas.create_line(event.x, event.y+1, event.x+1, event.y+2, width=5, fill="white")
        canvas.create_line(event.x-1, event.y, event.x, event.y+1, width=5, fill="white")
        canvas.create_line(event.x, event.y-1, event.x+1, event.y, width=5, fill="white")
        canvas.create_line(event.x+1, event.y+1, event.x+2, event.y+2, width=5, fill="white")
        canvas.create_line(event.x-1, event.y-1, event.x, event.y, width=5, fill="white")
        canvas.create_line(event.x+1, event.y+2, event.x+2, event.y+3, width=5, fill="white")
        canvas.create_line(event.x-1, event.y-2, event.x, event.y-1, width=5, fill="white")
        canvas.create_line(event.x-2, event.y-1, event.x-1, event.y, width=5, fill="white")

        canvas.create_line(event.x+1, event.y+1, event.x, event.y, width=5, fill="white")
        canvas.create_line(event.x+2, event.y+1, event.x+1, event.y, width=5, fill="white")
        canvas.create_line(event.x+1, event.y+2, event.x, event.y+1, width=5, fill="white")
        canvas.create_line(event.x, event.y+1, event.x-1, event.y, width=5, fill="white")
        canvas.create_line(event.x+1, event.y, event.x, event.y-1, width=5, fill="white")
        canvas.create_line(event.x+2, event.y+2, event.x+1, event.y+1, width=5, fill="white")
        canvas.create_line(event.x, event.y, event.x-1, event.y-1, width=5, fill="white")
        canvas.create_line(event.x+2, event.y+3, event.x+1, event.y+2, width=5, fill="white")
        canvas.create_line(event.x, event.y-1, event.x-1, event.y-2, width=5, fill="white")
        canvas.create_line(event.x-1, event.y, event.x-2, event.y-1, width=5, fill="white")
        canvas.create_line(event.x, event.y, event.x+1, event.y+1, width=5, fill="white")
        canvas.create_line(event.x+1, event.y, event.x+2, event.y+1, width=5, fill="white")
        canvas.create_line(event.x, event.y+1, event.x+1, event.y+2, width=5, fill="white")
        canvas.create_line(event.x-1, event.y, event.x, event.y+1, width=5, fill="white")
        canvas.create_line(event.x, event.y-1, event.x+1, event.y, width=5, fill="white")
        canvas.create_line(event.x+1, event.y+1, event.x+2, event.y+2, width=5, fill="white")
        canvas.create_line(event.x-1, event.y-1, event.x, event.y, width=5, fill="white")
        canvas.create_line(event.x+1, event.y+2, event.x+2, event.y+3, width=5, fill="white")
        canvas.create_line(event.x-1, event.y-2, event.x, event.y-1, width=5, fill="white")
        canvas.create_line(event.x-2, event.y-1, event.x-1, event.y, width=5, fill="white")

        canvas.create_line(event.x-1, event.y-1, event.x, event.y, width=5, fill="white")
        canvas.create_line(event.x-2, event.y-1, event.x-1, event.y, width=5, fill="white")
        canvas.create_line(event.x-1, event.y-2, event.x, event.y-1, width=5, fill="white")
        canvas.create_line(event.x, event.y-1, event.x+1, event.y, width=5, fill="white")
        canvas.create_line(event.x-1, event.y, event.x, event.y+1, width=5, fill="white")
        canvas.create_line(event.x-2, event.y-2, event.x-1, event.y-1, width=5, fill="white")
        canvas.create_line(event.x, event.y, event.x-1, event.y+1, width=5, fill="white")
        canvas.create_line(event.x-2, event.y-3, event.x-1, event.y-2, width=5, fill="white")
        canvas.create_line(event.x, event.y+1, event.x+1, event.y+2, width=5, fill="white")
        canvas.create_line(event.x+1, event.y, event.x+2, event.y+1, width=5, fill="white")


def add_text(event):
    global images
    if state == 'boton2':

        def poner_texto():
            canvas.create_text(event.x, event.y, text=entrada.get(), font=fuente_texto)
            texto.destroy()

        texto = Toplevel(ventana)
        entrada = Entry(texto, bg="chartreuse", font="Calibri 20")
        entrada.grid(row=0, column=0)
        Button(texto, text="Poner", bg="red", fg="white", font="Broadway 20", command=lambda: poner_texto()).grid(row=0, column=1)
    elif state == 'boton3':
        def crear_flecha(evento):
            canvas.create_line(event.x, event.y, evento.x, evento.y, fill=color_flechas, width=grueso_flechas, arrow=LAST)

        canvas.bind('<Button-3>', crear_flecha)

    elif state == 'boton4':
        puntos = []

        def crear_pol(evento):
            puntos.append((evento.x, evento.y))
            if is_pressed(' '):
                comando = "canvas.create_polygon(*.*, fill=color_poligono)"
                for punto in puntos:
                    comando = comando.replace("*.*", "{}, {}, *.*".format(punto[0], punto[1]))
                comando = comando.replace(", *.*", "")
                exec(comando)

        canvas.bind('<Button-3>', crear_pol)

    elif state == 'boton5':

        def poner_texto():
            enl = enlace.get()
            canvas.create_window(event.x, event.y, window=Button(canvas, text=entrada.get(), bg=fondo_enlaces, font=fuente_enlaces, fg=color_letra_enlaces, command=lambda: system("start {}".format(enl))))
            texto.destroy()

        texto = Toplevel(ventana)
        entrada = Entry(texto, bg="chartreuse", font="Calibri 20")
        entrada.grid(row=0, column=0)
        enlace = Entry(texto, bg="chartreuse", font="Calibri 20")
        enlace.grid(row=0, column=1)
        Button(texto, text="Poner", bg="red", fg="white", font="Broadway 20", command=lambda: poner_texto()).grid(row=1, columnspan=2, column=0)

    elif state == 'boton6':
        def crear_flecha(evento):
            canvas.create_rectangle(event.x, event.y, evento.x, evento.y, fill=destacado_color, stipple='gray50')

        canvas.bind('<Button-3>', crear_flecha)

    elif state == 'boton7':
        file = askopenfilename(title="Elige Imagen", filetypes=(("Image Files", "*.png *.gif"), ("All", "*.*")))
        image = PhotoImage(file=file)
        images += 1
        comand = "ventana.imagen_add{} = image".format(images)
        exec(comand)
        canvas.create_image(event.x, event.y, image=image)

    elif state == 'boton8':
        file = askopenfilename(title="Elige Video", filetypes=(("Image Files", "*.mp4 *.mkv"), ("All", "*.*")))
        mylabel = Label(canvas)
        canvas.create_window(event.x, event.y, window=mylabel)
        Thread(target=stream, args=(file, mylabel)).start()


def comprobar():
    global boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8
    oldstate2 = ""
    while activado:
        if oldstate2 != oldstate:
            comand = "{}.configure(bg=\"blue\")".format(state)
            exec(comand)
            comand = "{}.configure(bg=\"red\")".format(oldstate)
            exec(comand)
            oldstate2 = oldstate
        sleep(0.1)


def escribir():
    global state, oldstate
    oldstate = state
    state = "boton2"


def dibujar():
    global state, oldstate
    oldstate = state
    state = "boton1"


def flechas():
    global state, oldstate
    oldstate = state
    state = "boton3"


def lineas():
    global state, oldstate
    oldstate = state
    state = "boton4"


def enlaces():
    global state, oldstate
    oldstate = state
    state = "boton5"


def destacado():
    global state, oldstate
    oldstate = state
    state = "boton6"


def imagenes():
    global state, oldstate
    oldstate = state
    state = "boton7"


def videos():
    global state, oldstate
    oldstate = state
    state = "boton8"


def salir():
    global activado
    activado = False
    cerrar = askokcancel("Guardar?", "Quieres Guardar el Esquema?")
    if not cerrar:
        ventana.destroy()
    else:
        guardar(canvas)
        ventana.destroy()


def guardar(widget):
    path = asksaveasfilename(title="Guardar", filetypes=(("Imagenes", "*.png *.gif"), ("Todos", "*.*")))
    x1 = ventana.winfo_rootx()+widget.winfo_x()
    y1 = ventana.winfo_rooty()+widget.winfo_y()
    x2 = x1+widget.winfo_width()
    y2 = y1+widget.winfo_height()
    ImageGrab.grab().crop((x1, y1, x2, y2)).save(path)


def DibujarColor():
    global color_dibujar
    color_de_dibujar = askcolor()
    if color_de_dibujar != (None, None):
        color_dibujar = color_de_dibujar[1]


def DibujarGrosor():

    def change():
        global ancho_dibujar
        ancho_dibujar = int(grosor.get())
        panel.destroy()

    def validate(action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed:
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False

    panel = Toplevel(ventana)
    vcmd = (panel.register(validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
    grosor = Entry(panel, bg="chartreuse", font="Helvetica 20", validate='key', validatecommand=vcmd)
    grosor.grid(row=0, column=0)
    Button(panel, text="Cambiar!", font="Broadway 20", bg="red", fg="white", command=lambda: change()).grid(row=0, column=1)



def EscritoFuente():
    global fuente_texto
    font = askfont()
    if font == {}:
        return False
    fuente = str(font['family']).split(" ")[0]+" "+str(font['size'])
    if font['weight'] == "bold":
        fuente += " bold"
    if font['slant'] == "italic":
        fuente += " italic"
    fuente_texto = fuente


def FlechasGrosor():

    def change():
        global grueso_flechas
        grueso_flechas = int(grosor.get())
        panel.destroy()

    def validate(action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed:
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False

    panel = Toplevel(ventana)
    vcmd = (panel.register(validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
    grosor = Entry(panel, bg="chartreuse", font="Helvetica 20", validate='key', validatecommand=vcmd)
    grosor.grid(row=0, column=0)
    Button(panel, text="Cambiar!", font="Broadway 20", bg="red", fg="white", command=lambda: change()).grid(row=0, column=1)


def FlechasColor():
    global color_flechas
    color_de_flechas = askcolor()
    if color_de_flechas != (None, None):
        color_flechas = color_de_flechas[1]


def FormasColor():
    global color_poligono
    color_de_poligono = askcolor()
    if color_de_poligono != (None, None):
        color_poligono = color_de_poligono[1]


def EnlacesFuente():
    global fuente_enlaces
    font = askfont()
    if font == {}:
        return False
    fuente = str(font['family'])+" "+str(font['size'])
    if font['weight'] == "bold":
        fuente += " bold"
    if font['slant'] == "italic":
        fuente += " italic"
    fuente_enlaces = fuente


def EnlacesColor():
    global color_letra_enlaces
    cletra_enlaces = askcolor()
    if cletra_enlaces != (None, None):
        color_letra_enlaces = cletra_enlaces[1]


def EnlacesFondo():
    global fondo_enlaces
    color_fondo_enlaces = askcolor()
    if color_fondo_enlaces != (None, None):
        fondo_enlaces = color_fondo_enlaces[1]


def ResaltadoColor():
    global destacado_color
    color_resaltado = askcolor()
    if color_resaltado != (None, None):
        destacado_color = color_resaltado[1]


def LienzoFondo():
    color_lienzo = askcolor()
    if color_lienzo != (None, None):
        canvas.configure(bg=color_lienzo[1])

    # def cambiar():
    #     try:
    #         canvas.configure(bg=fondolienzo.get())
    #         lienzo_fondo.destroy()
    #     except:
    #         lienzo_fondo.destroy()
    #
    # lienzo_fondo = Toplevel(ventana)
    # fondolienzo = Entry(lienzo_fondo, font="Helvetica 20", bg="chartreuse")
    # fondolienzo.grid(row=0, column=0)
    # Button(lienzo_fondo, text="Cambiar", bg="red", fg="white", font="Broadway 20", command=lambda: cambiar()).grid(row=0, column=1)


ventana = Tk()
ventana.title("Diseños")
ventana.geometry("{}x{}".format(x, y))
ventana.configure(bg="aqua")
ventana.protocol("WM_DELETE_WINDOW", lambda: salir())

menubarra = Menu(ventana, tearoff=False)

menuarchivo = Menu(menubarra, tearoff=False)
menuarchivo.add_command(label="Guardar", command=lambda: guardar(canvas))
menuarchivo.add_separator()
menuarchivo.add_command(label="Salir", command=lambda: salir())
menubarra.add_cascade(label="Archivo", menu=menuarchivo)

menudibujar = Menu(menubarra, tearoff=False)
menudibujar.add_command(label="Color", command=lambda: DibujarColor())
menudibujar.add_command(label="Grosor", command=lambda: DibujarGrosor())
menubarra.add_cascade(label="Dibujo", menu=menudibujar)

menuescribir = Menu(menubarra, tearoff=False)
menuescribir.add_command(label="Fuente", command=lambda: EscritoFuente())
menubarra.add_cascade(label="Escrito", menu=menuescribir)

menuflechas = Menu(menubarra, tearoff=False)
menuflechas.add_command(label="Grosor", command=lambda: FlechasGrosor())
menuflechas.add_command(label="Color", command=lambda: FlechasColor())
menubarra.add_cascade(label="Flechas", menu=menuflechas)

menuformas = Menu(menubarra, tearoff=False)
menuformas.add_command(label="Color", command=lambda: FormasColor())
menubarra.add_cascade(label="Formas", menu=menuformas)

menuenlaces = Menu(menubarra, tearoff=False)
menuenlaces.add_command(label="Fuente", command=lambda: EnlacesFuente())
menuenlaces.add_command(label="Color", command=lambda: EnlacesColor())
menuenlaces.add_command(label="Fondo", command=lambda: EnlacesFondo())
menubarra.add_cascade(label="Enlaces", menu=menuenlaces)

menuresaltado = Menu(menubarra, tearoff=False)
menuresaltado.add_command(label="Color", command=lambda: ResaltadoColor())
menubarra.add_cascade(label="Resaltado", menu=menuresaltado)

menucanvas = Menu(menubarra, tearoff=False)
menucanvas.add_command(label="Fondo", command=lambda: LienzoFondo())
menubarra.add_cascade(label="Lienzo", menu=menucanvas)

ventana.configure(menu=menubarra)

boton1 = Button(ventana, width=3, text="✏", font="Helvetica 31", bg="red", fg="white", command=lambda: dibujar())
boton1.grid(row=0, column=0)
boton2 = Button(ventana, width=3, text="🖊", font="Helvetica 31", bg="red", fg="white", command=lambda: escribir())
boton2.grid(row=1, column=0)
boton3 = Button(ventana, width=3, text="➡", font="Helvetica 31", bg="red", fg="white", command=lambda: flechas())
boton3.grid(row=2, column=0)
boton4 = Button(ventana, width=3, text="⭐", font="Helvetica 31", bg="red", fg="white", command=lambda: lineas())
boton4.grid(row=3, column=0)
boton5 = Button(ventana, width=3, text="📎", font="Helvetica 31", bg="red", fg="white", command=lambda: enlaces())
boton5.grid(row=4, column=0)
boton6 = Button(ventana, width=3, text="🟥", font="Helvetica 31", bg="red", fg="white", command=lambda: destacado())
boton6.grid(row=5, column=0)
boton7 = Button(ventana, width=3, text="🎞", font="Helvetica 31", bg="red", fg="white", command=lambda: imagenes())
boton7.grid(row=6, column=0)
boton8 = Button(ventana, width=3, text="🎥", font="Helvetica 31", bg="red", fg="white", command=lambda: videos())
boton8.grid(row=7, column=0)


canvas = Canvas(ventana, bg="white", width=int(x)-int(x)/15, height=int(y)-int(y)/10)
canvas.grid_propagate(False)
canvas.grid(row=0, column=1, columnspan=100, rowspan=100)
canvas.bind("<Motion>", crear_punto)
canvas.bind("<Button-1>", add_text)

# canvas.create_line(585, 585, 585, 585)
# canvas.create_line(586, 586, 586, 586)
# canvas.create_line(585, 586, 587, 587)
# canvas.create_line(586, 585, 588, 588)
# canvas.create_line(587, 585, 589, 589)
# canvas.create_line(596, 597, 590, 590)

Thread(name="comprobador", target=comprobar).start()

ventana.mainloop()
