import fitz  # PyMuPDF
import requests
from io import BytesIO
from langchain_community.llms import Ollama

# Função para baixar o PDF e extrair texto
def extract_text_from_pdf_url(pdf_url):
    response = requests.get(pdf_url)
    response.raise_for_status()  # Verifica se o download foi bem-sucedido
    
    pdf_document = fitz.open(stream=BytesIO(response.content))
    text = ""
    
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    
    return text

# Função para rodar o modelo LLM
def run_llm_model(processed_text):
    # Carregar o modelo
    llm = Ollama()

    # Gerar a resposta usando o LLM
    response = llm.generate([processed_text])  # Passar uma lista de prompts
    
    return response

# URL do PDF
pdf_url = "https://softstar.s3.amazonaws.com/documents/Politica_de_Privacidade.pdf"

# Extrair e processar o texto
processed_text = extract_text_from_pdf_url(pdf_url)

# Rodar o modelo LLM
llm_output = run_llm_model(processed_text)
print(llm_output)
