import streamlit as st

#inicializacion d eusuarios
usuarios =[]

#funcion para agregar un usuario
def agregar_usuario(nombre):
    usuarios.append(nombre)
    st.success(f"Usuario {nombre} agregado.")

    #funcion para mostrar usuarios
    def mostrar_usuarios():
        if usuarios:
            st.write("Lista de usuarios")
            for usuario in usuario:
                st.white(f"- {usuario}")
        else:
            st.warning("No hay usuarios registrados.")

#Menu principal
st.tittle("Gestión de usuarios")

opcion=st.selectbox("Selecciona una opción", ["Agregar usuario", "Mostrar usuario"])

if opcion== "Agregar usuario":
    nombre=st.text_input("Nombre del usuario")
    if st.button("Agregar"):
        if nombre:
            agregar_usuario(nombre)
        else
        st.error("El nombre no puede estar vacío")
elif opcion=="Mostrar usuarios"
mostrar_usuarios()
