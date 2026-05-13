import streamlit as st
import pandas as pd

def mirar_plantilla(archivo_usuario):
    columnas = ["Heal", "Kills", "Asistencias"]
    df = pd.read_excel(archivo_usuario)

    columnas_subido = set(df.columns)
    columnas_faltantes = [ col for col in columnas if col not in columnas_subido ]

    if columnas_faltantes:
        st.error("Las columnas esperadas no se encuentran en el archivo. Reintente nuevamente sin modificar la plantilla")
        return None
    
    df = df.dropna(how='all')

    return df


    