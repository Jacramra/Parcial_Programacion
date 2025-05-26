import pandas as pd
import matplotlib.pyplot as plt
import random
import tkinter as tk
from tkinter import messagebox


# ________________________________________________
# ***Funciones Tarea: proyectos de construcción***
# ________________________________________________

# 1. Registro de producción diaria
def registrar_produccion(nombre, pf, pq, cr):
    #nombre = entry_nombreOperario.get().strip()         # Obtiene el texto ingresado y quitar espacios extra
        
    if not nombre.strip():
        raise ValueError("Por favor, ingrese el nombre del operario.")
        #return
        #messagebox.showinfo("Registrado", f"Nombre: {nombre}.")
        #messagebox.showinfo("Registrado", f"{nombre} registrado con eficiencia {eficiencia} ({estado})")
    
    #label_nombre.grid_remove()              # Oculta la etiqueta
    #entry_nombreOperario.grid_remove()      # Oculta el campo de texto
    #boton_confirmar.grid_remove()           # Oculta el botón confirmar
    #entry_nombreOperario.delete(0, tk.END)  # Limpia el campo

    try:
        pf = int(pf)
        pq = int(pq)
        cr = int(cr)
        if any(n < 0 or n > 500 for n in (pf, pq, cr)):
            raise ValueError("Cada cantidad debe estar entre 0 y 500.")
    except ValueError:
        raise ValueError("Debe ingresar cantidades válidas entre 0 y 500.")

    eficiencia = random.randint(70, 100)
    estado = "Óptimo" if eficiencia >= 90 else "Regular" if eficiencia >= 80 else "Bajo"

    registro = {
        "Operario": nombre,
        "Pan Francés": pf,
        "Pan de Queso": pq,
        "Croissants": cr,
        "Eficiencia": eficiencia,
        "Estado": estado
    }

    produccion.append(registro)
    return registro


