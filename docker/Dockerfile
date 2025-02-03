# Usa uma imagem base do Python
FROM python:3.9

# Define o diretório de trabalho
WORKDIR /GENAI

# Copia os arquivos para dentro do container
COPY . .

# Instala dependências
RUN pip install -r requirements.txt

# Define a porta que o container irá expor
EXPOSE 5001

# Define o comando de execução
ENTRYPOINT ["python", "./app/app.py"]
