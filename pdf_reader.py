def read_pdf(file_path):
    from PyPDF2 import PdfReader

    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text.replace("  ", " ")

# retorno = read_pdf("/home/aletavares/projetos/alunos/Gabriele/compare-names-app/src/testes/Preliminar OAB 42.pdf")

# with open("output.txt", "w") as f:
#      f.write(retorno)
# def read_pdf(file_path):
#     import pdfplumber
    
#     text = ""
# with pdfplumber.open(file_path) as pdf:
#     for page in pdf.pages:
#         text += page.extract_text() + "\n"
#     return text.strip()