import streamlit as st

def option_one():
    st.write("Has seleccionado la opción 1")
    # Aquí puedes agregar el código que quieras ejecutar para la opción 1

def option_two():
    st.write("Has seleccionado la opción 2")
    # Aquí puedes agregar el código que quieras ejecutar para la opción 2

def option_three():
    st.write("Has seleccionado la opción 3")
    # Aquí puedes agregar el código que quieras ejecutar para la opción 3

def main():
    st.title("Menú con Streamlit")

    options = ["Opción 1", "Opción 2", "Opción 3"]
    choice = st.sidebar.selectbox("Selecciona una opción", options)

    if choice == "Opción 1":
        option_one()
    elif choice == "Opción 2":
        option_two()
    elif choice == "Opción 3":
        option_three()

if __name__ == "__main__":
    main()
