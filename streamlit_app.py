import streamlit as st
from fuente import aplicar_fuente
from validacion import mirar_plantilla

# 2. Configuración de página
st.set_page_config(
    page_title="OwnStats",
    layout="centered"
)

aplicar_fuente()

st.markdown(
    "<h1 style='text-align: center; color: 	#000000; '>Ownstats</h1>",
    unsafe_allow_html=True
)

if st.button("descarga la plantilla"):
    st.markdown(
    "<h3 style='text-align: center; color: 	#000000; '>la descarga ha comenzado</h1>",
    unsafe_allow_html=True
)
    
subida = st.file_uploader("upload", type=["xlsx"])

if subida:
    revisar = mirar_plantilla(subida)

    if revisar is not None:
        st.success("Archivo validado")