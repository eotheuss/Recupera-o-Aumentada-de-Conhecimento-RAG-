from pdf_reader import download_pdf, extract_text_from_pdf
from train_model import process_text, train_model
from store_data import store_vectors

def main():
    pdf_url = "https://softstar.s3.amazonaws.com/documents/Politica_de_Privacidade.pdf"
    pdf_file = download_pdf(pdf_url)
    pdf_text = extract_text_from_pdf(pdf_file)

    with open("pdf_text.txt", "w") as file:
        file.write(pdf_text)

    processed_text = process_text(pdf_text)
    with open("processed_text.txt", "w") as file:
        file.write(processed_text)

    model = train_model(processed_text)
    store_vectors(processed_text)
    print("Process completed successfully!")

if __name__ == "__main__":
    main()
