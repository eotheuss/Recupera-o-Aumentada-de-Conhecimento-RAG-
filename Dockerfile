# Use uma imagem base do Python
FROM python:3.11-slim

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie o arquivo requirements.txt para o container
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o código da aplicação para o container
COPY . .

# Defina o comando padrão para rodar a aplicação
CMD ["python", "main.py"]
