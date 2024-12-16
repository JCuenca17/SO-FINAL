import tkinter as tk
from tkinter import messagebox
import subprocess

def ejecutar_script(script):
    #Ejecuta un archivo Python en un nuevo proceso.
    try:
        subprocess.Popen(["python", script])
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo ejecutar {script}: {e}")

def abrir_aplicacion1():
    ventana1 = tk.Toplevel(root)
    ventana1.title("Planificador de Procesos")
    ventana1.geometry("300x300")

    etiqueta = tk.Label(ventana1, text="Elija el tipo de algoritmo", font=("Helvetica", 12))
    etiqueta.pack(pady=10)

    botones = [
        ("FCFS", lambda: ejecutar_script("fcfs_scheduler.py")),
        ("RR", lambda: ejecutar_script("rr_scheduler.py")),
        ("SJF", lambda: ejecutar_script("sjf_scheduler.py")),
        ("Prioridad", lambda: ejecutar_script("Prioridad.py")),
        ("RR con Prioridad", lambda: ejecutar_script("RR_Prioridad.py"))
    ]

    for texto, comando in botones:
        boton = tk.Button(ventana1, text=texto, command=comando, width=20, height=2)
        boton.pack(pady=5)

def abrir_aplicacion2():
    ventana2 = tk.Toplevel(root)
    ventana2.title("Gestión de Memoria")
    ventana2.geometry("300x300")

    etiqueta = tk.Label(ventana2, text="Elija el tipo de algoritmo", font=("Helvetica", 12))
    etiqueta.pack(pady=10)

    botones = [
        ("Paginación", lambda: ejecutar_script("paginacion.py")),
        ("Segmentación", lambda: ejecutar_script("segmentacion.py")),
        ("Segmentación Paginada", lambda: ejecutar_script("segmentacion_paginada.py"))
    ]

    for texto, comando in botones:
        boton = tk.Button(ventana2, text=texto, command=comando, width=20, height=2)
        boton.pack(pady=5)

def abrir_logo():
    respuesta = messagebox.askokcancel("Apagar Sistema Operativo", "¿Estás seguro de que deseas Apagar el Sistema Operativo?")
    if respuesta:
        root.destroy()

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema Operativo")
root.geometry("1200x700")
root.configure(bg="lightblue")

# Calcular la posición para centrar la ventana
root.update_idletasks()
ancho = root.winfo_width()
alto = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (ancho // 2)
y = (root.winfo_screenheight() // 2) - (alto // 2)
root.geometry(f'{ancho}x{alto}+{x}+{y}')

# Crear una barra de tareas (opcional)
barra_tareas = tk.Frame(root, bg="darkgrey", height=30)
barra_tareas.pack(side="bottom", fill="x")

# Crear un área de escritorio
escritorio = tk.Frame(root, bg="lightblue")
escritorio.pack(expand=True, fill="both")

# Imagen de botones:
img_logo = tk.PhotoImage(file="apagar.png")
img_logo1 = tk.PhotoImage(file="cpu.png")
img_logo2 = tk.PhotoImage(file="memoria-ram.png")

# Crear los botones de las aplicaciones
boton_app1 = tk.Button(escritorio, image=img_logo1, bg="lightblue", command=abrir_aplicacion1, width=64, height=64)
boton_app2 = tk.Button(escritorio, image=img_logo2, bg="lightblue", command=abrir_aplicacion2, width=64, height=64)

# Crear etiquetas debajo de los botones
etiqueta_boton1 = tk.Label(escritorio, text="Planificador de Procesos", bg="lightblue", font=("Helvetica", 10))
etiqueta_boton2 = tk.Label(escritorio, text="Gestión de Memoria", bg="lightblue", font=("Helvetica", 10))

# Crear el botón del logo del SO
boton_logo = tk.Button(barra_tareas, image=img_logo, bg="darkgrey", command=abrir_logo, width=32, height=32)

# Posicionar los botones en el escritorio
boton_app1.place(x=100, y=100)
boton_app2.place(x=100, y=200)

# Posicionar las etiquetas debajo de los botones
etiqueta_boton1.place(x=100, y=160)
etiqueta_boton2.place(x=100, y=260)

# Posicionar el botón del logo del SO en la barra de tareas
boton_logo.pack(side="left", padx=10)

# Crear algunos elementos visuales adicionales
etiqueta_titulo = tk.Label(escritorio, text="Escritorio Simulado", bg="lightblue", font=("Helvetica", 16))
etiqueta_titulo.pack(pady=20)

# Crear etiqueta para mostrar la fecha y hora en la esquina inferior derecha
fecha_hora = tk.Label(root, text="19/12/2024 11:20", bg="gray", font=("Helvetica", 10))
fecha_hora.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

# Ejecutar la aplicación
root.mainloop()
