import requests
import PyPDF2
from io import BytesIO

def download_pdf(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BytesIO(response.content)
    else:
        raise Exception("Erro ao baixar o PDF")

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

if __name__ == "__main__":
    pdf_url = "https://softstar.s3.amazonaws.com/documents/Politica_de_Privacidade.pdf"
    pdf_file = download_pdf(pdf_url)
    pdf_text = extract_text_from_pdf(pdf_file)
    print(pdf_text)
