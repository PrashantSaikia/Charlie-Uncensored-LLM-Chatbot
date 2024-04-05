FROM python:3.11-slim

ENV PORT ""

ENV OLLAMA_BASE_URL "/ollama"

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "app.py"]
