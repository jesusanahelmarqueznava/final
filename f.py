import streamlit as st

def show_code(file_path):
    with open(file_path, "r") as file:
        code = file.read()
    st.code(code, language="python")

def main():
    st.title("Menú con Streamlit")

    options = ["Opción 1", "Opción 2", "Opción 3"]
    choice = st.sidebar.selectbox("Selecciona una opción", options)

    if choice == "Opción 1":
        st.write("Has seleccionado la opción 1")
        show_code("Patrones.ipynb")
    elif choice == "Opción 2":
        st.write("Has seleccionado la opción 2")
        show_code("Anomalias.ipynb")
    elif choice == "Opción 3":
        st.write("Has seleccionado la opción 3")
        show_code("Analisis_Estacionariedad.ipynb")

if __name__ == "__main__":
    main()


