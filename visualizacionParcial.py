import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

ventana = tk.Tk()
ventana.title("Control de la Producción en Panadería")

# 1. Registro de producción diaria
def registrar_produccion():
    nombreOperario = label_nombreOperario.get().strip()
    messagebox.showinfo("Registrado", f"{nombre} registrado con eficiencia {eficiencia} ({estado})")

# Menú
#tk.Button(root, text="Registrar producción", command=registrar_produccion).grid(row=4, column=0, columnspan=2, pady=5)
boton_registrar = tk.Button(ventana, text="Registrar producción", command=registrar_produccion)
boton_registrar.grid(row=4, column=0, columnspan=2, pady=5)

#Campo: Nombre operario
label_nombreOperario = tk.Label(ventana, text="Nombre del operario")
label_nombreOperario.grid(row=0, column=0)

label_nombreOperario = tk.Entry(ventana)
label_nombreOperario.grid(row=0, column=1)



ventana.mainloop()