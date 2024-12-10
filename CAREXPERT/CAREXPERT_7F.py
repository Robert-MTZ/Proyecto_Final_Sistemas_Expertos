# Roberto Martinez Bailón 21310216
# Sistemas Expertos

import tkinter as tk
from tkinter import messagebox
import sqlite3
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk



# Función para obtener datos de la base de datos
def obtener_datos(tabla, tipo_falla_id):
    conn = sqlite3.connect("CarExpert.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT descripcion FROM {tabla} WHERE tipo_falla_id = ?", (tipo_falla_id,))
    datos = cursor.fetchall()
    conn.close()
    return [d[0] for d in datos]

# Función para mostrar la ventana principal
def mostrar_menu_principal():
    for widget in ventana.winfo_children():
        widget.destroy()

    ventana.title("CarExpert")
    tk.Label(ventana, text="CarExpert", font=("Arial", 24)).pack(pady=10)
    tk.Label(ventana, text="Hola, ¿qué tipo de falla quieres solucionar?", font=("Arial", 16)).pack(pady=20)

    tk.Button(ventana, text="Combustión", font=("Arial", 14), command=lambda: mostrar_sintomas(1)).pack(pady=10)
    tk.Button(ventana, text="Lubricación", font=("Arial", 14), command=lambda: mostrar_sintomas(2)).pack(pady=10)
    tk.Button(ventana, text="Refrigeración", font=("Arial", 14), command=lambda: mostrar_sintomas(3)).pack(pady=10)
    
    
# Función para mostrar los síntomas
def mostrar_sintomas(tipo_falla_id):
    sintomas = obtener_datos("sintomas", tipo_falla_id)

    for widget in ventana.winfo_children():
        widget.destroy()

    tk.Label(ventana, text="¿Su vehículo presenta alguno de estos síntomas?", font=("Arial", 16)).pack(pady=10)
    tk.Label(ventana, text="\n".join(sintomas), font=("Arial", 12), wraplength=400, justify="left").pack(pady=10)
    
    tk.Button(ventana, text="Sí", font=("Arial", 14), command=lambda: mostrar_causas(tipo_falla_id)).pack(pady=10)
    tk.Button(ventana, text="No", font=("Arial", 14), command=mostrar_menu_principal).pack(pady=10)

# Función para mostrar las causas
def mostrar_causas(tipo_falla_id):
    causas = obtener_datos("causas", tipo_falla_id)

    for widget in ventana.winfo_children():
        widget.destroy()

    tk.Label(ventana, text="Posibles causas de la falla:", font=("Arial", 16)).pack(pady=10)
    tk.Label(ventana, text="\n".join(causas), font=("Arial", 12), wraplength=400, justify="left").pack(pady=10)

    tk.Button(ventana, text="Soluciones", font=("Arial", 14), command=lambda: mostrar_soluciones(tipo_falla_id)).pack(pady=10)
    tk.Button(ventana, text="Menú principal", font=("Arial", 14), command=mostrar_menu_principal).pack(pady=10)

# Función para mostrar las soluciones
def mostrar_soluciones(tipo_falla_id):
    soluciones = obtener_datos("soluciones", tipo_falla_id)

    for widget in ventana.winfo_children():
        widget.destroy()

    tk.Label(ventana, text="Soluciones recomendadas:", font=("Arial", 16)).pack(pady=10)
    tk.Label(ventana, text="\n".join(soluciones), font=("Arial", 12), wraplength=400, justify="left").pack(pady=10)

    tk.Button(ventana, text="Sugerencias", font=("Arial", 14), command=lambda: mostrar_sugerencias(tipo_falla_id)).pack(pady=10)
    tk.Button(ventana, text="Menú principal", font=("Arial", 14), command=mostrar_menu_principal).pack(pady=10)

# Función para mostrar las sugerencias
def mostrar_sugerencias(tipo_falla_id):
    sugerencias = obtener_datos("sugerencias", tipo_falla_id)

    for widget in ventana.winfo_children():
        widget.destroy()

    tk.Label(ventana, text="Sugerencias para prevenir esta falla:", font=("Arial", 16)).pack(pady=10)
    tk.Label(ventana, text="\n".join(sugerencias), font=("Arial", 12), wraplength=400, justify="left").pack(pady=10)

    tk.Button(ventana, text="Menú principal", font=("Arial", 14), command=mostrar_menu_principal).pack(pady=10)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("CarExpert")
ventana.geometry("500x600")

# Mostrar el menú principal al iniciar
mostrar_menu_principal()

# Ejecutar la aplicación
ventana.mainloop()
