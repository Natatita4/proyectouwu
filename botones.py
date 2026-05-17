import streamlit as st
import os
from validacion import mirar_plantilla

def boton_subida():
    subida = st.file_uploader("upload", type=["xlsx"])

    if subida:
        revisar = mirar_plantilla(subida)

        if revisar is not None:
            st.success("Archivo validado")

def boton_descarga():
    ruta_plantilla = "plantilla_ow.xlsx"
    if os.path.exists(ruta_plantilla):
        with open(ruta_plantilla, "rb") as f:
            data = f.read()
        st.download_button(
            label="Descargar plantilla",
            data=data,
            file_name="plantilla_ow.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )