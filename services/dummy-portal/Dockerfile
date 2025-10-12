FROM python:3.14-alpine

WORKDIR /app

COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/
COPY tests/ tests/

RUN pytest tests/

CMD ["sh", "-c", "uvicorn src.main:app --host 0.0.0.0 --port ${PORT:-3000}"]