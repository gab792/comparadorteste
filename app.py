from pdf_reader import read_pdf
from csv_reader import read_csv
from name_comparator import compare_names
import streamlit as st

def main():
    st.title("Comparador de Nomes entre PDF e CSV")

    pdf_file = st.file_uploader("Faça upload do arquivo PDF", type=["pdf"])
    csv_file = st.file_uploader("Faça upload do arquivo CSV", type=["csv"])

    if pdf_file and csv_file:
        pdf_text = read_pdf(pdf_file)
        csv_names = read_csv(csv_file)

        matches = compare_names(pdf_text, csv_names)

        if matches:
            st.success("Nomes encontrados em ambos os arquivos:")
            st.write(matches)
        else:
            st.warning("Nenhum nome correspondente encontrado.")

if __name__ == "__main__":
    main()