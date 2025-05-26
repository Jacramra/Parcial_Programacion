import pandas as pd
import matplotlib.pyplot as plt
import random
from tkinter import messagebox

# Lista para almacenar los datos de producción
produccion = []  # Aquí se guardan los datos registrados
datos_operarios = {}  # Diccionario con detalles de cada operario
#_________________________________________________________________________________________
# _______________________________________FUNCIONES________________________________________
#_________________________________________________________________________________________

# 1. Registro de producción diaria
def registrar_produccion(nombre, pf, pq, cr):
      
    if not nombre.strip():
        raise ValueError("Por favor, ingrese el nombre del operario.")
   
    try:
        pf = int(pf)
        pq = int(pq)
        cr = int(cr)
        if any(n < 0 or n > 500 for n in (pf, pq, cr)):
            raise ValueError("Cada cantidad debe estar entre 0 y 500.")
    except ValueError:
        raise ValueError("Debe ingresar cantidades válidas entre 0 y 500.")

    # Genera complejidades aleatorias para cada producto
    complejidades = {
        "Pan Francés": round(random.uniform(1.0, 1.5), 2),
        "Pan de Queso": round(random.uniform(1.0, 1.5), 2),
        "Croissants": round(random.uniform(1.0, 1.5), 2),
    }

    # Calcula eficiencia ponderada
    total = pf * complejidades["Pan Francés"] + pq * complejidades["Pan de Queso"] + cr * complejidades["Croissants"]
    suma_complejidad = sum(complejidades.values())
    eficiencia = round(total / suma_complejidad)
    estado = "Cumple" if eficiencia >= 300 else "No cumple"

    # Crear registro para guardar
    registro = {
        "Operario": nombre,
        "Pan Francés": pf,
        "Pan de Queso": pq,
        "Croissants": cr,
        "Eficiencia": eficiencia,
        "Estado": estado
    }

    # Guardar el registro en las listas
    produccion.append(registro) 

    # También se guarda individualmente
    datos_operarios[nombre] = {
        "cantidades": {
            "Pan Francés": pf,
            "Pan de Queso": pq,
            "Croissants": cr
        },
        "complejidades": complejidades,
        "eficiencia": eficiencia,
        "estado": estado
    }

    return registro

def obtener_reporte_general():
    if not produccion:
        raise ValueError("No hay registros disponibles.")

    df = pd.DataFrame(produccion)
    estadisticas = df.describe()
    promedio = df["Eficiencia"].mean()

    # Gráfico de torta
    conteo_estados = df["Estado"].value_counts()
    conteo_estados.plot.pie(autopct='%1.1f%%', startangle=90)
    plt.title("Cumplimiento de Meta")
    plt.ylabel("")
    plt.show()

    # Matriz de correlación
    correlacion = df[["Pan Francés", "Pan de Queso", "Croissants"]].corr()
    plt.matshow(correlacion, cmap='coolwarm')
    plt.colorbar()
    plt.xticks(range(len(correlacion.columns)), correlacion.columns, rotation=45)
    plt.yticks(range(len(correlacion.columns)), correlacion.columns)
    plt.title("Correlación entre tipos de pan", y=1.2)
    plt.show()

    return df[["Operario", "Eficiencia", "Estado"]], estadisticas, promedio
    
def obtener_reporte_individual(nombre):
    if nombre not in datos_operarios:
        raise ValueError("Operario no encontrado.")

    datos = datos_operarios[nombre]
    cantidades = datos["cantidades"]
    complejidades = datos["complejidades"]
    eficiencia = datos["eficiencia"]
    estado = datos["estado"]

    # Histogramas
    # 1. Producción
    plt.bar(cantidades.keys(), cantidades.values(), color='skyblue')
    plt.title("Producción por tipo de pan")
    plt.ylabel("Cantidad")
    plt.show()