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

CANCIONES = {
    "Canción más tierna": "cancion_mas_tierna.mp3",
    "Canción Miku": "cancion_Miku.mp3",
    "Caramel Dancing": "caramel_dancing.mp3"
}

def obtener_imagen(ruta_carpeta):
    imagenes = os.listdir(ruta_carpeta)
    if imagenes:
        imagen = random.choice(imagenes)
        return Image.open(os.path.join(ruta_carpeta, imagen))
    return None

st.title("Para ti, qué animal es más lindo?")

with st.sidebar:
    st.header("Comparte tu opinión")
    respuesta = st.text_input("Cuál de estos animales te parece el más lindo y por qué? explayece")
    if st.button("Enviar"):
        if respuesta:
            st.sidebar.write("Gracias por tu opinion ☺️☺️☺️")
        else:
            st.sidebar.write("Por favor, pongase serio y envie una opinion real.....")

    st.header("elija una cancion (la mejor es la mas tierna pero no es tan tierna para se sincero)")
    cancion_seleccionada = st.selectbox("Elige una canción para escuchar:", list(CANCIONES.keys()))
    if cancion_seleccionada:
        st.audio(CANCIONES[cancion_seleccionada], format="audio/mp3")

if "mostrar_seleccion" not in st.session_state:
    st.session_state.mostrar_seleccion = True

if st.session_state.mostrar_seleccion:
    if st.button("Opción 1: Mapache 🦝"):
        st.session_state.mostrar_seleccion = False
        imagen = obtener_imagen(CARPETAS["mapache"])
        if imagen:
            st.image(imagen, caption="El mapache, animal que representa a los informaticos (por las ojeras)")
        else:
            st.write("No se encontraron imágenes en la carpeta 'mapache'.")

    elif st.button("Opción 2: Zorrito 🦊"):
        st.session_state.mostrar_seleccion = False
        imagen = obtener_imagen(CARPETAS["zorrito"])
        if imagen:
            st.image(imagen, caption="Zorrito, el zorro chilote tiene cara de que nada le importa")
        else:
            st.write("No se encontraron imágenes en la carpeta 'zorrito'.")

    elif st.button("Opción 3: Pandita Rojo 🐼🔴"):
        st.session_state.mostrar_seleccion = False
        imagen = obtener_imagen(CARPETAS["pandita rojo"])
        if imagen:
            st.image(imagen, caption="sabias que el maestro shifu era un panda rojo????")
        else:
            st.write("No se encontraron imágenes en la carpeta 'pandita rojo'.")

if not st.session_state.mostrar_seleccion:
    if st.button("volver"):
        st.session_state.mostrar_seleccion = True

