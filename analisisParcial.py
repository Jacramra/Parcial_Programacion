import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random


# ________________________________________________
# ***Funciones Tarea: proyectos de construcción***
# ________________________________________________

class Panaderia:

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

   