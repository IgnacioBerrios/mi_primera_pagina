import streamlit as st
import random
import os
from PIL import Image

# Rutas
RUTA_BASE = "tiernos"
CARPETAS = {
    "mapache": os.path.join(RUTA_BASE, "mapache"),
    "zorrito": os.path.join(RUTA_BASE, "zorrito"),
    "pandita rojo": os.path.join(RUTA_BASE, "pandita rojo")
}

# Función para obtener imagen aleatoria
def obtener_imagen_aleatoria(ruta_carpeta):
    imagenes = os.listdir(ruta_carpeta)
    if imagenes:
        imagen_aleatoria = random.choice(imagenes)
        return Image.open(os.path.join(ruta_carpeta, imagen_aleatoria))
    return None

# Título
st.title("¿Para ti, qué animal es más lindo?")

# Barra lateral para escribir y enviar una respuesta
with st.sidebar:
    st.header("Comparte tu opinión")
    respuesta = st.text_input("¿Cuál de estos animales te parece el más lindo y por qué?")
    if st.button("Enviar respuesta"):
        if respuesta:
            st.sidebar.write("Gracias por tu respuesta!")
        else:
            st.sidebar.write("Por favor, escribe una respuesta.")

# Variable de estado para mostrar la pantalla inicial
if "mostrar_seleccion" not in st.session_state:
    st.session_state.mostrar_seleccion = True

# Pantalla de selección inicial
if st.session_state.mostrar_seleccion:
    if st.button("Opción 1: Mapache 🦝"):
        st.session_state.mostrar_seleccion = False
        imagen = obtener_imagen_aleatoria(CARPETAS["mapache"])
        if imagen:
            st.image(imagen, caption="¡Aquí tienes un mapache!")
        else:
            st.write("No se encontraron imágenes en la carpeta 'mapache'.")

    elif st.button("Opción 2: Zorrito 🦊"):
        st.session_state.mostrar_seleccion = False
        imagen = obtener_imagen_aleatoria(CARPETAS["zorrito"])
        if imagen:
            st.image(imagen, caption="¡Aquí tienes un zorrito!")
        else:
            st.write("No se encontraron imágenes en la carpeta 'zorrito'.")

    elif st.button("Opción 3: Pandita Rojo 🐼🔴"):
        st.session_state.mostrar_seleccion = False
        imagen = obtener_imagen_aleatoria(CARPETAS["pandita rojo"])
        if imagen:
            st.image(imagen, caption="¡Aquí tienes un pandita rojo!")
        else:
            st.write("No se encontraron imágenes en la carpeta 'pandita rojo'.")

# Botón para regresar a la selección inicial
if not st.session_state.mostrar_seleccion:
    if st.button("Regresar a la selección inicial"):
        st.session_state.mostrar_seleccion = True
