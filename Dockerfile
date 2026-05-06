FROM python:latest
WORKDIR /app
COPY . .
RUN pip install -r app/requirements.txt
CMD ["python", "app/app.py"]
