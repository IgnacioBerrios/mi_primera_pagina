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

# Ubicación de las canciones
CARPETA_CANCIONES = "Song_so_cute"
canciones/ = {
    "Canción 1": os.path.join(CARPETA_CANCIONES, "cancion_Miku.mp3"),
    "Canción 2": os.path.join(CARPETA_CANCIONES, "caramel_dancing.mp3"),
    "Canción 3": os.path.join(CARPETA_CANCIONES, "cancion_mas_tierna.mp3")
}

def obtener_imagen_aleatoria(ruta_carpeta):
    imagenes = os.listdir(ruta_carpeta)
    if imagenes:
        imagen_aleatoria = random.choice(imagenes)
        return Image.open(os.path.join(ruta_carpeta, imagen_aleatoria))
    return None

st.title("Para ti qué animal es más lindo?")

st.sidebar.title("Barra lateral")
musica = st.sidebar.selectbox("Selecciona una canción:", list(CANCIONES.keys()))
comentario = st.sidebar.text_area("Escribe un comentario:")

st.sidebar.write(f"Reproduciendo: {musica}")
st.audio(CANCIONES[musica])

st.sidebar.write("Tu comentario:")
st.sidebar.write(comentario)

if "opcion_seleccionada" not in st.session_state:
    st.session_state.opcion_seleccionada = None

def reset_opcion():
    st.session_state.opcion_seleccionada = None

if st.session_state.opcion_seleccionada is None:
    if st.button("Opción 1: Mapache 🦝"):
        st.session_state.opcion_seleccionada = "mapache"
    elif st.button("Opción 2: Zorrito 🦊"):
        st.session_state.opcion_seleccionada = "zorrito"
    elif st.button("Opción 3: Pandita Rojo 🐼🔴"):
        st.session_state.opcion_seleccionada = "pandita rojo"

if st.session_state.opcion_seleccionada:
    imagen = obtener_imagen_aleatoria(CARPETAS[st.session_state.opcion_seleccionada])
    if imagen:
        st.image(imagen, caption=f"¡Aquí tienes un {st.session_state.opcion_seleccionada}!")
    else:
        st.write(f"No se encontraron imágenes en la carpeta '{st.session_state.opcion_seleccionada}'.")

    if st.button("Volver"):
        reset_opcion()

