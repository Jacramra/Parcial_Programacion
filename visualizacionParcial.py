import tkinter as tk
from tkinter import messagebox
from analisisParcial import registrar_produccion
from analisisParcial import obtener_reporte_general, obtener_reporte_individual


# Crear ventana principal
ventana = tk.Tk()
ventana.title("Control de la Producción en Panadería")

# Tabla de resultados global para poder insertar luego
tabla = tk.Text(ventana, width=70, height=10)
tabla.grid(row=7, column=0, columnspan=2)

#_________________________________________________________________________________________
# _______________________________________CAMPOS___________________________________________
#_________________________________________________________________________________________

# Mostrar campos para ingresar datos
def mostrar_campos():
    global entry_nombre, entry_pf, entry_pq, entry_cr
    global label_nombreOperario, boton_confirmar

    # Campo: Nombre Operario
    label_nombreOperario = tk.Label(ventana, text="Nombre del operario")
    label_nombreOperario.grid(row=1, column=0)                  # Mostrar etiqueta 
    entry_nombre = tk.Entry(ventana)
    entry_nombre.grid(row=1, column=1)          # Mostrar campo de texto

    # Campo: Cant. Pan Francés
    label_panFrances = tk.Label(ventana, text="Cant. pan francés")
    label_panFrances.grid(row=2, column=0)              # Mostrar etiqueta 
    entry_pf = tk.Entry(ventana)
    entry_pf.grid(row=2, column=1)                      # Mostrar campo de texto

    # Campo: Cant. Pan Queso
    label_panQueso = tk.Label(ventana, text="Cant. pan de queso")
    label_panQueso.grid(row=3, column=0)                # Mostrar etiqueta 
    entry_pq = tk.Entry(ventana)
    entry_pq.grid(row=3, column=1)                      # Mostrar campo de texto

    # Campo: Cant. Pan Croissants
    label_panCroissants = tk.Label(ventana, text="Cant. pan de croissants")
    label_panCroissants.grid(row=4, column=0)           # Mostrar etiqueta 
    entry_cr = tk.Entry(ventana)
    entry_cr.grid(row=4, column=1)                      # Mostrar campo de texto

    # Mostrar el botón Confirmar cuando se llame a esta función
    boton_confirmar.grid()  # Esto lo muestra nuevamente en la ventana


# Confirmar y registrar datos ingresados
def confirmar():
    global entry_nombre, entry_pf, entry_pq, entry_cr
    global label_nombreOperario, label_panFrances, label_panQueso, label_panCroissants

    # Ocultar los campos y etiquetas solicitados
    #label_nombreOperario.grid_remove()
    #entry_nombre.grid_remove()
    #label_panFrances.grid_remove()
    #entry_pf.grid_remove()
    #label_panQueso.grid_remove()
    #entry_pq.grid_remove()

    nombre = entry_nombre.get()
    pf = entry_pf.get()
    pq = entry_pq.get()
    cr = entry_cr.get()

    try:
        registro = registrar_produccion(nombre, pf, pq, cr)
        if registro is None:
            raise ValueError("El registro está vacío.")
        mensaje = f"{registro['Operario']} - {registro['Eficiencia']}% ({registro['Estado']})"
        messagebox.showinfo("Registrado", mensaje)
        mostrar_en_tabla(registro)
        limpiar_campos()
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Mostrar los resultados en la tabla de texto
def mostrar_en_tabla(registro):
    tabla.insert(tk.END, f"{registro['Operario']} | PF: {registro['Pan Francés']} | PQ: {registro['Pan de Queso']} | CR: {registro['Croissants']} | Eficiencia: {registro['Eficiencia']}% | Estado: {registro['Estado']}\n")

# Limpiar entradas
def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_pf.delete(0, tk.END)
    entry_pq.delete(0, tk.END)
    entry_cr.delete(0, tk.END)

 # Cerrar la ventana
# Referencia: 
 # GeeksforGeeks. (2022). Destroy method in Tkinter Python. Disponible en: https://www.geeksforgeeks.org/destroy-method-in-tkinter-python/
def cerrar_ventana():
    ventana.destroy()


#_________________________________________________________________________________________
# _______________________________________MENÚ_____________________________________________
#_________________________________________________________________________________________

# Botón para registrar producción
boton_registrar = tk.Button(ventana, text="Registrar producción", command=mostrar_campos)
boton_registrar.grid(row=0, column=0)

# Botón para confirmar el registro
boton_confirmar = tk.Button(ventana, text="Confirmar registro", command=confirmar)
boton_confirmar.grid(row=0, column=1, columnspan=2)
boton_confirmar.grid_remove()  # Oculta el botón inicialmente

# Botón para Reporte General
boton_reporteGeneral = tk.Button(ventana, text="Reporte General", command=mostrar_campos)
boton_reporteGeneral.grid(row=5, column=0)

# Botón para Reporte Individual
boton_reporteIndividual = tk.Button(ventana, text="Reporte Individual", command=mostrar_campos)
boton_reporteIndividual.grid(row=6, column=0)

# Botón para salir
boton_Salir = tk.Button(ventana, text="Salir", command=cerrar_ventana) 
boton_Salir.grid(row=8, column=0)

ventana.mainloop()