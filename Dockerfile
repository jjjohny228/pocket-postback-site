FROM python:3.11-alpine

WORKDIR /postback_site

COPY requirements.txt .

ENV PYTHONPATH=/

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8001", "app:app"]
