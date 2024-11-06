import streamlit as st
import random
import os
from PIL import Image

# Rutas base para imágenes y canciones
RUTA_BASE = "tiernos"
CARPETAS = {
    "mapache": os.path.join(RUTA_BASE, "mapache"),
    "zorrito": os.path.join(RUTA_BASE, "zorrito"),
    "pandita rojo": os.path.join(RUTA_BASE, "pandita rojo")
}

# Ubicación de las canciones
CARPETA_CANCIONES = "Songs_so_cute"
canciones = {
    "Canción 1": os.path.join(CARPETA_CANCIONES, "cancion_Miku.mp3"),
    "Canción 2": os.path.join(CARPETA_CANCIONES, "caramel_dancing.mp3"),
    "Canción 3": os.path.join(CARPETA_CANCIONES, "cancion_mas_tierna.mp3")
}

# Función para obtener una imagen aleatoria de una carpeta
def obtener_imagen_aleatoria(ruta_carpeta):
    imagenes = [f for f in os.listdir(ruta_carpeta) if f.endswith(('jpg', 'jpeg', 'png', 'gif'))]
    if imagenes:
        imagen_aleatoria = random.choice(imagenes)
        return Image.open(os.path.join(ruta_carpeta, imagen_aleatoria))
    return None

# Título principal
st.title("Para ti qué animal es más lindo?")

# Barra lateral con selección de música
st.sidebar.title("Barra lateral")
musica = st.sidebar.selectbox("Selecciona una canción:", list(canciones.keys()))
comentario = st.sidebar.text_area("Escribe un comentario:")

# Verifica si el archivo de audio existe antes de intentar reproducirlo
if not os.path.exists(canciones[musica]):
    st.error(f"El archivo de audio '{musica}' no se encontró en la ruta especificada.")
else:
    st.sidebar.write(f"Reproduciendo: {musica}")
    st.audio(canciones[musica])

# Mostrar comentario del usuario
st.sidebar.write("Tu comentario:")
st.sidebar.write(comentario)

# Manejo de la opción seleccionada
if "opcion_seleccionada" not in st.session_state:
    st.session_state.opcion_seleccionada = None

def reset_opcion():
    st.session_state.opcion_seleccionada = None

# Botones para seleccionar el animal
if st.session_state.opcion_seleccionada is None:
    if st.button("Opción 1: Mapache 🦝"):
        st.session_state.opcion_seleccionada = "mapache"
    elif st.button("Opción 2: Zorrito 🦊"):
        st.session_state.opcion_seleccionada = "zorrito"
    elif st.button("Opción 3: Pandita Rojo 🐼🔴"):
        st.session_state.opcion_seleccionada = "pandita rojo"

# Mostrar la imagen del animal seleccionado
if st.session_state.opcion_seleccionada:
    imagen = obtener_imagen_aleatoria(CARPETAS[st.session_state.opcion_seleccionada])
    if imagen:
        st.image(imagen, caption=f"¡Aquí tienes un {st.session_state.opcion_seleccionada}!")
    else:
        st.write(f"No se encontraron imágenes en la carpeta '{st.session_state.opcion_seleccionada}'.")

    # Botón para volver a elegir un animal
    if st.button("Volver"):
        reset_opcion()


