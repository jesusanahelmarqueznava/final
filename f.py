import streamlit as st
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert import HTMLExporter

def execute_notebook(notebook):
    execute_preprocessor = ExecutePreprocessor(timeout=-1, kernel_name='python3')
    execute_preprocessor.preprocess(notebook, {'metadata': {'path': './'}})

def option_one():
    st.write("Has seleccionado la opción 1")
    notebook_path = "Patrones.ipynb"
    notebook = nbformat.read(notebook_path, as_version=4)
    execute_notebook(notebook)
    html_exporter = HTMLExporter()
    (body, _) = html_exporter.from_notebook_node(notebook)
    st.write(body, unsafe_allow_html=True)

def option_two():
    st.write("Has seleccionado la opción 2")
    notebook_path = "Anomalias.ipynb"
    notebook = nbformat.read(notebook_path, as_version=4)
    execute_notebook(notebook)
    html_exporter = HTMLExporter()
    (body, _) = html_exporter.from_notebook_node(notebook)
    st.write(body, unsafe_allow_html=True)

def option_three():
    st.write("Has seleccionado la opción 3")
    notebook_path = "Analisis_Estaionariedad.ipynb"
    notebook = nbformat.read(notebook_path, as_version=4)
    execute_notebook(notebook)
    html_exporter = HTMLExporter()
    (body, _) = html_exporter.from_notebook_node(notebook)
    st.write(body, unsafe_allow_html=True)

def main():
    st.title("Menú con Ejecución de Notebook en Streamlit")

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



