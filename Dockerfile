FROM dhi.io/python:3.14.3-debian13-dev AS build

WORKDIR /app

ENV VIRTUAL_ENV=/app/.venv
ENV PATH="/app/.venv/bin:${PATH}"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY src/requirements.txt .
RUN python -m venv /app/.venv && \
    pip install --no-cache-dir -r requirements.txt

COPY src src/
COPY tests tests/

RUN pytest tests/

FROM dhi.io/python:3.14.3-debian13

WORKDIR /app

ENV VIRTUAL_ENV=/app/.venv
ENV PATH="/app/.venv/bin:${PATH}"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY --from=build /app/.venv /app/.venv
COPY --from=build /app/src /app/src

EXPOSE 3000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "3000"]