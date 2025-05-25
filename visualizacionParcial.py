import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Control de la Producción en Panadería")

# 1. Registro de producción diaria
def registrar_produccion():
    nombre = entry_nombreOperario.get().strip()

    if not nombre:
        messagebox.showwarning("Falta nombre", "Por favor, ingrese el nombre del operario.")
        return
    messagebox.showinfo("Registrado", f"Nombre: {nombre}.")
    #messagebox.showinfo("Registrado", f"{nombre} registrado con eficiencia {eficiencia} ({estado})")

# 4. Cierra la ventana
# Referencia: 
# GeeksforGeeks. (2022). Destroy method in Tkinter Python. Disponible en: https://www.geeksforgeeks.org/destroy-method-in-tkinter-python/
def cerrar_ventana():
    ventana.destroy()


# Menú
# Botón de registro
boton_registrar = tk.Button(ventana, text="Registrar producción", command=registrar_produccion)
boton_registrar.grid(row=4, column=0)

boton_reporteGeneral = tk.Button(ventana, text="Reporte General", command=registrar_produccion)
boton_reporteGeneral.grid(row=5, column=0)

boton_reporteIndividual = tk.Button(ventana, text="Reporte Individual", command=registrar_produccion)
boton_reporteIndividual.grid(row=6, column=0)

boton_Salir = tk.Button(ventana, text="Salir", command=cerrar_ventana) 
boton_Salir.grid(row=7, column=0)

#Campo: Nombre operario
label_nombre = tk.Label(ventana, text="Nombre del operario")
label_nombre.grid(row=0, column=0)

entry_nombreOperario = tk.Entry(ventana)
entry_nombreOperario.grid(row=0, column=1)



ventana.mainloop()