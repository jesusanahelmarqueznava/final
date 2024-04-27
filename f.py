import streamlit as st

# Funciones para cada opción del menú
def option_one():
    st.write("Has seleccionado la opción 1")
    # Aquí puedes agregar el código que quieras ejecutar para la opción 1

def option_two():
    st.write("Has seleccionado la opción 2")
    # Aquí puedes agregar el código que quieras ejecutar para la opción 2

def option_three():
    st.write("Has seleccionado la opción 3")
    # Aquí puedes agregar el código que quieras ejecutar para la opción 3

# Función principal para crear y mostrar el menú
def main():
    st.title("Menú con Streamlit")

    # Configuración del estilo del menú
    st.markdown(
        """
        <style>
        .menu-title {
            color: #ff6347;
            text-align: center;
            font-size: 36px;
            margin-bottom: 30px;
        }
        .menu-options {
            text-align: center;
        }
        .option-button {
            background-color: #ff6347;
            color: white;
            font-size: 24px;
            padding: 10px 20px;
            margin: 10px;
            border-radius: 10px;
            cursor: pointer;
        }
        .option-button:hover {
            background-color: #d84315;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Título del menú
    st.markdown("<h1 class='menu-title'>Menú de Opciones</h1>", unsafe_allow_html=True)

    # Selección de opción
    options = ["Opción 1", "Opción 2", "Opción 3"]
    selected_option = st.selectbox("Selecciona una opción", options, index=0, format_func=lambda x: x)

    # Botones de opciones
    st.markdown("<div class='menu-options'>", unsafe_allow_html=True)
    if st.button("Opción 1", key="opcion_1"):
        option_one()
    if st.button("Opción 2", key="opcion_2"):
        option_two()
    if st.button("Opción 3", key="opcion_3"):
        option_three()
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

