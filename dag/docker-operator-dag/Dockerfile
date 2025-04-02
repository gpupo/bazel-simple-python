FROM python:3.12.9-slim

WORKDIR /app
COPY task.py /app/

# Instala dependências (se necessário)
RUN pip install --no-cache-dir pandas numpy  # Exemplo

CMD ["python", "task.py"]
