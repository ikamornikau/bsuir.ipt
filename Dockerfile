FROM python:slim

WORKDIR /src

COPY main.py .

CMD ["python", "main.py"]
