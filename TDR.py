# Para correr: streamlit run hola.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def main_page():
    st.title("Subida de imagen")
    uploaded_image = st.file_uploader("Elige una imagen", type=['jpg', 'png'])
    if uploaded_image is not None:
        st.image(uploaded_image, caption='Imagen cargada')
        if 'next_page' not in st.session_state:
            st.session_state.next_page = False
        if st.button("Ir al siguiente paso"):
            st.session_state.next_page = True

def second_page():
    st.title("Segundo paso")
    st.write("Aquí continuamos con el segundo paso del proceso.")

# Control de flujo de la página
if 'next_page' in st.session_state and st.session_state.next_page:
    second_page()
else:
    main_page()


st.title('TDR: Mercado Libre')

st.write('Paso 1: Subir Archivo "Scroll Order" (Dispatch)')

uploaded_file_dispatch = st.file_uploader('Selecciona un Archivo', type=['csv', 'xlsx'])

if uploaded_file_dispatch is not None:
    try:
        if uploaded_file_dispatch.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file_dispatch)
        elif uploaded_file_dispatch.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file_dispatch)
        st.write(df)
    except Exception as e:
        st.error(f"Error al leer el archivo: {e}")

st.write('Paso 2: Subir Archivo "Asignaciones de Tag por Unidad"')
st.write('¡NOTA! El archivo a subir debe ser un archivo Excel (.xlsx), y debe contener solamente una hoja, con dos columnas. Ejemplo: ')

#image_path = '/Users/sebastianrodriguez/Desktop/TDR-APP/Screen Shot 2024-05-28 at 15.56.46.png'  # Cambia esto por la ruta a tu imagen
#st.image(image_path, caption='Archivo Excel con dos columnas, "Tag" y "Unidad"')

# Ruta a la imagen
image_path = '/Users/sebastianrodriguez/Desktop/TDR-APP/Screen Shot 2024-05-28 at 15.56.46.png'  # Cambia esto por la ruta a tu imagen
img = Image.open(image_path)
img = img.resize((300, 200), Image.ANTIALIAS)
st.image(img, caption='Archivo Excel con dos columnas, "Tag" y "Unidad"')


# TELEVIA 
#uploaded_file_televia = st.file_uploader('Paso 2: Subir Archivo "TeleVia"', type=['csv', 'xlsx'])

#if uploaded_file_televia is not None:
    # Puedes hacer algo con el archivo aquí
    #st.write("¡Archivo cargado con éxito!")



