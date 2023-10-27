import fitz 
import spacy
import re



def extrair_texto_do_pdf(caminho_do_pdf):
    texto = ""
    documento_pdf = fitz.open(caminho_do_pdf)
    for pagina in documento_pdf:
        texto += pagina.get_text()
    documento_pdf.close()
    return texto

#problemas com dias sem 'feira' e '1º'
def encontrar_datas(texto):
    padrao = r"(\d{1,2}) de (\w+) \((\w+-feira)\),(.*?)(?=\;|$)"
    datas_encontradas = re.findall(padrao, texto, re.IGNORECASE | re.DOTALL)
    return datas_encontradas

caminho_do_pdf = "decreto.pdf"


texto_extraido = extrair_texto_do_pdf(caminho_do_pdf)


datas_encontradas = encontrar_datas(texto_extraido)


print("Datas encontradas:")
for data in datas_encontradas:
    print(data)
