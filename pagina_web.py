import streamlit as st
import random
import os
from PIL import Image

RUTA_BASE = "/workspaces/mi_primera_pagina/tiernos"
CARPETAS = {
    "mapache": os.path.join(RUTA_BASE, "/workspaces/mi_primera_pagina/tiernos/mapache"),
    "zorrito": os.path.join(RUTA_BASE, "/workspaces/mi_primera_pagina/tiernos/zorrito"),
    "pandita rojo": os.path.join(RUTA_BASE, "/workspaces/mi_primera_pagina/tiernos/pandita rojo")
}

CARPETA_CANCIONES = "/workspaces/mi_primera_pagina/Songs_so_cute"
canciones = {
    "Canción 1": os.path.join(CARPETA_CANCIONES, "/workspaces/mi_primera_pagina/Songs_so_cute/cancion_Miku.mp3"),
    "Canción 2": os.path.join(CARPETA_CANCIONES, "/workspaces/mi_primera_pagina/Songs_so_cute/caramel_dancing.mp3"),
    "Canción 3": os.path.join(CARPETA_CANCIONES, "/workspaces/mi_primera_pagina/Songs_so_cute/cancion_mas_tierna.mp3")
}

def obtener_imagen_aleatoria(ruta_carpeta):
    imagenes = os.listdir(ruta_carpeta)
    if imagenes:
        imagen_aleatoria = random.choice(imagenes)
        return Image.open(os.path.join(ruta_carpeta, imagen_aleatoria))
    return None

st.title("Para ti qué animal es más lindo?")

st.sidebar.title("Barra lateral")
musica = st.sidebar.selectbox("Selecciona una canción:", list(canciones.keys()))
comentario = st.sidebar.text_area("Escribe un comentario:")

st.sidebar.write(f"Reproduciendo: {musica}")
st.audio(canciones[musica])

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
