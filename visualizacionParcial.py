import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Control de la Producción en Panadería")

#_________________________________________________________________________________________
# _______________________________________CAMPOS___________________________________________
#_________________________________________________________________________________________

def mostrar_campos(): # Crear el label y entry solo cuando se pulse el botón
    
    # Campo Nombre Operario
    label_nombre = tk.Label(ventana, text="Nombre del operario")
    label_nombre.grid(row=1, column=0)                  # Mostrar etiqueta 
    entry_nombreOperario = tk.Entry(ventana)
    entry_nombreOperario.grid(row=1, column=1)          # Mostrar campo de texto

    # Campo Cant. Pan Francés
    label_panFrances = tk.Label(ventana, text="Cant. pan francés")
    label_panFrances.grid(row=2, column=0)              # Mostrar etiqueta 
    entry_pf = tk.Entry(ventana)
    entry_pf.grid(row=2, column=1)                      # Mostrar campo de texto

    # Campo Cant. Pan Queso
    label_panQueso = tk.Label(ventana, text="Cant. pan de queso")
    label_panQueso.grid(row=3, column=0)                # Mostrar etiqueta 
    entry_pq = tk.Entry(ventana)
    entry_pq.grid(row=3, column=1)                      # Mostrar campo de texto



    boton_confirmar.grid(row=5, column=0, columnspan=2) # Mostrar botón "Confirmar registro"



# 1. Registro de producción diaria
def registrar_produccion():
    nombre = entry_nombreOperario.get().strip()         # Obtiene el texto ingresado y quitar espacios extra

    if not nombre:
        messagebox.showwarning("Falta nombre", "Por favor, ingrese el nombre del operario.")
        return
    messagebox.showinfo("Registrado", f"Nombre: {nombre}.")
    #messagebox.showinfo("Registrado", f"{nombre} registrado con eficiencia {eficiencia} ({estado})")

    # Oculta los widgets relacionados para limpiar la interfaz
    label_nombre.grid_remove()              # Oculta la etiqueta
    entry_nombreOperario.grid_remove()      # Oculta el campo de texto
    boton_confirmar.grid_remove()           # Oculta el botón confirmar
    entry_nombreOperario.delete(0, tk.END)  # Limpia el campo

# 4. Cierra la ventana
# Referencia: 
# GeeksforGeeks. (2022). Destroy method in Tkinter Python. Disponible en: https://www.geeksforgeeks.org/destroy-method-in-tkinter-python/
def cerrar_ventana():
    ventana.destroy()

#_________________________________________________________________________________________
# _______________________________________MENÚ_____________________________________________
#_________________________________________________________________________________________

# Botón inicial para mostrar el campo de nombre
boton_registrar = tk.Button(ventana, text="Registrar producción", command=mostrar_campos)
boton_registrar.grid(row=4, column=0)

# Botón para confirmar el registro (inicialmente oculto)
boton_confirmar = tk.Button(ventana, text="Confirmar registro", command=registrar_produccion)

boton_reporteGeneral = tk.Button(ventana, text="Reporte General", command=registrar_produccion)
boton_reporteGeneral.grid(row=5, column=0)

boton_reporteIndividual = tk.Button(ventana, text="Reporte Individual", command=registrar_produccion)
boton_reporteIndividual.grid(row=6, column=0)

boton_Salir = tk.Button(ventana, text="Salir", command=cerrar_ventana) 
boton_Salir.grid(row=7, column=0)




ventana.mainloop()