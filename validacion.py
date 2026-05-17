import streamlit as st
import pandas as pd

def mirar_plantilla(archivo_usuario):
    columnas = ["Tiempo Jugado con Heroe", "Partidas Jugadas", "Partidas Ganadas", "Partidas Perdidas", "Eliminaciones", "Eliminaciones por vida", "Muertes", "Daño Infligido a Heroes", "Daño Infligido a Heroes por Vida", "Sanacion realizada", "Muertes en objetivo", "Precision de Golpes Criticos", "Golpes Criticos", "Golpes Criticos por Vida", "Precision con armas", "Mejor Presicion en una partida", "Daño Amplificado", "Mejor Racha de Muertes", "Asistencias", "Golpes de Gracia", "Tiempo en objetivo"]
    df = pd.read_excel(archivo_usuario)

    columnas_subido = set(df.columns)
    columnas_faltantes = [ col for col in columnas if col not in columnas_subido ]

    if columnas_faltantes:
        st.error("Las columnas esperadas no se encuentran en el archivo. Reintente nuevamente sin modificar la plantilla")
        return None
    
    df = df.dropna(how='all')

    return df


    