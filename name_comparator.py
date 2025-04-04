def compare_names(pdf_text, csv_names):
    # Divide o texto do PDF em palavras e as normaliza
    pdf_words = pdf_text.lower()
    # Normaliza os nomes do CSV e verifica correspondências
    matched_names = [name for name in csv_names if name.lower() in pdf_words]
    
    return matched_names