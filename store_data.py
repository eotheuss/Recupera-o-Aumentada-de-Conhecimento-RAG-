import chromadb
from langchain import Vectorizer

def store_vectors(processed_text):
    client = chromadb.Client(uri="http://chroma:8000")
    vectorizer = Vectorizer()
    vectors = vectorizer.vectorize(processed_text)
    client.store_vectors(vectors)

if __name__ == "__main__":
    with open("processed_text.txt", "r") as file:
        processed_text = file.read()
    store_vectors(processed_text)
    print("Vectors stored successfully!")
