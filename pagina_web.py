import streamlit as st
import random
import os
from PIL import Image

RUTA_BASE = "tiernos"
CARPETAS = {
    "mapache": os.path.join(RUTA_BASE, "mapache"),
    "zorrito": os.path.join(RUTA_BASE, "zorrito"),
    "pandita rojo": os.path.join(RUTA_BASE, "pandita rojo")
}

def obtener_imagen_aleatoria(ruta_carpeta):
    imagenes = os.listdir(ruta_carpeta)
    if imagenes:
        imagen_aleatoria = random.choice(imagenes)
        return Image.open(os.path.join(ruta_carpeta, imagen_aleatoria))
    return None

st.title("Para ti, que animal es mas lindo????")

if st.button("Opción 1: Mapache 🦝"):
    imagen = obtener_imagen_aleatoria(CARPETAS["mapache"])
    if imagen:
        st.image(imagen, caption="¡Aquí tienes un mapache!")
    else:
        st.write("No se encontraron imágenes en la carpeta 'mapache'.")

elif st.button("Opción 2: Zorrito"):
    imagen = obtener_imagen_aleatoria(CARPETAS["zorrito 🦊"])
    if imagen:
        st.image(imagen, caption="¡Aquí tienes un zorrito!")
    else:
        st.write("No se encontraron imágenes en la carpeta 'zorrito'.")

elif st.button("Opción 3: Pandita Rojo"):
    imagen = obtener_imagen_aleatoria(CARPETAS["pandita rojo 🐼🔴"])
    if imagen:
        st.image(imagen, caption="¡Aquí tienes un pandita rojo!")
    else:
        st.write("No se encontraron imágenes en la carpeta 'pandita rojo'.")
