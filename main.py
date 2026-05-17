import streamlit as st
from fuente import aplicar_fuente
from botones import boton_subida
from botones import boton_descarga

st.set_page_config(
    page_title="OwnStats",
    layout="centered"
)

aplicar_fuente()

st.markdown(
    "<h1 style='text-align: center; color: 	#000000; '>Ownstats</h1>",
    unsafe_allow_html=True
)

boton_descarga()
boton_subida()
