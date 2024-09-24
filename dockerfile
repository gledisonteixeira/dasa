# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Instala as dependências
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY . .

CMD ["python", "app.py"]
