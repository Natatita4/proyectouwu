import streamlit as st
import base64
import os

@st.cache_data
def obtener_fuente(ruta_fuente):
    if os.path.exists(ruta_fuente):
        with open(ruta_fuente, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

def aplicar_fuente():
    # Nombre de tu archivo (asegúrate que esté en la misma carpeta o ajusta la ruta)
    font_path = "BankSans CapsEF EL Bol.ttf"
    font_base64 = obtener_fuente(font_path)
    if font_base64:
        st.markdown(
            f'''
            <style>
            @font-face {{
                font-family: 'BankSans';
                src: url(data:font/ttf;base64,{font_base64}) format('truetype');
                font-weight: normal;
                font-style: normal;
            }}

            html, body, [class*="st-"], .stMarkdown, p, h1, h2, h3, span, button {{
                font-family: 'BankSans', sans-serif !important;
            }}

            .stApp {{
                background-color: #ffffff;
            }}

            .stButton > button {{
                background-color: #38a9c7;
                color: white;
                border-radius: 10px;
                height: 50px;
                width: 200px;
                font-size: 18px;
                font-family: 'BankSans', sans-serif !important;
            }}

            .stButton > button:hover {{
                background-color: #3882c7;
                color: #7e9fbd;
            }}
            </style>
            ''',
            unsafe_allow_html=True
        )
    else:
        st.error("Error: No se pudo cargar la fuente personalizada.")